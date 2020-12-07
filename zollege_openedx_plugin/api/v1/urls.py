""" urls.py """

from django.conf import settings
from django.conf.urls import url

from zollege_openedx_plugin.api.v1 import views

app_name = "zollege_openedx"  # pylint: disable=invalid-name


PROFILE = ProfileView.as_view({"get": "retrieve", "patch": "partial_update"})


urlpatterns = [  # pylint: disable=invalid-name
    url(r"^profile/{}$".format(settings.USERNAME_PATTERN), PROFILE, name="profile_api")
]
