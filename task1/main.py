# 00010671 Seminar 2 Task 1

# Example 1

# In the function below, name inside the parenthesis is a parameter
def simple_function(name, age):
    print("Hello " + name + "! Did you know that  print() itself is also a function?")
    print("You are " + str(age) + ". That's so cool. You have so much to do in your future! \n")


# Users input that will be passed to parameter is an argument
# input("What is your name? ") => is an argument
simple_function(input("What is your name? "), input("How old are you? "))


# Example 2

# Value
simple_function("John", 78)

# Variable
user_name = "Andrew"
user_age = 93
simple_function(user_name, user_age)

# Statement
if user_name == "Andrew" and user_age == 93:
    print("Thank you Mr.Andrew! Your age is impressive, I wish you to meet your grand grand grand children. \n")


# Example 3

# Variable student_id inside the scope and can be accessed only within the function below
def function_with_local_variable():
    student_id = "00010671"
    print("My ID is " + student_id)


function_with_local_variable()

# print function below will cause an error "unresolved reference 'student_id', as it is not defined in the global scope"
# print(student_id)


# Example 4

def function_with_unique_parameter(car):
    print("Majority of boys dream car is " + car)


function_with_unique_parameter("Lamborghini")

# line 54 causes an error since car is not defined in the global scope
# print(car + " is a luxurious car")


# Example 5

# No matter in what order variable was (re)defined, the final value will always be the value of variable
# in the global scope
# Shadows name warning occurring, however, the code works fine

def last_exercise_a():
    speed_limit = 70
    print("Speed limit in Tashkent is " + str(speed_limit))


last_exercise_a()

speed_limit = 90
print("Speed limit in Spain is " + str(speed_limit))
print(speed_limit)  # prints 90

# When I firstly pass value to a global variable

milk_price = 8000
print("The price of the 1% milk in Korzinka is " + str(milk_price))


def last_exercise_b():
    milk_price = 8200
    print("The price of the 1% milk in Havas is " + str(milk_price))


last_exercise_b()
print(milk_price)  # prints 8000
