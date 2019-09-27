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