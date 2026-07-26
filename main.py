#create class
class Vehicle:

    #create init method
    def __init__(self, maximum_speed, mileage):

        #bind the arguments
        self.maximum_speed = maximum_speed
        self.mileage = mileage

#Object creation
modelx = Vehicle(240, 18)

print("Model Max Speed:", modelx.maximum_speed)
print("Model Mileage:", modelx.mileage)