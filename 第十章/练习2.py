#访客
# 编写一个程序，提示用户输入其名字后；用户做出响应
# 后，将其名字写入到文件guest.txt中。#

filename = 'text_files\guest.txt'

name = input("what's your name?")

with open(filename,'w') as file_object:
    file_object.write(name)

#访客名单
# 编写一个while循环，提示用户输入其名字。用户输入其名字后，
# 在屏幕上打印一句问候语，并将一条到访记录添加到文件guest_book.txt中。
# 确保这个文件中的每条记录都独占一行。#

filename = 'text_files\guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = input("\n What's your name?")
    if name == 'quit':
        break
    else:
        with open(filename,'a') as file_object:
            file_object.write(name + "\n")
        print("Hi " + name + ", you've been added to the guest book.")


#编写一个while循环，询问用户为何喜欢编程。
# 每当用户输入一个原因后，
# 都将其添加到一个存储所有原因的文件中。#

filename = 'text_files\programming_poll.txt'

responses = []

while True:
    response = input("\nWhy do you like prohramming?")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond?(y/n)")
    if continue_poll != 'y':
        break

with open(filename,'a') as file_object:
    for response in responses:
        file_object.write(response + '\n')
