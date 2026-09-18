import logic as lg
if lg.login():
    while True:
        lg.menu()
        ch=input("enter the choice: ").upper()
        if ch=='c':
            lg.checkbalance()
        elif ch=='d':
            lg.deposite()
        elif ch=='w':
            lg.withdraw()
        elif ch=='v':
            lg.viewtransaction()
        elif ch=='e':
            print("----thankyou,visit again----")
            break
        else:
            print("enter the valid choice")