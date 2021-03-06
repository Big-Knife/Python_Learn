#9-1练习
class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        '''初始化餐馆'''
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''显示餐馆摘要'''
        msg = self.restaurant_name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        '''显示一条信息，餐厅正在营业'''
        msg = self.restaurant_name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self,people):
        self.number_served = people

    def increment_number_served(self,additional_served):
        self.number_served += additional_served

restaurant = Restaurant('the mean queen', 'pizza')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(90)
restaurant.increment_number_served(10)
print(restaurant.number_served)


#9-2
class User():
    """一个表示用户的简单类。"""

    def __init__(self, first_name, last_name, username, email, location):
        """初始化用户。"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """显示用户信息摘要。"""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """它向用户发出个性化的问候。"""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print("Login attempts:" + str(eric.login_attempts))
print("Resetting login attempts...")
eric.reset_login_attempts()
print("Login attempts:" + str(eric.login_attempts))

willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()

class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name,cuisine_type='ice_cream'):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())

big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla','chocolate','black cherry']
big_one.describe_restaurant()
big_one.show_flavors()

class Admin(User):
    '''有管理权限的用户'''

    def __init__(self,fitst_name,last_name,username,
                 email,location):
        '''初始化管理员'''
        super().__init__(fitst_name,last_name,username,email,location)
        self.privileges = Privileges()

class Privileges():
    """一个存储管理员权限的类。"""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")


eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges.show_privileges()

print("\nAdding privileges...")
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()
