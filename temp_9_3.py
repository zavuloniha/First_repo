class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None

    def remove_contacts(self, id):
        result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
        if len(result) > 0:
            self.contacts.remove(result[0]) 
            return self.contacts
list_contact = Contacts()
list_contact.add_contacts("Wylie Pope2", "(692) 802-29492", "est@utquamvel.net2", True)
list_contact.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
print(list_contact.list_contacts())
print(list_contact.get_contact_by_id(2))
print(list_contact.remove_contacts(2))
