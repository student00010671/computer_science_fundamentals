
asterisks = ["*", "* *", "* * *", "* * * *", "* * * * *"]


def my_loop():
    for i in range(4):
        print(asterisks[i])
    for reverse_asterisk in reversed(asterisks):
        print(reverse_asterisk)


my_loop()
