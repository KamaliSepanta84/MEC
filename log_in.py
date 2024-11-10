import userObj
from argon2 import *
from hashlib import *


def log_in(user_name, password):
    user = userObj.hashObj_instance
    my_user = user[user_name]
    my_salt = my_user["Salt"]
    user_login_password = encryption2(password , my_salt)
    return user_login_password == my_user["Hashed_Password"]


def encryption2(password , salt):
    ph = PasswordHasher(time_cost= 6 , memory_cost= 4096)
    hashed_password = ph.hash(password + salt)
    return hashed_password


