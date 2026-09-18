class Flipkart:

    discount = 30

    @classmethod
    def updatediscount(cls):
        cls.discount = 40
        print("Updated discount:", cls.discount)

    def info(self, name, phno, address):
        self.name = name
        self.phno = phno
        self.address = address
        print("Welcome to Flipkart", self.name)

    @staticmethod
    def banner():
        print(f"{Flipkart.discount}% discount is going on, grab the offer")


prasanna = Flipkart()
prasanna.info('prasanna', 3456789, 'vskp')
prasanna.updatediscount()
prasanna.banner()

samardhh = Flipkart()
samardhh.info('samardhh', 34567845, 'hyd')
samardhh.updatediscount()
samardhh.banner()

sai = Flipkart()
sai.info('sai', 2345678, 'rjy')
sai.updatediscount()
sai.banner()

