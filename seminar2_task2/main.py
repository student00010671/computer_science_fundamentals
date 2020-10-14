# Outputting 25 lines exercise

def new_line():
    print("*")


def three_lines():
    for line in range(3):
        new_line()


def nine_lines():
    for line in range(3):
        three_lines()


# 9 + 3 + 3 + 1 = 16 lines will be outputted
def clear_screen():
    nine_lines()
    three_lines(), three_lines()
    new_line()


# The last line of my program should call first nine_lines and then the clear_screen function
nine_lines(), clear_screen()
