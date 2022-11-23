#!/usr/bin/python3
from logic import main
import tkinter as tk
root = tk.Tk()

# setting the windows size
root.title(" Password Genrator by Kaushal Bhatol")
root.geometry("500x250")

# declaring string variable
# for storing values
prefix_var = tk.StringVar()
length_passwd_var = tk.IntVar()
small_char_var = tk.BooleanVar()
capital_char_var = tk.BooleanVar()
number_char_var = tk.BooleanVar()
special_char_var = tk.BooleanVar()
output_var = tk.StringVar()


def submit():
    prefix = prefix_var.get()
    length_passwd = length_passwd_var.get()
    small_char = small_char_var.get()
    capital_char = capital_char_var.get()
    number_char = number_char_var.get()
    special_char = special_char_var.get()
    output_char = main(prefix, length_passwd, small_char,
                       capital_char, number_char, special_char)

    if __name__ == "__main__":
        print("Prefix is : " + prefix)
        print("Length is : ", length_passwd)
        print("Small char : ", small_char)
        print("Capital char : ", capital_char)
        print("number_char : ", number_char)
        print("special_char: ", special_char)
        print("output char: ", output_char)

    output_var.set(output_char)


# creating a label using widget Label
# prefix
prefix_label = tk.Label(root, text='Enter Prefix',
                        font=('calibre', 10, 'bold'))
prefix_entry = tk.Entry(root, textvariable=prefix_var, width=10,
                        font=('calibre', 10, 'normal'))

# length_passwd
length_passwd_label = tk.Label(root, text='length_passwd',
                               font=('calibre', 10, 'bold'))
length_passwd_entry = tk.Entry(root, textvariable=length_passwd_var, width=10,
                               font=('calibre', 10, 'normal'))
length_passwd_entry.insert(0, 2)

# small char
small_char_label = tk.Label(root, text='Small char',
                            font=('calibre', 10, 'bold'))
small_char_entry = tk.Checkbutton(
    root, variable=small_char_var, onvalue=True, offvalue=False,)

# capital_char
capital_char_label = tk.Label(root, text='Capital char',
                              font=('calibre', 10, 'bold'))
capital_char_entry = tk.Checkbutton(
    root, variable=capital_char_var, onvalue=True, offvalue=False,)

# number_char
number_char_label = tk.Label(root, text='Numbers',
                             font=('calibre', 10, 'bold'))
number_char_entry = tk.Checkbutton(
    root, variable=number_char_var, onvalue=True, offvalue=False,)

# special_char
special_char_label = tk.Label(root, text='Special Char',
                              font=('calibre', 10, 'bold'))
special_char_entry = tk.Checkbutton(
    root, variable=special_char_var, onvalue=True, offvalue=False,)

# output
output_label = tk.Label(root, text='Genrated passwd: ',
                        font=('calibre', 10, 'bold'))
output_entry = tk.Entry(root, textvariable=output_var, width=26,
                        font=('calibre', 10, 'normal'))

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(root, text='Submit', command=submit)

# placing the label and entry in
# the required position using grid
# method
prefix_label.grid(row=0, column=0)
prefix_entry.grid(row=0, column=2)
length_passwd_label.grid(row=1, column=0)
length_passwd_entry.grid(row=1, column=2)
small_char_label.grid(row=2, column=0)
small_char_entry.grid(row=2, column=1)
capital_char_label.grid(row=3, column=0)
capital_char_entry.grid(row=3, column=1)
number_char_label.grid(row=4, column=0)
number_char_entry.grid(row=4, column=1)
special_char_label.grid(row=5, column=0)
special_char_entry.grid(row=5, column=1)
sub_btn.grid(row=6, column=1)
output_label.place(x=10, y=200)
output_entry.place(x=190, y=200)

# performing an infinite loop
# for the window to display
root.mainloop()
