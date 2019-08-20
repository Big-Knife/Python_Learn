#if-else语句 经常需要在条件测试通过时执行一个操作，并在没有通过时执行另一个操作
age= 17
if age >=18:
    print("成年人")
    print("允许通过")
else:
    print("未成年")
    print("禁止通行")

#if-elif-else 结构 需要检查超过两个条件的情况，它依次检查每个条件测试，直到通过测试后执行后面的代码。并跳过余下的测试
age=12
if age <4:
    price=0
elif age <18:
    price=5
else:
    price=10
print("你的门票价格为：" + str(price))
