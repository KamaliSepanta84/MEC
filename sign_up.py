from argon2 import *
from hashlib import *
import os


def sign_up(user_name , password , security_level):
    user_name = user_name
    password = password
    security_level = security_level
    encrypted_password = encrypt(user_name, password, security_level)
    print(encrypted_password)
    
def encrypt(user_name, password , security_level):
    time_cost , memory_cost = get_security_level(security_level)
    salt = custom_salt(user_name)
    user_hashed_password = hash_password(password , time_cost , memory_cost , salt)
    return user_hashed_password


def hash_password(user_password: str , time_cost: int , memory_cost:int , salt: str) -> str:
    ph = PasswordHasher(time_cost= time_cost , memory_cost= memory_cost)
    password = user_password
    hashed_password = ph.hash(password + salt)
    return hashed_password


def custom_salt(user_name:str) -> str:
    random_value = os.urandom(16)
    generated_salt = sha256(user_name.encode() + random_value).hexdigest()
    return generated_salt



def get_security_level(security_level: str) -> tuple:
    if security_level == "Medium":
        time_cost = 2
        memory_cost = 1024
    elif security_level == "High":
        time_cost = 4
        memory_cost = 2048
    elif security_level == "Very High":
        time_cost = 6
        memory_cost = 4096
    return time_cost, memory_cost



sign_up("luca" , "Mawyin" , "Very High")