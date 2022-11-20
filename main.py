#!/bin/python3
from random import choice

charlen = 20
passwd = ""

small_char = ["a", "b", "c", "d", "e", "f"]
cap_char = ["A", "B", "c", "D", "E", "F"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
specal_char = ["!", "@", "#", "$", "%", "&", "*"]
random_list = [small_char, cap_char, numbers, specal_char]

for i in range(charlen):
    rand_passwd = choice(choice(random_list))
    passwd += rand_passwd

print(passwd)
