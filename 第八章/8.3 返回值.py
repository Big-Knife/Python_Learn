def get_formatted_name(first_name,last_name):
    '''返回整洁的姓名'''
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)

#让实参变成可选的
def get_formatted_name(first_name,middle_name,last_name):
    '''返回整洁的姓名'''
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('john','lee','hooker')
print(musician)

#有中间名时的处理方式
def get_formatted_name(first_name,last_name,middle_name=' '):
    '''返回整洁的姓名'''
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('john','hooker','lee')
print(musician)

#返回字典
def build_person(first_name,last_name,age=''):
    '''返回一个字典，其中包含有关一个人的信息'''
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi','hendrix',age=22)
print(musician)

#综合使用函数和while循环
def get_formatted_name(first_name,last_name):
    '''返回整洁的姓名'''
    full_name = first_name + ' ' + last_name
    return full_name.title()
#这是一个无限循环
while True:
    print("\n告诉我你叫什么名字")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print("你好！ " + formatted_name)