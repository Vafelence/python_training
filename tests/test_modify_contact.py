from model.contact import Contact


def test_modify_contact(app):
    app.contact.modify_first_contact(Contact(firstname="New person", middlename="New middlename"))
