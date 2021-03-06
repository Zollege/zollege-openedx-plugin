import json

from django.core.exceptions import ObjectDoesNotExist

from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication
from edx_rest_framework_extensions.auth.session.authentication import (
    SessionAuthenticationAllowInactiveUser,
)


from zollege_openedx_plugin.edxapp_wrappers.users import (
    get_edxapp_user_model,
    get_user_profile_model,
    get_user_api_errors,
    get_user_api_helpers,
    get_account_settings,
    get_bearer_authentication_allow_inactive_user,
)

from zollege_openedx_plugin.edxapp_wrappers.lib_utils import get_merge_patch_parser

errors = get_user_api_errors()
User = get_edxapp_user_model()
UserProfile = get_user_profile_model()
helpers = get_user_api_helpers()
BearerAuthenticationAllowInactiveUser = get_bearer_authentication_allow_inactive_user()
MergePatchParser = get_merge_patch_parser()


class ProfileView(ViewSet):

    authentication_classes = (
        JwtAuthentication,
        BearerAuthenticationAllowInactiveUser,
        SessionAuthenticationAllowInactiveUser,
    )
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (MergePatchParser,)

    def retrieve(self, request, username):
        """
        GET /api/user/v1/accounts/{username}/
        """
        try:
            account_settings = get_account_settings(
                request, [username], view=request.query_params.get("view")
            )
        except errors.UserNotFound:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(account_settings[0])

    def partial_update(self, request, username):
        """
        PATCH /api/user/v1/profile/{username}/
        """
        try:
            with transaction.atomic():
                update_profile(request.user, request.data, username=username)
                account_settings = get_account_settings(request, [username])[0]
        except errors.UserNotAuthorized:
            return Response(status=status.HTTP_403_FORBIDDEN)
        except errors.UserNotFound:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except errors.AccountValidationError as err:
            return Response(
                {"field_errors": err.field_errors}, status=status.HTTP_400_BAD_REQUEST
            )
        except errors.AccountUpdateError as err:
            return Response(
                {
                    "developer_message": err.developer_message,
                    "user_message": err.user_message,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(account_settings)


@helpers.intercept_errors(
    errors.UserAPIInternalError, ignore_errors=[errors.UserAPIRequestError]
)
def update_profile(requesting_user, update, username=None):
    """Update user profile information.
    currently only handles meta

    """
    # Get user
    if username is None:
        username = requesting_user.username
    user, user_profile = _get_user_and_profile(username)
    """
    1. if existing meta is blank or not an object, enforce that provided meta is JSON and override entire field
    2. if provided meta is invalid json, raise error
    3. if both are valid json, merge
    """
    if not requesting_user.is_superuser:
        raise errors.UserNotAuthorized()
    try:
        updated_meta = json.loads(update["meta"])
    except json.decoder.JSONDecodeError as err:
        raise errors.AccountValidationError(["meta must be json"])

    if not user_profile.meta:
        user_profile.meta = update["meta"]
        user_profile.save()
        return
    try:
        meta_to_update = json.loads(user_profile.meta)
    except json.decoder.JSONDecodeError as err:
        user_profile.meta = update["meta"]
        user_profile.save()
        return
    for key in updated_meta:
        meta_to_update[key] = updated_meta[key]
    user_profile.meta = meta_to_update
    user_profile.save()


def _get_user_and_profile(username):
    """
    Helper method to return the legacy user and profile objects based on username.
    """
    try:
        existing_user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        raise errors.UserNotFound()

    existing_user_profile, _ = UserProfile.objects.get_or_create(user=existing_user)

    return existing_user, existing_user_profile
