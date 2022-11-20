#!/bin/python3
from random import choice
import user_intrect as ui

passwd = ""
choice_of_char = ui.choice_of_char()

for i in range(ui.len_of_passwd()):
    random_char = choice(choice(choice_of_char))
    passwd += random_char

print(passwd)
