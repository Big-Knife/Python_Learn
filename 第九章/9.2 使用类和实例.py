class Car():

    def __init__(self,make,modle,year):
        self.make = make
        self.modle = modle
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year) +' ' + self.make + ' ' + self.modle
        return long_name.title()

my_new_car = Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())


class Car():

    def __init__(self,make,modle,year):
        self.make = make
        self.modle = modle
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) +' ' + self.make + ' ' + self.modle
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

my_new_car = Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())
#直接修改属性的值
my_new_car.odometer_reading = 27
my_new_car.read_odometer()

#通过方法修改属性的值
my_new_car = Car('audi','a4','2016')
my_new_car.update_odometer(23)
my_new_car.read_odometer()

#通过方法递增属性
my_used_car = Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()