#User Story 3: As a user I can learn which colors are primary colors and which are not!

import json

def loadCateg():
    with open('Categories.json') as data_file:
        file = json.load(data_file)
    categ = file["categories"]["colors"]
    return categ

def showPrimaryColors(categ):
    while True:
        if (input("Dear user do you want to learn the primary colors?") != "yes"):
            print("Okay!If you change your mind visit again!:D")
            break
        else:
            for color,data in categ.items():
                if data["isPrimaryColor"] == True:
                    print(color + " is a primary color")
                else:
                    print("the color " + color + " is not a primary color")


def main():
    categorySetup = loadCateg()
    primaryColor = showPrimaryColors(categorySetup)

main()
