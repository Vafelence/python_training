# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_new_contact(app):
    app.contact.create_contact(Contact(firstname="joe", middlename="barbaro", address="russia", mobile="nokia",
                                       lastname="scaletta", nickname="kot", title="cocos", company="pits", home_phone_number="grove street",
                                       work_phone_number="hard", fax_number="1029384756", email_1="1@1.ru", email_2="2@2.ru", email_3="3@3.ru",
                                       bday="15", bmonth="May", byear="1996", aday="10", amonth="June", ayear="1991",
                                       address_2="world", phone_2="7963852741", notes="abvgde"))


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="123", header="123", footer="123")
    app.group.create_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
