class Car():

    def __init__(self,make,modle,year):
        self.make = make
        self.modle = modle
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year) + self.make + self.modle
        return long_name.title()

