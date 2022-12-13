password = "Davian"
username = "Sanchit"


def inputting_username():
    global ue
    ue = input("Enter username")
    if ue == username:
        inputting_password()
    else:
        print("The username is not correct please try again")
        inputting_username()


def inputting_password():
    pe = input("Enter password")
    if pe == password:
        print("welocme", ue)
    else:
        print("The password is incorrect")
        decision()


def decision():
    decision = input(
        "If you want to retrieve password enter 'A' and if you want to try entering again enter 'B'")
    print()
    if decision == 'B':
        inputting_password()
    elif decision == "A":
        retrieve()
    else:
        print("Wrong decision")
        retrieve()


def retrieve():
    guess = input("Guess your password")
    if len(guess) != len(password):
        if len(guess) > len(password):
            print("it is longer than the registered password")
        else:
            print("It is smaller than the registered password")
        retrieve()
    else:
        if guess == password:
            print("The password is retrieved:", password)
            exit()
        else:
            print("Guessed password is of the length of the registered password")
            s = ""
            for i in guess:
                if i in password:
                    print(i, " exists in registered password")
                    s = s+i
            if len(s) == len(password):
                if s == password:
                    print("password retrieved")
                    exit()
                else:
                    print(
                        "All the characters of password are present in the guessed password. Try resuffling the characters")
                    print("The first 2 characters of teh password are:",
                          password[0], password[1])
            print("Retry guessing password again")
            print()
            retrieve()


def call():
    inputting_username()
