history = []
while True:
    name = input ("please enter your name: ")
    password = input ("Enter your password: ")

    if name == "emrhiz" and password == "1234":
        print ("Login Successfully")
        break
    else:
        print ("Invalid username or password")



initial_balance = int(input ("Enter Initial Balance (min:100): "))

# while True:
#     if passwords != passwords:
#         print ("Invalid Pin")
#         break
#     else:
#         break
while True: 
    if initial_balance < 100:
        print ("Insufficient balance")
        initial_balance = int(input ("Enter Initial Balance (min:100): ")) 

    else:
        break

while True:
    print ("\n===ATM MENU===")
    print ("1 - Check Balance")
    print ("2 - Deposit")
    print ("3 - Withdraw")
    print ("4 - Transaction History")
    print ("5 - Exit")
    

    while True:
        choice = input ("\nSelect Option: ")
        break

    if choice == "1":
        print (f"\nBalance: {initial_balance}")

    elif choice == "2":
        deposit = int(input ("\nHow much would you like to deposit? "))
        initial_balance = initial_balance + deposit
        print (f"\nCurrent Balance:{initial_balance}")
        history.append(f"deposited: {deposit}")

    elif choice == "3":
        withdraw = int(input("\nHow much would you like to withdraw? "))
        initial_balance = initial_balance - withdraw
        print (f"\nCurrent Balance: {initial_balance}")
        history.append(f"withdrawn: {withdraw}")

    elif choice == "4":
        print ("\n===TRANSACTION HISTORY===")
        for transaction in history:
            print (transaction)
        
        

    elif choice == "5":
        print ("\nThank you for using our ATM")
        break
    else:
        break