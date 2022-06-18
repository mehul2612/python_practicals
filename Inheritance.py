class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost

    def show_details(self):
        print("I am a Vehicle")
        print("The mileage of the vehicle is: ",self.mileage)
        print("The cost of the vehicle is: ",self.cost)

# v1=Vehicle(50,5000000)
# v1.show_details()

class Car(Vehicle):
    # constructor over-riding
     def __init__(self,mileage,cost,tyres,hp):
        super().__init__(mileage,cost)
        self.tyres=tyres
        self.hp=hp

     def show_car_details(self):
        print("I am a car")
        print("Number of tyres are: ",self.tyres)
        print("Value of horse power is: ",self.hp)
    

c1=Car(250,800000,4,300)
c1.show_car_details()
c1.show_details()

