#!/bin/python3
from random import choice   # using random module for choice function
import library.user_intrect as ui   # importing user_intrect module as ui

passwd = ""  # blank passwd string
choice_of_char = ui.choice_of_char()

# loop for appending random character in passwd string
for i in range(ui.len_of_passwd()):
    random_char = choice(choice(choice_of_char))
    passwd += random_char

print(passwd)
