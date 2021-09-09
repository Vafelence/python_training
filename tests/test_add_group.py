# -*- coding: utf-8 -*-
import pytest
from model.group import group
from fixture.application import application

@pytest.fixture
def app(request):
    fixture = application()
    request.addfinalizer(fixture.Destroy)
    return fixture

def test_add_group(app):
        app.session.login(username="admin", password="secret")
        app.create_group(group(name="test", header="testing", footer="auto-testing"))
        app.session.logout()

def test_add_empty_group(app):
        app.session.login(username="admin", password="secret")
        app.create_group(group(name="", header="", footer=""))
        app.session.logout()

