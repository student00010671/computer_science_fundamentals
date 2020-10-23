# From the code below


def countdown(n):
    if n <= 0:

        print('Blastoff!')

    else:

        print(n)

        countdown(n - 1)


# Write a new recursive function count-up that expects a negative argument and counts “up” from inputted number.
# Output from running the function should look something like this:

"""
count-up(-3)

-3

-2

-1

Blastoff! 
"""


# ****Solution****

# function in case user input negative integer
def count_up(n):
    if n >= 0:
        print("Blastoff!")
    else:
        print(n)
        count_up(n + 1)


# If user input is invalid try/except here block ValueError, so that user will not see how program collapse
try:
    user_number = int(input("Please type your integer: "))

except ValueError:
    print("User, come on! That is not an integer :(")

else:
    if user_number > 0:
        countdown(user_number)
    elif user_number < 0:
        count_up(user_number)
    elif user_number == 0:
        print("Nothing is to count from zero to zero: ")
