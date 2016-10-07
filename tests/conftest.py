import os

import pytest
from flask import Flask
from webtest import TestApp

from app import app as main_app


@pytest.yield_fixture(scope='function')
def app():
    """An application for the tests."""
    _app = main_app
    _app.config['TESTING'] = True
    _app.config['DEBUG'] = False

    ctx = _app.test_request_context()
    ctx.push()

    yield _app


@pytest.fixture(scope='function')
def test_client(app):
    client = TestApp(app)
    return client
