LOWER = 33

UPPER = 127





def main():

    character = (input("Enter a character: "))

    print("The ASCII code for {0} is {1}.".format(character, ord(character)))



    number = get_number(LOWER, UPPER)

    print("The character for {0} is {1}.".format(number, chr(number)))



    # print("\n")

    # for i in range(LOWER, (UPPER+1), 1):

    #    print("{0:<3}{1:>6}".format(i, chr(i)))





def get_number(lower, upper):

    valid_number = False

    while not valid_number:

        try:

            number = int(input("Enter a number between {0} and {1}: ".format(lower, upper)))

            if lower <= number <= upper:

                valid_number = True

                return number

            else:

                print("The number must be between {0} and {1}.\n".format(lower, upper))

        except ValueError:

            print("Must be a number!\n")





main()
