'''create another child class(driver) for red bus 
they need to see user info(means like which seats user booked)
and hide driver personal details
and display only driver name and phone number

class driver:
    def __init__(self,name,phonenumber,age,)
        '''
class Redbus:
    bus = {i: "Available" for i in range(1, 11)}

    def displayseats(self):
        print("----xyz bus----")

        for i in Redbus.bus:
            print(i, Redbus.bus[i])

    def booking(self, seatno):
        for i in Redbus.bus:
            if i == seatno and Redbus.bus[i] == "Available":
                Redbus.bus[i] = "Booked"
                print(f"Your seat-{seatno} is booked successfully")
                break
        else:
            print(f"Your seat-{seatno} is already booked")


class driver(Redbus):
    def __init__(self, name, email, phonenum, age, experience):
        self.name = name
        self.__email = email
        self.phonenum = phonenum
        self.__age = age
        self.__experience = experience

    def display_driver(self):
        print("----Driver Details----")
        print("Driver Name:", self.name)
        print("Phone Number:", self.phonenum)


class user(Redbus):
    def __init__(self, name, email, phonenum):
        self.name = name
        self.email = email
        self.phonenum = phonenum
prasanna = user("prasanna", "prasanna@gmail.com", 2345678)
priyanka = user("priyanka", "priyanka@gmail.com", 435678)
gayathri = user("gayathri", "gayathri@gmail.com", 456788)
d = driver("Ramesh", "ramesh@gmail.com", 9876543210, 35, 10)
prasanna.displayseats()
prasanna.booking(3)
d.display_driver()
priyanka.displayseats()
priyanka.booking(5)
gayathri.displayseats()
gayathri.booking(4)
gayathri.displayseats()
gayathri.booking(4)




