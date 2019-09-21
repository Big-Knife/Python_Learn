class Car():
    '''一次模拟汽车的简单尝试'''

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odomemter_reading = 0

    def get_descripive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        print("This car has " + str(self.odomemter_reading) + " miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odomemter_reading:
            self.odomemter_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odomemter_reading += miles
