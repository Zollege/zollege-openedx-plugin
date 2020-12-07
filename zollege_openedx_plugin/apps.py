"""
App configuration for zollege_openedx_plugin.
"""

from __future__ import unicode_literals

from django.apps import AppConfig


class ZollegePluginConfig(AppConfig):
    """
    Zollege Open edX plugin configuration.
    """

    name = "zollege_openedx_plugin"
    verbose_name = "Zollege Open edX plugin"

    plugin_app = {
        "url_config": {
            "lms.djangoapp": {
                "namespace": "zollege_openedx_plugin",
                "regex": r"^zollege-openedx/",
                "relative_path": "urls",
            }
        },
        "settings_config": {
            "lms.djangoapp": {
                "common": {"relative_path": "settings.common"},
                "test": {"relative_path": "settings.test"},
                "production": {"relative_path": "settings.production"},
            },
            "cms.djangoapp": {
                "common": {"relative_path": "settings.common"},
                "test": {"relative_path": "settings.test"},
                "production": {"relative_path": "settings.production"},
            },
        },
    }
