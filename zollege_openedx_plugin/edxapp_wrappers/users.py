#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Users public function definitions
"""

from importlib import import_module

from django.conf import settings


def get_edxapp_user_model():
    """ Gets user model defined in edxapp. """
    backend_function = settings.ZOLLEGE_USERS_BACKEND
    backend = import_module(backend_function)

    return backend.get_edxapp_user_model()


def get_user_profile_model():
    """ Gets edxapp user profile model """

    backend_function = settings.ZOLLEGE_USERS_BACKEND
    backend = import_module(backend_function)

    return backend.get_user_profile_model()


def get_user_api_errors():
    """ Get user_api error module. """
    backend_function = settings.ZOLLEGE_USERS_BACKEND
    backend = import_module(backend_function)

    return backend.get_user_api_errors()


def get_user_api_helpers():
    """ Get user api helpers module. """
    backend_function = settings.ZOLLEGE_USERS_BACKEND
    backend = import_module(backend_function)

    return backend.get_user_api_helpers()


def get_account_settings(*args, **kwargs):
    """
    Wrapper for openedx get_account_settings function.
    """
    backend_function = settings.ZOLLEGE_USERS_BACKEND
    backend = import_module(backend_function)
    return backend.get_account_settings(*args, **kwargs)


def get_bearer_authentication_allow_inactive_user():
    """
    Gets BearerAuthenticationAllowInactiveUser class.
    """
    backend_function = settings.ZOLLEGE_USERS_BACKEND
    backend = import_module(backend_function)
    return backend.get_bearer_authentication_allow_inactive_user()
