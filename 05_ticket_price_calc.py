#functions go here
def calc_ticket_price(var_age):

    #ticket is $7.50 for users under 16
    if var_age < 16:
        price = 7.50

    #ticket is $10.50 for users between 16 and 65
    elif var_age < 65:
        price = 10.50

    #ticket is $6.50 for seniors (65+)
    else:
        price = 6.50

    return price


#loop for testing
while True:

    #get age (assume users input a valid integer)
    age = int(input("Age: "))

    #calculate ticket cost
    ticket_cost = calc_ticket_price(age)
    print("Age: {}, Ticket price: ${:.2f}".format(age, ticket_cost))