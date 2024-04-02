#fuctions go here
#checks user doesn't leave question blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be blank, please try again")
        else:
            return response
        
#checks user enters an integer to a question
def num_check(question):
    while True:
        try:
            response = int(not_blank(question))
            return response

        except ValueError:
            print("Please enter an integer")


#main routine goes here
        
tickets_sold = 0

while True:

    name = input("garble gorf")
    
    if name == "xxx":
        break
    
    age = num_check("Please enter age: ")

    if age < 12:
        print("Sorry, you are too young for this movie")
        continue

    elif 12<= age <= 120:
        pass

    else:
        print("??That looks like a typo, Please try again")
        continue

tickets_sold +=1