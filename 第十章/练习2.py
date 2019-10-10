#访客
# 编写一个程序，提示用户输入其名字后；用户做出响应
# 后，将其名字写入到文件guest.txt中。#

filename = 'text_files\guest.txt'

name = input("what's your name?")

with open(filename,'w') as file_object:
    file_object.write(name)

filename = 'text_files\guest_book.txt'

print("Enter 'quit' when you are finished.")
while Ture:
    name = input("\n What's your name?")
    if name == 'quit'
        break
    else::
    with open(filename,)