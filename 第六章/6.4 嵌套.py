alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}

aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

#用代码生成外星人
aliens=[]
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

#显示创建了多少个外星人
print(str(len(aliens)))

#创建一群不同参数的外星人
aliens=[]
for number in range(10):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:10]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['points']=10
        alien['speed']='medium'
    elif  alien['color']=='yellow':
        alien['color']='red'
        alien['speed']='fast'
        alien['points']=15
for alien in aliens[:5]:
    print(alien)

#在字典中储存列表
pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
    }
print("披萨的厚度:"+pizza['crust'].title())
for topping in pizza['toppings']:
    print("披萨配料："+topping.title())