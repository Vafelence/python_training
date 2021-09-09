from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Roman", mobile="7894561230"))
    app.group.delete_first_contact()