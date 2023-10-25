# Suppose you must determine whether a given number between 3 and 100.
# Inclusive, is a prime. Recall that an integer N>= 2 is prime if its only factors
# are 1 and itself. so 17 and 23 are prime where 33 is not, because it is the product of 3 and 11. Assume that you must
# solve this problem without benefit of a computer or pocket calculator. Your first attempt at a solution, using the
# generate-and-test approach, might look like the following pseudocode


# {While the problem is not yet solved and more
#       possible factors for Number

# remain:
#       [Generate a possible factor for Number
#         possible factors will be generated in the
#           order 2,3,4,5,...,
# Number
#       Test: If (Number)/(Possible Factor) is and integer >=2
#       Then return not prime]
# End while
# If possible factor equals Number,
# Then return Number is prime


def main():
    Number = 0  # Getting Input from user and check if it is between 3-100
    while Number < 3 or Number > 100 or Number.is_integer() is False:
        Number = float(input("Input a number between 3 and 100 to test if its prime: "))
        if Number < 3 or Number > 100 or Number.is_integer() is False:
            print("Error invalid input. Please try again.")

    counter = 2  # Using a counter to divide
    Flag = True  # this is for later to print if it is prime

    while counter < Number:
        aux = Number / counter
        if aux.is_integer() is True:
            print("The number inputted is not prime. The factors found are: ", counter, " and ", int(aux))
            Flag = False
            break
        else:
            counter += 1
            aux == 0

    if Flag is True:
        print("The number inputted is prime")


if __name__ == "__main__":
    main()
