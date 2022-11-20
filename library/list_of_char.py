import string

small_char = list(string.ascii_lowercase)
cap_char = list(string.ascii_uppercase)
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
specal_char = ['~', ':', "'", '+', '[', '\\', '@', '^',
               '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

if __name__ == "__main__":
    print(small_char)
    print(cap_char)
    print(numbers)
    print(specal_char)
