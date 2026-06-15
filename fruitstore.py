def main ():
    cart = []
    couponcode = []
    abcd = True
    bbbb = True
    cccc = True
    total = 0
    while True:
        print ("Fruit Store")
        print ("1.Apple - 50")
        print ("2.Grapes - 30")
        print ("3.Pineapple - 70")

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
            price = 50
            subtotal = price*qty
            cart.append(f"Apple - {price} x {qty} | {subtotal}")
            total += subtotal


        elif choice == "2":
            price = 30
            subtotal = price*qty
            cart.append(f"Grapes - {price} x {qty} | {subtotal} ")   
            total += subtotal

        elif choice == "3":
            price = 70
            subtotal = price*qty
            cart.append(f"Pineapple - {price} x {qty} | {subtotal}")
            total += subtotal

        choice2 = input("Press enter if you'll purchase more and type no if not: ")

        if choice2 == "no":
            break

    subtotal2 = total 
    vat = total*0.12


    while True:
        coupons = input("Do you have any coupon code? (yes, no) ")

        if coupons == "yes":
            code = input ("please enter your coupon code: ")

            if code == "abcd" and abcd == True:
                abcd = False               
                total *= 0.90
                couponcode.append("abcd - 10 off discount")
                print ("10 percent discount has been applied") 
                
            elif code == "bbbb" and bbbb == True:
                bbbb = False
                total *= 0.80
                couponcode.append("bbbb - 20 off discount" )
                print ("20 percent discount has been applied") 
               
            elif code == "cccc" and cccc == True:
                cccc = False
                total *= 0.80
                couponcode.append ("cccc - 20 off discount")
                print ("20 percent discount has been applied") 
                break
            else:
                print ("Invalid or expired coupon")
        else:
            break

    print ("---Receipt---")
    for i in cart:
        print(i)
    
    print (f"subtotal: {subtotal2}")
    
    print ("coupons")
    for i in couponcode:
        print(i)

    print (f"Vat (12%): {vat}")
    print (f"Total: {total + vat}")

if __name__ =="__main__":
    main()