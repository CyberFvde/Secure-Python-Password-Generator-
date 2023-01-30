import string   # import the string module
import random   # import the random module

def generate_password(length=16):   # define a function to generate password, default length is 16
    chars = string.ascii_letters + string.digits + string.punctuation   # create a string of all characters: letters, digits and punctuation marks
    password = ''.join(random.choice(chars) for i in range(length))   # choose a random character from the `chars` string and join them to form a password
    return password   # return the password

print(generate_password())   # call the function and print the password
