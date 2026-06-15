# # print ("hello")

# name = "emrhiz"
# # print( "Hello" , name)

# # print (f"hello {name})\

# age = 22
# grade = 90.8
# is_student = True
# print (f"{name} {age} {grade} {is_student}")
# # name = input ("what is your name?")
# # print (f"Hi, {name}")\

# num1 = int(input ("Enter your first number: "))
# num2 = int(input ("Enter your second number: "))

# # print (num1 + num2)
# # print (num1 - num2)
# # print (num1 * num2)
# # print (num1 / num2)

# money = 5

# if money > 30:
#     print ("hi")

# elif money > 10:
#     print ("average")

# else:
#     print ("poor")

# def main():
#     print("hello")

# if __name__=="__main__":
#     main()

# for i in range(6):
#     print("*" * i)
    
# i = 1
# while i < 6:
#     print("*" * i)
#     i += 1

# i = 5
# while i > 0:
#     print ("*" * i)
#     i -= 1

# colors = ["Blue", "Green", "Red"]
# colors.append ("Violet")
# colors.remove("Green")
# for i in colors:
#     print(i)

cart = []
total = 0
while True:
    print ("Fruit Store")
    print ("1.Apple - 50")
    print ("2.Grapes - 30")
    print ("Pineapple - 70")

    while True:
        choice = input("what do you want to buy? ")

        if choice == "":
            print ("choice must not be empty")
        
        else:
            break
    while True:
        qty = int(input ("how many items would you like to purchase? "))

        if qty < 1:
            print ("invalid quantity")
        
        else:
            break
    price = 0

    if choice == "1":
        cart.append(f"Apple - 50 x {qty}")
        price = 50
        total += price * qty

    elif choice == "2":
        cart.append(f"Grapes - 30 x {qty}")
        price = 30
        total += price * qty

    elif choice == "3":
        cart.append(f"Pineapple - 70 x {qty}")
        price = 70
        total +=price * qty

    choice2 = input("Press enter if you'll purchase more and type no if not: ")

    if choice2 == "no":
        break
print ("---Receipt---")
for i in cart:
    print(i)

print (f"Total:{total}")