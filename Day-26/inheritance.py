#single inheritance
'''
class whatsappv1:
    def message(self):
        print("you can send a message")
class whatsappv2(whatsappv1):
    def status(self):
        print("you can upload status for 24hrs")
prasanna=whatsappv1()
prasanna.message()
ramya=whatsappv2()
ramya.message()
ramya.status()

#multilevel inheritance
class whatsappv1:
    def message(self):
        print("you can send a message")
class whatsappv2(whatsappv1):
    def status(self):
        print("you can upload status for 24hrs")
class whatsappv3(whatsappv2):
    def groups(self):
        print("you can create group and talk")
prasanna=whatsappv1()
prasanna.message()
ramya=whatsappv2()
ramya.message()
ramya.status()
sri=whatsappv3()
sri.message()
sri.status()
sri.groups()
'''
#multiple inheritance,hybrid inheritance
class whatsappv1:
    def message(self):
        print("you can send a message")
class whatsappv2(whatsappv1):
    def status(self):
        print("you can upload status for 24hrs")
class whatsappv3:
    def groups(self):
        print("you can create group and talk")
class whatsappv4:
    def community(self):
        print("you can form community with huge no.of people")
class whatsappv5(whatsappv2,whatsappv3,whatsappv4):
    def channel(self):
        print("you can create and share updates regularly")
prasanna=whatsappv1()
prasanna.message()
sri=whatsappv3()
sri.groups()
kaveri=whatsappv5()
kaveri.message()
kaveri.status()
kaveri.groups()
kaveri.community()
kaveri.channel()
#hierarical inheritance
class whatsappv1:
    def message(self):
        print("you can send a message")
class whatsappv2(whatsappv1):
    def status(self):
        print("you can upload status for 24hrs")
class whatsappv3(whatsappv1):
    def groups(self):
        print("you can create group and talk")
class whatsappv4(whatsappv1):
    def community(self):
        print("you can form community with huge no.of people")
prasanna=whatsappv1()
prasanna.message()
ramya=whatsappv2()
ramya.message()
ramya.status()
sai=whatsappv3()
sai.message()
sai.groups()
kaveri=whatsappv4()
kaveri.message()
kaveri.community()



