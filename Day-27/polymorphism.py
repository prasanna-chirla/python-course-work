#method overriding-Method overriding means a child class provides its own version of a method that already exists in the parent class.
class Hotstar:
    def __init__(self,name):
        print(f"---------welcome to the hotstar,{name}--------")
    def auth(self):
        print("you can login or register")
    def dashboard(self):
        print("you can see the dashboard")
    def search(self):
        print("you can search")
    def history(self):
        print("you can see history")
    def playcontrollers(self):
        print("pause play resume")
    def ads(self):
        print("adds will be run")
    def quality(self):
        print("you have limited quality")
    def devices(self):
        print("you have single login")
    def access(self):
        print("you have limited access to content")
    def download(self):
        print("you cant download")
class Premiumhotstar():
    def __init__(self,name):
        print(f"---------welcome to the hotstar,{name}--------")
    def auth(self):
        print("you can login or register")
    def dashboard(self):
        print("you can see the dashboard")
    def search(self):
        print("you can search")
    def history(self):
        print("you can see history")
    def playcontrollers(self):
        print("pause play resume")
    def ads(self):
        print("adds will not run")
    def quality(self):
        print("you have high quality")
    def devices(self):
            print("you have multiple login")
    def access(self):
        print("you have unlimited access to content")
    def download(self):
        print("you can download")
prasanna=Hotstar('prasanna')
prasanna.auth()
prasanna.dashboard()
prasanna.search()
prasanna.history()
prasanna.playcontrollers()
prasanna.ads()
prasanna.quality()
prasanna.devices()
prasanna.access()
prasanna.download()


sai=Premiumhotstar('sai')
sai.auth()
sai.dashboard()
sai.search()
sai.history()
sai.playcontrollers()
sai.ads()
sai.quality()
sai.devices()
sai.access()
sai.download()
#operator overloading
