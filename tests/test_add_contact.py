# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_create_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="joe", middlename="barbaro", address="russia", mobile="nokia",
                                       lastname="scaletta", nickname="kot", title="cocos", company="pits", home_phone_number="grove street",
                                       work_phone_number="hard", fax_number="1029384756", email_1="1@1.ru", email_2="2@2.ru", email_3="3@3.ru",
                                       bday="15", bmonth="May", byear="1996", aday="10", amonth="June", ayear="1991",
                                       address_2="world", phone_2="7963852741", notes="abvgde"))
    app.session.logout()
    #123