current_number=1
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