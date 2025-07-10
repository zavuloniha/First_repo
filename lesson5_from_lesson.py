from faker import Faker

fake = Faker("uk_UA")

def get_fake_user():
    return {
        "name": fake.name(),
        "phone_number": fake.phone_number(), 
        "email": fake.email(),
        "password": fake.password()
    }

print(get_fake_user())