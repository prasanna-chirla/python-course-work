#assert is used to raise assertion errors with custom messages 
email=""
password=""

amount=-2000
assert amount>0, "amount needs to be +ve"
assert email!="" and password!="","userneeds to enter email and password"