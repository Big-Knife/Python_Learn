#首先，创建一个待验证用户列表
    #   和一个用于储存已验证用户的空列表

unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
    #验证每个用户，知道没有未验证用户为止
    #   将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

    #   显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#删除包含特定值的所有列表元素
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

#使用用户输入来填充字典
responses = {}
#设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
    #提示输入被调查者的名字和回答
    name = input("\n你叫什么名字？")
    response = input("有时间你想爬哪座山？")
    #将答卷储存在字典中
    responses[name] = response
    #看看是否还有人要参于调查
    repeat = input("你参加了问卷调查了吗(yes/no)")
    if repeat == 'yes':
        polling_active = False
#调查结束，显示结果
print(responses)
print("\n调查结果")
for name,response in responses.items():
    print("姓名：" + name + "\n想爬的山：" + response)