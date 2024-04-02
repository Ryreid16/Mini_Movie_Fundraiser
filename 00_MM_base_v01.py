# Functions go here

# Checks user has entered yes/no to a question
def yes_no (question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        
        elif response == "no" or response == "n":
            return "no"
        
        else:
            print("Please enter yes or no")
        break

#checks that user response is not blank
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


#main routine starts here

# set maximum number of tickets below
MAX_TICKETS = 3
tickets_sold = 0
# ask user if they want to see the instructions
want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    print("Instructions go here")


#loop to sell tickets
    
while tickets_sold < MAX_TICKETS:
    name = not_blank("Enter your name(or xxx to quit) ")
    
    if name == 'xxx':
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

    tickets_sold += 1

# output number of tickets sold

if tickets_sold == MAX_TICKETS:
    print("Congradulations, you have sold all the tickets")

else:
    print("You have sold {} ticket/s. There is {} ticket/s " "remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))
