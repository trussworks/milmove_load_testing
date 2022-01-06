# -*- coding: utf-8 -*-
"""
This file should contain our custom TaskSets that can then be used in our tasks files.
"""
from locust import TaskSet

from utils.request import MilMoveRequestMixin
from utils.rest import RestMixin


class RestTaskSet(MilMoveRequestMixin, RestMixin, TaskSet):
    """
    A convenience class for testing REST JSON endpoints.
    """


class LoginTaskSet(RestMixin, TaskSet):
    """
    TaskSet that grabs the CSRF and session tokens for the user and creates a fake logon for making requests.
    """

    def __init__(self, parent):
        self.csrf_token = None
        self.session_token = None

        super().__init__(parent)

    def _set_csrf_token(self):
        """
        Pull the CSRF token from the website by hitting the root URL.
        This token is set as a cookie with the name `masked_gorilla_csrf`.
        """
        self.client.get("/devlocal-auth/login")
        self.csrf_token = self.client.cookies.get("masked_gorilla_csrf")

    def _create_login(self, user_type, session_token_name):
        """
        Creates a login for the given user type and grabs the session cookie for later use.
        :param user_type: str
        :param session_token_name: str
        :return: response
        """
        resp = self.client.post(
            "/devlocal-auth/create", data={"userType": user_type, "gorilla.csrf.Token": self.csrf_token}
        )
        self.session_token = self.client.cookies.get(session_token_name)

        return resp

    def _logout(self):
        """
        Logs the current user out of the session. Can be followed by an interrupt or by logging in again.
        """
        self.client.post("/auth/logout")
        self.session_token = None

    def on_start(self):
        """
        Grab the CSRF token from the base url and update the headers with that value before any tasks execute.
        """
        self._set_csrf_token()
        self.client.headers.update({"x-csrf-token": self.csrf_token})