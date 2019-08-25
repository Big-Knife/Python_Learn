#根据不同年龄收取不通过票价
message=("请问你的年龄是？")

while True:
    age=input(message)
    age = int(age)
    if age == 'quit':
        break
    if age<3:
        print("免费")
    elif age<=12:
        print("10美元")
    else:
        print("15美元")
