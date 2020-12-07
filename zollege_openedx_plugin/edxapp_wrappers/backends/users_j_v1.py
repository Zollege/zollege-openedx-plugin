# edxapp user backend compatible with Juniper.

from student.models import User, UserProfile  # pylint: disable=import-error

from openedx.core.lib.api.authentication import (
    BearerAuthenticationAllowInactiveUser,
)  # pylint: disable=import-error
from openedx.core.djangoapps.user_api.accounts.api import (
    get_account_settings as edxapp_get_account_settings,
)  # pylint: disable=import-error
from openedx.core.djangoapps.user_api import (
    errors as user_api_errors,
)  # pylint: disable=import-error
from openedx.core.djangoapps.user_api import (
    helpers as user_api_helpers,
)  # pylint: disable=import-error


def get_edxapp_user_model():
    """ Gets the edxapp User model. """
    return User


def get_user_profile_model():
    """ Gets the UserProfile model. """
    return UserProfile


def get_user_api_errors():
    """ Gets user api errors module. """
    return user_api_errors


def get_user_api_helpers():
    """ Gets user api helpers module. """
    return user_api_helpers


def get_account_settings(*args, **kwargs):
    """ Gets get_account_setting function/ """
    return edxapp_get_account_settings(*args, **kwargs)


def get_bearer_authentication_allow_inactive_user():
    """ return the BearerAuthenticationAllowInactiveUser class"""
    return BearerAuthenticationAllowInactiveUser
