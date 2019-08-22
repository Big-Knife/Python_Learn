#函数input()工作原理
message=input("你叫什么名字？")
print("你好："+message+"!")

prompt="你好"
prompt+="\n你姓什么？"

name=input(prompt)
print(name)