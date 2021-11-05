def menu():
    print(" ------------------------------------------------")
    print("|                                                |")
    print("|    07Menu                                      |")
    print("|    Name : Khyati                               |")
    print("|    Version : 01                                |")
    print("|                                                |")
    print(" ------------------------------------------------")


    print("1. Hello World")
    print("2. Goodbye World ")
    print("3. Goodbye Person")
    print("4. Good Teacher")
    print("5. forLoop")
    print("6. whileLoop")
    print("7. string Loop")
    print("8. Convert to ascii")
    print("9. Encode a string")
    print("x. To Exit")


def hello_world():
    print("Hello World")

def goodbye_world():
    print("Hello World")
    input("------> Program paused - press enter to continue")
    print("Goodbye World")

def goodbye_person():
    print("Hello")
    name = input("What is your name ? " )
    print("Goodbye " + name)

def good_teacher():
    name = input("Teacher name (try Mr Horan) " )
    if name == "Mr Horan":
        print ("You are lucky, he is a great teacher.")
    else:
        print (name + " is an ok teacher")

def for_Loop():
    for x in range(1,500):  
        print(x)


def while_Loop():
    x=0
    while x == 0:
        subject = input("What is the name of this subject ")
        if subject == "IST":
            print(" ")
            print(" ")
            print("Congratulations!!")
            print(" ")
            print(" ")
            print(" ")
            break
        else:
            print("Not Correct - try again")


while True:
    menu()
    number = input("Enter an option ")
    print(" ")
    valid_options = ('1', '2', '3', '4', '5', '6', 'x')
    print("----Start of Output ---------------------------")
    print (" ")
    if number in valid_options:
        if number.lower() == 'x':
            print(" ")
            print("----End of Output -----------------------------")
            print(" ")
            print(" ")
            print("Press Enter to continue ")
            break
        elif number == "1":
            hello_world()

        elif number == "2":
            goodbye_world()

        elif number == "3":
            goodbye_person()
        
        elif number == "4":
            good_teacher()

        elif number == "5":
            for_Loop()
        
        elif number == "6":
            while_Loop()

    else:
        print("Invalid option")

    print("")
    print("----End of Output -----------------------------")
    print(" ")
    print(" ")
    print(" ")

    input("Press Enter to continue ")