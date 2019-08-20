squares=[value**2 for value in range(1,11)]
print(squares)

#切片
players=['charles','martina','michael','florence','eli']
print(players[0:3])
for player in players[3:]:
    print(player)

#列表复制
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]#使用切片复制列表，若是单纯=源表，知识进行了关联，并非创建新的副本
print(friend_foods)
friend_foods.append('icr cream')
my_foods.append('cannoli')
print(my_foods)
print(friend_foods)

#不使用切片创建副本，后添加的元素将同事出现在两个列表
friend_foods=my_foods
print(friend_foods)
friend_foods.append('icr cream')
my_foods.append('cannoli')
print(my_foods)
print(friend_foods)