lower = 10
upper = 100
#print("Enter a number ({} - {}):".format(lower, upper))

def get_number(lower, upper):
    while True:
     try:
        number = int(input("Enter a number between 10-100:"))
        if number >= 10 and number <=100:
            print("Success")
            return number
        else:
            print("Please enter within range")
     except ValueError:
        print("<ERROR> Enter a valid number.")

user_input = get_number(lower, upper)


