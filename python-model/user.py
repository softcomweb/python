from pprint import pprint
from model.user import User
from schema.user import userEntity, usersEntity

user1 = User(
    "leadel", "kolo", "leadel@localhost.com", "passwort1!", "starstr", "IT-Specialist"
)
user1.set_id()
user2 = User(
    "nicole",
    "kolomingi",
    "nicole@localhost.com",
    "passwort1000!",
    "starstr 200",
    "Buchhalterin",
)
user2.set_id()
user3 = User(
    "jamie",
    "kolomongo",
    "jamie@localhost.com",
    "passwort2000!",
    "starstr 300",
    "Student",
)
user3.set_id()

userEntityList = [user1, user2, user3]

for user in userEntityList:
    print(userEntity(user.to_obj()))
