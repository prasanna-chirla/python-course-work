#creation
'''
class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self._post=[]
    def getpassword(self):
        return self.__password
    @property
    def accesspost(self):
        return self._post
prasanna=Instagram('prasanna','3456789')
print(prasanna.username)
print(prasanna.getpassword())
print(prasanna.accesspost)
'''
#updating
class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self._post=[]
    def getpassword(self):
        return self.__password
    def setpassword(self,newpassword):
            self.__password=newpassword
    @property
    def accesspost(self):
        return self._post
    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)
prasanna=Instagram('prasanna','3456789')
prasanna.username='prasanna_9'
print(prasanna.username)
prasanna.setpassword('234567896756453456')
print(prasanna.getpassword())
prasanna.accesspost='python'
prasanna.accesspost='java'
print(prasanna.accesspost)
