#!/usr/bin/env python3
"""
Contains 'Auth'.
"""
import flask
from typing import List, TypeVar
import os


class Auth:
    """
    Auth class.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require_auth method.
        """
        if path is None or excluded_paths is None:
            return True

        if not path.endswith('/'):
            path += '/'

        return path not in excluded_paths

    def authorization_header(self, request: flask.Request = None) -> str:
        """
        authorization_header method.
        """
        if request is None:
            return None

        result = request.headers.get('authorization')

        return result

    def current_user(self, request=None):
        """
        current_user method.
        """
        return None

    def session_cookie(self, request: flask.Request = None):
        """
        docstring
        """
        if request is None:
            return None

        return request.cookies.get(
            os.environ.get("SESSION_NAME", None)
        )
