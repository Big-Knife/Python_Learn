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

class ElectricCar(Car):
    '''电动汽车的独特之处'''

    def __init__(self,make,model,year):
        '''初始化父类的属性'''
        super().__init__(make,model,year)
        self.battery_size = 70

    def describe_battery(self):
        '''描述电池容量的信息'''
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank():
        '''ElectricCar Not Fill'''
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descripive_name())
my_tesla.describe_battery()