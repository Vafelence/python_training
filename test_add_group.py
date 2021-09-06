# -*- coding: utf-8 -*-
import pytest
from group import group
from application import application

@pytest.fixture
def app(request):
    fixture = application()
    request.addfinalizer(fixture.Destroy)
    return fixture

def test_add_group(app):
        app.login(username="admin", password="secret")
        app.create_group(group(name="test", header="testing", footer="auto-testing"))
        app.logout()

def test_add_empty_group(app):
        app.login(username="admin", password="secret")
        app.create_group(group(name="", header="", footer=""))
        app.logout()

