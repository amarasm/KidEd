#Final app!


import json
import random


def finalQuestion():
    while True:
        question = input("\nDear user do you want to exit the app or continue it? If you want to exit type exit, if not type continue!")
        if question == "exit":
            print("\nThank you for using our app! :)")
            break
        elif question == "continue":
            setUpGame()
        else:
            print("You either had a typo or you chose incorrectly. Please try again")

def setUpGame():
    print("\nDear user, this application is for kids of age 3 to 6.\nBefore we start, let me know what you want to do first!\nDo you want to start learning or to make some changes in the categories?")
    while True:
        choiceOfTheUser = int(input("1-Start learning" + "\n2-Make changes\ntype 1 to start learning and type 2 to make changes!"))
        if choiceOfTheUser == 1:
            def loadCateg():
                with open('Categories.json') as data_file:
                    file = json.load(data_file)
                categ = file["categories"]
                return categ

            def AskToChooseACateg(categ):
                print("\nDear user, please choose a category from", (", ").join(categ.keys()))
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
                            print("Its name is", number, ", its sound is", file["categories"]["animals"][number]["sound"],
                                  "and it's a type of", file["categories"]["animals"][number]["kind"], ".")
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

                        def loadCateg():
                            with open('Categories.json') as data_file:
                                file = json.load(data_file)
                            categ = file["categories"]["colors"]
                            return categ

                        def showPrimaryColors(categ):
                            while True:
                                learnPrimeColor = (input("Do you want to learn the primary colors too?"))
                                if learnPrimeColor == "no":
                                    print("Okay!If you change your mind visit again!:D")
                                    break
                                elif learnPrimeColor != "yes":
                                    print("I think you had a typo! Try again")
                                else:
                                    for color, data in categ.items():
                                        if data["isPrimaryColor"] == True:
                                            print(color + " is a primary color")
                                        else:
                                            print("the color " + color + " is not a primary color")
                                    print("\nAmazing! You have learned the primary colors too! Good Job :)")
                                    break

                        def main():
                            categorySetup = loadCateg()
                            primaryColor = showPrimaryColors(categorySetup)

                        main()
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
                            print("the lowercase is", number, "the uppercase is",
                                  file["categories"]["alphabet"][number]["upperCase"], ". For example:",
                                  file["categories"]["alphabet"][number]["example"])
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
                    elif chosenCateg in categ.keys():
                        LengthOfDefault = len(categ[chosenCateg].items())
                        print("\nHow many ", chosenCateg, " do you want to learn today?Your maximum is ",
                              LengthOfDefault)
                        while True:
                            number = input("input the number here:")
                            if number.isnumeric():
                                number = int(number)
                                if number <= (LengthOfDefault):
                                    break
                                else:
                                    print("oops!You have to type a number from 1 to ", LengthOfDefault,
                                          "!Now try again!")
                            else:
                                print("Please insert numbers only")
                        numberlist = []
                        for key, item in categ[chosenCateg].items():
                            numberlist.append(key)
                        yourchoices = random.choices(numberlist, k=number)
                        for number in yourchoices:
                            print(number, " - ", file["categories"][chosenCateg][number]["name"])
                        break
                    else:
                        print("Oh wait your choice is not in the categories!Please try again :)")
                        chosenCateg = AskToChooseACateg(categ)

            def main():
                categorySetup = loadCateg()
                chosenCategory = AskToChooseACateg(categorySetup)
                randomCategKey(chosenCategory, categorySetup)

            main()
            break
        elif choiceOfTheUser == 2:
            def loadCateg():
                with open('Categories.json') as data_file:
                    file = json.load(data_file)
                return file

            def printLengthOfTheCategory(categ):
                print("\nThe length of the category is currently", len(categ["categories"]))

            def additionToCateg(file):

                while True:
                    Addition = input("\nDear programmer do you want to add another category to the current one? Please say either yes or no")
                    if Addition == "no":
                        print("okay!")
                        break
                    elif Addition == "yes":
                        addToCateg = input("What do you want to add?")
                        file["categories"][addToCateg] = {}
                        newCategory = file["categories"][addToCateg]
                        while True:
                            addingTopic = input("Do you want to add topic to the category: " + addToCateg + "? say either yes or no!")
                            if addingTopic == "no":
                                break
                            elif addingTopic != "yes":
                                print("you had a typo I guess")
                            else:
                                newTopic = {}
                                newTopicKey = input("Please tell me the key")
                                newTopic["name"] = input("Please add the display name")
                                newCategory[newTopicKey] = newTopic
                                data_file = open("categories.json", "w")
                                data_file.write(json.dumps(file))
                                data_file.close()
                    else:
                        print("Nope, please write yes or no! It's simple :D")
                return file

            def main():
                loadCategory = loadCateg()
                printLengthOfTheCategory(loadCategory)
                newFile = additionToCateg(loadCategory)
                printLengthOfTheCategory(newFile)

            main()

            break
        else:
            print("\nJust choose between 1 and 2 please!")

def main():
    startGame = setUpGame()


main()
finalQuestion()


