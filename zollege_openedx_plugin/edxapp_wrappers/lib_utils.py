#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Users public function definitions
"""

from importlib import import_module

from django.conf import settings


def get_merge_patch_parser():
    """
    Return MergePatchParser.
    """
    backend_function = settings.ZOLLEGE_LIB_UTILS_BACKEND
    backend = import_module(backend_function)
    return backend.get_merge_patch_parser()
