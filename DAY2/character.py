def character(char):
    if char.isalpha():
        return "Alphabet"
    elif char.isdigit():
        return "Digits"
    else:
        return "Special Characters"
a=input("Enter a Character: ")
print(character(a))