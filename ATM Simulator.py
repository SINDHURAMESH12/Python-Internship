import getpass

pin = None
balance = 1000
count = 0

print(" *******************************************************************")          
print("                        WELCOME TO INDIAN BANK                      ")                        
print(" *******************************************************************")  

while (True) :   
            
    print("""  
            1. CREATE PIN
            2. DEPOSIT
            3. WITHDRAW
            4. CHECK BALANCE
        """)                                   
            
    options = int(input("Choose from above options : "))
    if options == 1:
        pin = getpass.getpass()
        print("PIN number was successfully generated!!!")

    elif options == 2:
        while count < 3:
            if pin != None:
                user_pin = getpass.getpass()
                
                if(pin == user_pin):
                    amount = int(input("Enter amount to be deposited:"))
                    if amount > 50000:
                        print("Amount should not exceed 50000")
                        continue
                    else:
                        balance += amount
                        print("Amount is deposited to your account successfully!!!")
                    break
                else:
                    count += 1
                    if count >= 3:
                        print("\nYOU HAVE ENTERED WRONG PIN 3 TIMES. THIS ATM CARD HAS BEEN BLOCKED.\nPLEASE CONTACT CUSTOMER CARE SERVICE.")
                        exit()
                    else:
                        print(f"You entered wrong PIN number.You have {3 - count} chances to Re-enter your password")
                                
            else :
                print("You must create PIN number first!!!")
                break

    elif options == 3:
        while count < 3:
            if pin != "":
                user_pin = getpass.getpass()
                if(pin == user_pin):
                    amt = int(input("Enter amount to withdraw :"))
                    if amt <= balance:
                        balance -= amt
                        print(f"Rs.{amt} was debited from your account!!!")
                        print(f"Available  Balance is {balance} ")
                        break
                    else:
                        print("You dont have sufficient balance!!!")
                        print(f"You have {balance} only")
                        continue
                else:
                    count += 1
                    if count >= 3:
                        print("\nYOU HAVE ENTERED WRONG PIN 3 TIMES. THIS ATM CARD HAS BEEN BLOCKED.\nPLEASE CONTACT CUSTOMER CARE SERVICE.")
                        exit()
                    else:
                        print(f"You entered wrong PIN number.You have {3 - count} chances to Re-enter your password")
            else :
                print("You must create PIN number first!!!")
                break
                    
    elif options == 4:
        while count < 3:
            if pin != None:
                user_pin = getpass.getpass()
                if pin == user_pin :
                    print(f"Current Balance is {balance} ")
                    break
                else:
                    count += 1
                    if count >= 3:
                        print("\nYOU HAVE ENTERED WRONG PIN 3 TIMES. THIS ATM CARD HAS BEEN BLOCKED.\nPLEASE CONTACT CUSTOMER CARE SERVICE.")
                        exit()
                    else:
                        print(f"You entered wrong PIN number.You have {3 - count} chances to Re-enter your password")
                    continue
            else :
                print("You must create PIN number first!!!")
                break

    else:
        options=int(input("Incorrect!!!Enter option from above"))

    choice = str(input("Do you want to continue(y/n):"))
    if choice == 'y' or choice == 'Y':
        continue
    else:
        exit()

