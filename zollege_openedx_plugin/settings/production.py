"""
Production Django settings for zollege_openedx_plugin project.
"""

from __future__ import unicode_literals


def plugin_settings(settings):
    """
    Set of plugin settings used by the Open Edx platform.
    More info: https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/plugins/README.rst
    """
    settings.SCORMXBLOCK_ASYNC_THRESHOLD = settings.ENV_TOKENS.get('SCORMXBLOCK_ASYNC_THRESHOLD', 150)
