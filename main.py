import random


# generates number
def generator():
    rand = random.randint(0, 100)
    print(rand)


# gives option to quit or generate new number
def redo():
    cont = input("Press n to quit: ")
    if cont != "n":
        beginning()
    else:
        print("Have a nice day!")


# allows loop to work
def beginning():
    generator()
    redo()


beginning()