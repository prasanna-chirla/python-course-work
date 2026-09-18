#super() is used to call the parent class’s methods or constructor from the child class.
#single inheritance
'''
class whatsappv1:
    def status(self):
        print("you can upload the status for 24hrs")
class whatsappv2(whatsappv1):
    def status(self):
        super().status()
        print("you add music and you can react")
a=whatsappv1()
a.status()
b=whatsappv2()
b.status()
'''
#multiple inheritance
class whatsappv1:
    def status(self):
        print("you can upload the status for 24hrs")
class whatsappv2:
    def status(self):
        print("you add music and you can react")
class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        
        whatsappv1.status(self)
        whatsappv2.status(self)
        print("you add to the cross platforms")
a=whatsappv3()
a.status()
