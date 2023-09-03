def my_name(name):
    print(f"my name is {name}")
name = input("Enter your name:")   
my_name(name)

def my_meal(food, drink):
    print(f'I like to eat {food} and while drinking {drink}')
my_meal('cookies','milk')

def cube(number):
    return number **3
print(cube(3))

def by_three(number):
    if number %3 == 0:
        return cube(number)
    else:
        return "false"
print (by_three(6))