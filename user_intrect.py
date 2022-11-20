from library.list_of_char import *


def len_of_passwd():
    len_of_passwd = input("How Much Length You Want: ")
    # if user put blank defalut value applied
    if len(str(len_of_passwd)) == 0:
        len_of_passwd = 20
    return int(len_of_passwd)


def choice_of_char():
    random_list = []
    random_list.clear()

    ch_smallchar = input("Do yo want small Char?\t[Y/n]: ")
    if ch_smallchar != "n" and ch_smallchar != "N":
        random_list.append(small_char)

    ch_cap_char = input("Do yo want Capital Char?[Y/n]: ")
    if ch_cap_char != "n" and ch_cap_char != "N":
        random_list.append(cap_char)

    ch_numbers = input("Do yo want numbers?\t[Y/n]: ")
    if ch_numbers != "n" and ch_numbers != "N":
        random_list.append(numbers)

    ch_specal_char = input("Do yo Specal char\t[Y/n]: ")
    if ch_specal_char != "n" and ch_specal_char != "N":
        random_list.append(specal_char)

    return random_list


if __name__ == "__main__":
    print("len_of_passwd = \t", len_of_passwd())
    print(choice_of_char())
