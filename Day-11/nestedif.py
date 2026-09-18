#instagram
'''fa=eval(input("follows account: "))
if fa:
    cf=eval(input("close friend: "))
    if cf:
        print("story visible")
    else:
        print("not in close friends")
else:
    print("follow the account first")'''

#bgmi tournament entry
'''reg=eval(input("registered: "))
if reg:
    fee=eval(input("fee paid: "))
    if fee:
        print("tournament entry confirmed")
    else:
        print("entry fee pending")
else:
    print("registration required")'''

#google drive file access
'''link=eval(input("link active: "))
if link:
    per=eval(input("permission granted"))
    if per:
        print("file opened successfully")
    else:
        print("access denird")
else:
    print("invalid link")'''

#all combined example program
'''data={
    'prasanna':{'status':True,'python':90,'mysql':89,'flask':95},
    'sushma':{'status':False,'python':None,'mysql':None,'flask':None},
    'siri':{'status':True,'python':88,'mysql':94,'flask':90},
    'saranya':{'status':True,'python':56,'mysql':67,'flask':89},
    'likhitha':{'status':True,'python':78,'mysql':89,'flask':90}
}
name=input("enter name")
if name in data:
    if data[name]['status']:
        sum=data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg=sum/3
        if avg>=90:
            print("outstanding")
        elif avg>=70:
            print("very good")
        elif avg>=35:
            print("good")
        else:
            print("fail,try hard")
    else:
        print(f'{name} missed exam ,bring parents')
else:
    print(f'{name} not found')'''