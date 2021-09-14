from sys import maxsize


class Contact:

    def __init__(self, firstname, middlename, address, mobile, lastname, nickname, title, company, home_phone_number,
                 work_phone_number, fax_number, email_1,
                 email_2, email_3, bday, bmonth, byear, aday, amonth, ayear, address_2, phone_2, notes, id):
        self.firstname = firstname
        self.middlename = middlename
        self.address = address
        self.mobile = mobile
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.home = home_phone_number
        self.work = work_phone_number
        self.fax = fax_number
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address_2
        self.phone2 = phone_2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.name and\
               self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
