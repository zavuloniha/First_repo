from lesson5_from_lesson import get_fake_user


filename = input("Enter filename >>> ")
amount = int(input("How many users to generate >>> "))

with open(filename, "w") as file:
    users = []
    for _ in range(amount):
        users.append(str(get_fake_user(), ensure_ascii=False))

    file.writelines(users)  