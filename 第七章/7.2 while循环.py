'''current_number=1
while current_number<=3:
    print(current_number)
    current_number+=1

prompt='当你想要退出时告诉我'
prompt='键入[quit]结束程序'

message=''
while message !='quit':
    message=input(prompt)
    if message !='quit':
        print(message)
'''

'''
#使用标志变量让程序判断程序是否继续运行
prompt="当你想要退出时告诉我"
prompt="键入[quit]结束程序"
active=True

while active:
    message=input(prompt)
    if message =='quit':
        active=False
    else:
        print(message)
'''
'''
#使用brake退出循环
prompt="你去过哪些城市"
prompt+="\n键入[quit]结束程序"

while True:
    city=input(prompt)
    if city == 'quit':
        break
    else:
        print("这个地方我去过呢\n")
'''

#在循环中使用continue
current = 0
while current <10:
    current +=1
    if current%2==0:
        continue
    print(current)

#要避免写出无限循环，务必对每个while循环进行测试，确保它按照预期那样结束。如果你希望程序在用户输入特定值时结束，
#可运行程序并输入这样的值测试；如果在这种情况程序没有结束，请检查程序处理这个值的方式，确认程序至少有一个这样的
#地方能让循环条件为False或让break语句得以执行。
