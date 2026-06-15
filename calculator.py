def main():
    num1 = int(input ("Enter your first number: "))
    num2 = int(input ("Enter your second number: "))

    operator = input ("what operator will you use?")

    if operator == "+" or operator == "plus":
        print(num1 + num2)

    elif operator == "-":
        print(num1 - num2)

    elif operator == "*":
        print(num1*num2)

    elif operator == "/":
        print(num1/num2)

    else:
        print("incorrect operator")

if __name__=="__main__":
    main()
    