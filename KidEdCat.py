#User Story 1: As a user I can choose a category and based on what I’ve chosen I will be able to learn it.


import json
import random

def loadCateg():
    with open('Categories.json') as data_file:
        file = json.load(data_file)


    categ = file["categories"]
    return categ

def AskToChooseACateg(categ):
    print ("\nDear user, please choose a category from", (": ").join(categ.keys()))
    chosenCateg = input("Categroy:")

    return chosenCateg


def randomCategKey(chosenCateg, categ):
    with open('Categories.json') as data_file:
        file = json.load(data_file)

    while True:
        if chosenCateg == "animals":
            print("\nHow many animals do you want to learn today?")
            while True:
                number = int(input("Number of animals you want to learn today:"))
                if number < 25:
                    break
                else:
                    print("oops!,try again!")
            yourchoices = random.choices(file["categories"]["animals"], k=number)
            print(yourchoices)
            break

        elif chosenCateg == "colors":
            print("\nHow many colors do you want to learn today?")
            while True:
                number = int(input("Number of colors you want to learn today:"))
                if number < 10:
                    break
                else:
                    print("oops!,try again!")
            yourchoices = random.choices(file["categories"]["colors"], k=number)
            print(yourchoices)
            break

        elif chosenCateg == "alphabet":
            print("\nHow many letters do you want to learn today?")
            while True:
                number = int(input("Number of letters you want to learn today:"))
                if number < 26:
                    break
                else:
                    print("oops!,try again!")
            yourchoices = random.choices(file["categories"]["alphabet"], k=number)
            print(yourchoices)
            break

        elif chosenCateg == "numbers":
            while True:
                number = input("Number of numbers you want to learn today:")
                if (number.isnumeric()):
                    number = int(number)
                    if number < 10:
                        break
                    else:
                        print("oops!,try again!")
                else:
                    print("Please insert numbers only")
            numberlist = []
            for key in file["categories"]["numbers"][0].keys():
                numberlist.append(key)
            yourchoices = random.choices(numberlist, k=number)
            for number in yourchoices:
                print(number, " - ", file["categories"]["numbers"][0][number]["name"])
            break
        else:
            print("Oh wait ynumou chose wrong!")
            chosenCateg = AskToChooseACateg(categ)


def main():
    categorySetup = loadCateg()
    chosenCategory = AskToChooseACateg(categorySetup)
    randomCategKey(chosenCategory, categorySetup)


main()
