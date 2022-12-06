#Data Management by Adi
import json
import helper
#Load data from JSON file
file = open("book_data.json", "r")
dataStr = file.read()
file.close()

books = json.loads(dataStr)


#Set Loop True
ProgramLoop = True

#Start Looping
while ProgramLoop:

  #Options To pick From
    print("OPTION 1: Display all of the data")
    print("OPTION 2: Display some of the data")
    print("OPTION 3: Sort the data")
    print("OPTION 4: Select data to add to a favourites list / shopping cart")
    print("OPTION 5: Display favourites list / shopping cart")
    print("OPTION 6: Exit")

    #Input From The user
    userInput = input("Pick your Option:")

    #Option 1 - Display Contact Names
    if(userInput == "1"):
        for i in range(len(books)):
            print(books[i]["title"])
            print(books[i]["author"])
            print(books[i]["isbn"])
            print(books[i]["genre"])
            print(",")

    #Option 2 - Search for Contact
    elif(userInput == "2"):
        verify = 0
        userask = input("Enter the title of your book:\n")
        for i in range(len(books)):
            if userask == books[i]["title"]:
                print(books[i]["title"])
                print(books[i]["author"])
                print(books[i]["isbn"])
                print(books[i]["genre"])
                verify = 0
            else:
                verify = 1
        if verify == 1:
            print("Book not found")


    #Option 3 - Edit Contact
    elif(userInput == "3"):
        sort_data = []
        for i in range(len(books)):
            sort_data.append(books[i]["genre"])
        helper.insertionSort(sort_data)
        print(sort_data)


    #Option 4 - New Contact
    elif(userInput == "4"):
        print("PlaceHolder")


    #Option 5 - Remove Contact
    elif(userInput == "5"):
        print("PlaceHolder")


    #Option 6 - End Loop
    elif(userInput == "6"):
        break
    