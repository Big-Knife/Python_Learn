def greet_user(username):
    '''显示简单的问侯句'''
    print("Hello" + username.title()+"!")
    '''变量username是一个形参——函数完成其工作所需的一项信息'''
greet_user('jesse')
'''jesse是一个实参——实参是调用函数时传递给函数的信息。
在greet_user('jesse')中,将实参'Jesse'传递给了函数greet_user()，这
个值被储存在形参username中。'''

#位置实参
def describe_pet(animal_type,pet_name):
    '''显示宠物的信息'''
    print("我有一只：" + animal_type)
    print("我的" + animal_type + "名字叫：" + pet_name)
describe_pet('老虎','小白')
#关键字实参
describe_pet(animal_type='老虎',pet_name='小白')