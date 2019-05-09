import json

def loadCateg():
    with open('Categories.json') as data_file:
        file = json.load(data_file)
    categ = file["categories"]["colors"]
    return categ

def showPrimaryColors(categ):

    for color,data in categ.items():
        if data["isPrimaryColor"] == True:
            print(color + " is a primary color")
        else:
            print("the color " + color + " is not a primary color")


def main():
    categorySetup = loadCateg()
    primaryColor = showPrimaryColors(categorySetup)

main()