class Mammal:
    phrase = ''

    def voice(self):
        return self.phrase

class Dog(Mammal):
    phrase = 'Bark!'

class Cat(Mammal):
    phrase = 'Meow!'

class Chupakabra:
    def voice(self):
        return 'Whooooo!!!'

class Recorder:
    def record_animal(self, animal):
        voice = animal.voice()
        print(f'Recorded "{voice}"')

r = Recorder()
cat = Cat()
dog = Dog()
strange_animal = Chupakabra()

r.record_animal(cat)  # Recorded "Meow!"
r.record_animal(dog)  # Recorded "Bark!"
r.record_animal(strange_animal)  # Recorded "Whooooo!!!"






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
        for item in self.contacts:
            if id in item.contact:
               return f'{item.self.contact}'
            else: 
                return None


list_contact = Contacts()
list_contact.add_contacts("Wylie Pope2", "(692) 802-29492", "est@utquamvel.net2", True)

list_contact.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
print(list_contact.list_contacts())
print(list_contact.get_contact_by_id(2))