from calendar import c


class Parent:
    def assign_name(self,name):
        self.name=name

    def show_name(self):
        print("Name: ",self.name)

class Child(Parent):
    def assign_age(self,age):
        self.age=age

    def show_age(self):
        print("Age: ",self.age)

class GrandChild(Child):
    def assign_gender(self,gender):
        self.gender=gender
    
    def show_gender(self):
        print("Gender: ",self.gender)

gc=GrandChild()
gc.assign_name("Mehul")
gc.assign_age(20)
gc.assign_gender("Male")
gc.show_name()
gc.show_age()
gc.show_gender()


