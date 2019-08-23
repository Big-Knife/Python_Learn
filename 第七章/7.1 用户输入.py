#函数input()工作原理
'''prompt="你好"
prompt+="\n你姓什么？"

name=input(prompt)
print("你好："+name)‘'''

#使用int()来获取数值输入
'''height=input("你多高？")
height=int(height)

if height >=140:
    print("成人票")
else:
    print("儿童票")'''

#求模运算
number=input("键入一个数字来帮你判断是奇数还是偶数")
number=int(number)

if number%2==0:
    print("偶数")
else:
    print("奇数")
'''求模运算不会指出一个数是另一个数的多少倍，而指出余数是多少。
如果一个数可被另一个数整除，余数就为0，因此求模运算符将返回0.你可利用这一点来判断一个数是奇数还是偶数'''
