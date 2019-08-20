requested_topping='mushrooms'
if requested_topping !='anchovies':
    print("Hold the anchovies!")

annswer=17
if annswer !=42:
    print("That is not the correct answer. Please try again!")

#使用and检查多个条件
age_1=22
age_2=18
if age_1 and age_2 >=21:
    print('是')
else:
    print('否')

#使用or检查多个条件
age_1=22
age_2=18
if age_1 or age_2 >=21:
    print('是')
else:
    print('否')

#检查特定值是否包含在列表中
requested_topping=['mushrooms','onions','pineapple']
if 'mushrooms' in requested_topping:
    print("蘑菇在里面")

#检查值不在里面
banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:
    print(user.title()+"不在里面")

