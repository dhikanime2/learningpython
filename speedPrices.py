
def caught_speeding(speed, is_birthday):



    if is_birthday.upper() == 'YES':
        s = speed - 5

    else:
        s = speed


    if s <= 60:
        print("You're score is " + str(s) + " and you get No Ticket")
    elif (s >= 61) and (s <= 80):
        print("You're score is " + str(s) + " and you get Small Ticket")
    else:
        print("You're score is " + str(s) + " and you get Big Ticket")


speed = input("Please input you're speed : " )
speed = int(speed)

is_birthday = input("""

 today is your birthday?
 Type 'yes' if yes :
 Type 'no' is no : """ )


caught_speeding(speed, is_birthday)







