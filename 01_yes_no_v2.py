#fuction goes here
def yes_no (question):
    pass
# main code goes here
    
while True:
    want_instructions = input("Do you want to read the instructions? ").lower()

    if want_instructions == "yes" or want_instructions == "y":
        print("Instructions go here")
    elif want_instructions == "no" or want_instructions == "n":
        pass
    else:
        print("Please answer yes/no")

print("We are done")
