alien_0={'color':'green','points':5}
#获取键的值
new_points=alien_0['points']
print("你的得分"+str(new_points))

alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

#空字典添加键值
alien_0={}
alien_0['color']='green'
alien_0['points']=5
print(alien_0)

#修改字典中的值
alien_0={'x_position':5,'y_position':25,'speed':'medium'}
print("当前x轴位置:"+str(alien_0['x_position']))
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3
alien_0['x_position']=alien_0['x_position']+x_increment
print("新的x轴坐标位置："+str(alien_0['x_position']))

#删除键值对
alien_0={'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)
#被删除的键值永远消失

favorite_languages={
    'jen':'python',
    'sarah':'c',
    'reward':'ruby',
    'phil':'python',
    }
print("Jen最喜欢的编程语言是"+favorite_languages['jen'].title())
