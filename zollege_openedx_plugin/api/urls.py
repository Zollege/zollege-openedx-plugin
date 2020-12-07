""" urls.py """

from django.conf.urls import include, url

app_name = "zollege_openedx"  # pylint: disable=invalid-name

urlpatterns = [  # pylint: disable=invalid-name
    url(
        r"^v1/",
        include("zollege_openedx_plugin.api.v1.urls", namespace="zollege-openedx-api"),
    )
]
