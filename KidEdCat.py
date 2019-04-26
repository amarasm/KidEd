#User Story 1: As a user I can choose a category and based on what I’ve chosen I will be able to learn it.


import json
import random

def loadCateg():
    with open('Categories.json') as data_file:
        file = json.load(data_file)


    categ = file["categories"]
    return categ

def AskToChooseACateg(categ):
    print ("\nDear user, please choose a category from", (", ").join(categ.keys()))
    chosenCateg = input("Category:")

    return chosenCateg


def randomCategKey(chosenCateg, categ):
    with open('Categories.json') as data_file:
        file = json.load(data_file)

    while True:
        if chosenCateg == "animals":
            print("\nHow many animals do you want to learn today?Your maximum is 25")
            while True:
                number = input("Number of animals you want to learn today:")
                if number.isnumeric():
                    number = int(number)
                    if number < 26:
                        break
                    else:
                        print("oops!You have to type a number from 1 to 25!Now try again!")
                else:
                    print("Please insert numbers only:)")
            numberlist = []
            for keys in file["categories"]["animals"].keys():
                numberlist.append(keys)
            yourchoices = random.choices(numberlist, k=number)
            for number in yourchoices:
                print("Its name is", number, ", its sound is", file["categories"]["animals"][number]["sound"],"and it's a type of", file["categories"]["animals"][number]["kind"], ".")
            break

        elif chosenCateg == "colors":
            print("\nHow many colors do you want to learn today?Your maximum is 10")
            while True:
                number = input("Number of colors you want to learn today:")
                if number.isnumeric():
                    number = int(number)
                    if number < 11:
                        break
                    else:
                        print("oops!You have to type a number from 1 to 10!Now try again!")
                else:
                    print("Please insert numbers only:)")
            numberlist = []
            for keys in file["categories"]["colors"].keys():
                numberlist.append(keys)
            yourchoices = random.choices(numberlist, k=number)
            for number in yourchoices:
                print(number)
            break

        elif chosenCateg == "alphabet":
            print("\nHow many letters do you want to learn today?Your maximum is 26")
            while True:
                number = input("Number of letters you want to learn today:")
                if number.isnumeric():
                    number = int(number)
                    if number < 27:
                        break
                    else:
                        print("oops!You have to type a number from 1 to 26!Now try again!")
                else:
                    print("Please insert numbers only:)")
            numberlist = []
            for keys in file["categories"]["alphabet"].keys():
                numberlist.append(keys)
            yourchoices = random.choices(numberlist, k=number)
            for number in yourchoices:
                print("the lowercase is",number, "the uppercase is", file["categories"]["alphabet"][number]["upperCase"], ". For example:", file["categories"]["alphabet"][number]["example"])
            break

        elif chosenCateg == "numbers":
            print("\nHow many numbers do you want to learn today?Your maximum is 10")
            while True:
                number = input("Number of numbers you want to learn today:")
                if number.isnumeric():
                    number = int(number)
                    if number < 11:
                        break
                    else:
                        print("oops!You have to type a number from 1 to 10!Now try again!")
                else:
                    print("Please insert numbers only")
            numberlist = []
            for key in file["categories"]["numbers"].keys():
                numberlist.append(key)
            yourchoices = random.choices(numberlist, k=number)
            for number in yourchoices:
                print(number, " - ", file["categories"]["numbers"][number]["name"])
            break
        else:
            print("Oh wait you chose wrong!")
            chosenCateg = AskToChooseACateg(categ)


def main():
    categorySetup = loadCateg()
    chosenCategory = AskToChooseACateg(categorySetup)
    randomCategKey(chosenCategory, categorySetup)


main()
