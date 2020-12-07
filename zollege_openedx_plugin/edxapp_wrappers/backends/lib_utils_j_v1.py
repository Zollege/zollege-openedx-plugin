## Backend for lib utils of edxapp.

from openedx.core.lib.api.parsers import MergePatchParser


def get_merge_patch_parser():
    """ Returns MergePatchParser """
    return MergePatchParser
