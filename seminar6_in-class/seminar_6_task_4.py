def compare_function(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1


print(compare_function(int(input("First integer: ")), int(input("Second integer: "))))
