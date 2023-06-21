#This is a comment
print("Hello World")

## Variables that are constant ALL UPPERCASE
MY_CONSTANT = 5
## All other variables, snake case
my_variable = "Hello World"

print(MY_CONSTANT)
print(my_variable)


## Taking in User Input

# user_input = input("Who are you?")

# print(f"Hello {user_input}")

## Conditionals

num = 5 

if (num > 3):
    print("num is greater than 3")
elif (num > 1):
    print("num is greater than 1")
else:
    print("num is 1 or less")

## Looping

counter = 0

## Loop 10 times
while(counter < 10):
    if(counter % 2 == 0):
        print("It's even")
    elif (counter % 2 == 1 and counter % 3 == 0):
        print("Meow")
    else:
        print(counter)
    counter += 1
        

