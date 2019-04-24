import json

def loadCateg():
    with open('Categories.json') as data_file:
        file = json.load(data_file)


    categ = file["categories"]
    return categ

def length(categ):
    print("\nThe length of the category is currently", len(categ))

def saveNewCateg(newTopic):
    data_file = open("categories.json", "w")
    data_file.write(json.dumps(newTopic))
    data_file.close()


def additionToCateg(categ):
    with open('Categories.json') as data_file:
        file = json.load(data_file)

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
                if (input("Do you want to add topic to the category: " + addToCateg + "? say either yes or no!") != "yes"):
                    break
                else:
                    newTopic = {}
                    newTopicKey = input("Please tell me the key")
                    newTopic["name"] = input("Please add the display name")
                    newCategory[newTopicKey] = newTopic
                    saveNewCategory = saveNewCateg(newCategory[newTopicKey])
        else:
            print("Nope, please write yes or no! It's simple :D")
    return newTopic



def currLength(length):
    print(length)

def main():
    loadCategory = loadCateg()
    lengthOfTheCategory = length(loadCategory)
    addNewCategory = additionToCateg(loadCategory)

    currLength(lengthOfTheCategory)

main()