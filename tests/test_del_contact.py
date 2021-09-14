from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        contact = Contact(firstname="joe", middlename="barbaro", address="russia", mobile="nokia",
                          lastname="scaletta", nickname="kot", title="cocos", company="pits",
                          home_phone_number="grove street",
                          work_phone_number="hard", fax_number="1029384756", email_1="1@1.ru", email_2="2@2.ru",
                          email_3="3@3.ru",
                          bday="15", bmonth="May", byear="1996", aday="10", amonth="June", ayear="1991",
                          address_2="world", phone_2="7963852741", notes="abvgde")
        app.contact.create_contact(contact)
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
