#ToDo - Please insert your story here:


import json
import random

def loadCateg():
    with open('Categories.json') as data_file:
        file = json.load(data_file)


    categ = file["categories"]
    return categ

def AskToChooseACateg(categ):
    print ("\nDear user, please choose a category from", (", ").join(categ.keys()))
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
            print("\nHow many numbers do you want to learn today?")
            while True:
                number = int(input("Number of numbers you want to learn today:"))
                if number < 10:
                    break
                else:
                    print("oops!,try again!")
            yourchoices = random.choices(file["categories"]["numbers"], k=number)
            print(yourchoices)
            break

        else:
            print("Oh wait you chose wrong!")
            chosenCateg = AskToChooseACateg(categ)


def main():
    categorySetup = loadCateg()
    chosenCategory = AskToChooseACateg(categorySetup)
    randomCategKey(chosenCategory, categorySetup)


main()
