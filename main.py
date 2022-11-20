#!/bin/python3
from random import choice   # using random module for choice function
import library.user_intrect as ui   # importing user_intrect module as ui

passwd = ui.prefix()
length = ui.len_of_passwd()-len(passwd)

if len(passwd) > length:
    print("Please enter valid length")
else:
    choice_of_char = ui.choice_of_char()
    # loop for appending random character in passwd string
    for i in range(length):
        random_char = choice(choice(choice_of_char))
        passwd += random_char

    print("Your password is:", passwd)
