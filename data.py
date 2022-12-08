#Data Management by Adi
import json
import helper
#Load book data from JSON file
file = open("book_data.json", "r")
dataStr = file.read()
file.close()
books = json.loads(dataStr)
#Load Favourites from JSON file
file2 = open("fav.json", "r")
dataStr2 = file2.read()
file2.close()
favs = json.loads(dataStr2)

#Set Loop True
ProgramLoop = True

#Start Looping
while ProgramLoop:

  #Options To pick From
    print("OPTION 1: Display all of the data")
    print("OPTION 2: Display some of the data")
    print("OPTION 3: Sort the data")
    print("OPTION 4: Select data to add to a favourites list / shopping cart")
    print("OPTION 5: Remove data from favourites list / shopping cart")
    print("OPTION 6: Display favourites list / shopping cart")
    print("OPTION 7: Exit")

    #Input From The user
    userInput = input("Pick your Option:")

    #Option 1
    if(userInput == "1"):
        for i in range(len(books)):
            print(books[i]["title"], ",",
            books[i]["author"], "," ,
            books[i]["isbn"], "," ,
            books[i]["genre"])


    #Option 2
    elif(userInput == "2"):
        verify = 0
        userask = input("Enter the title of your book:\n")
        for i in range(len(books)):
            if userask == books[i]["title"]:
                print(books[i]["title"], ",",
                books[i]["author"], "," ,
                books[i]["isbn"], "," ,
                books[i]["genre"])
                verify = 0
            else:
                verify = 1
        if verify == 1:
            print("Book not found")


    #Option 3
    elif(userInput == "3"):
        helper.bubbleSort(books) # Sorted By Genre
        for i in range(len(books)):
                print(books[i]["title"], ",",
                books[i]["author"], "," ,
                books[i]["isbn"], "," ,
                books[i]["genre"])
            


    #Option 4
    elif(userInput == "4"):
        userin = input("What Is the name of the book you want to favouriate:\n")
        for i in range(len(books)):
            if userin == books[i]["title"]:
                favs.append(books[i])

        userin2 = input("Do you want to See your Favouraite list?\n Yes or No: \n")

        if userin2 == "yes":
            for n in range(len(favs)):
                print(favs[n]["title"], ",",
                favs[n]["author"], "," ,
                favs[n]["isbn"], "," ,
                favs[n]["genre"])


    #Option 5
    elif(userInput == "5"):
        print("PlaceHolder")


    #Option 6
    elif(userInput == "6"):
        print("PlaceHolder")


    #Option 7
    elif(userInput == "7"):
        break
    