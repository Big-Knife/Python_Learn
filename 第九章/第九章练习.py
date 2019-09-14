#9-1练习
class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        '''初始化餐馆'''
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''显示餐馆摘要'''
        msg = self.restaurant_name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        '''显示一条信息，餐厅正在营业'''
        msg = self.restaurant_name + " is open. Come on in!"
        print("\n" + msg)

restaurant = Restaurant('the mean queen', 'pizza')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()