import random
import re


def generatepassword():
    var = 1
    while var == 1:

        print("\nPASSWORD GENERATOR")

        print("Minimum length of password should be 3")

        UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                     'V', 'W', 'X', 'Y', 'Z']
        LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                     'v', 'w', 'x', 'y', 'z']
        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        SPECIAL = ['@', '#', '$', '=', ':', '?', '.', '/', '|', '~', '>', '*', '<']

        strong_list = DIGITS + UPPERCASE + LOWERCASE + SPECIAL
        weak_list = LOWERCASE + DIGITS

        password = []
        print("strength of password ""\n1.weak\n2.strong\n3.exit")
        passwordstrength = int(input("enter option:"))

        if (passwordstrength == 1):
            length1 = int(input("Enter the length of Password  "))

            if (length1 < 3):
                length1 = 3
            password = "".join(random.sample(weak_list, length1))


        elif (passwordstrength == 2):
            print("minimum length should be 8")

            length2 = int(input("Enter the length of Password : "))
            if (length2 > 7):
                 password = "".join(random.sample(strong_list, length2))
            else:
             print("invalid length")


        elif (passwordstrength == 3):
            return

        else:
            print("enter valid options")

        print("Generating  password\n", password)


def strengthcheck():
    password = input("Enter the password:")
    if (len(password) >= 3):
        if (bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&|*]).{3,100})', password)) == True):
            print("The password is strong")
        # elif (bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{3,100})', password)) == True):
        else:
            print("The password is weak")
    else:
        print("You have entered an invalid password.")


def main():
    var = 1
    while var == 1:
        print("password manager")
        print("\n1.password generator\n2.password strength checker\n3.exit")
        option = int(input("enter option :"))

        if (option == 1):
            Password = generatepassword()
        elif (option == 2):
            strength = strengthcheck()

        elif (option == 3):
            return

        else:
            print("enter valid options")


main()
