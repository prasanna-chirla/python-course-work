data={
    "Rice":65,
    "Grains":50,
    "Oil":90,
    "Salt":25,
    "Cake":45,
    "Sugar":36,
    "Dal":87,
    "Eggs":200,
    "Cheese":90
}
for i in data:
    print(i.ljust(20),data[i])
prod=input("Enter the products:").split()
print("----------------Bill---------------")
bill=0
for i in prod:
    print(i.ljust(20),data[i])
    bill+=data[i]
print("Total Bill".ljust(20),bill)