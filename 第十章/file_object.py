with open('text_files\pi_digits.txt') as file_object:
    #使用反斜杠(\)设置路径 让程序在该目录子文件夹打开指定文件
    content = file_object.read()
    print(content.rstrip())

print('\n')

#每次一行的方式检查文件

file_name = 'text_files\pi_digits.txt'

with open(file_name) as file_object:
    for line in file_object:
        #用rstrip()删除内容空格
        print(line.rstrip() )

print('\n')

#创建一个包含文件各行内容的列表
file_name = 'text_files\pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())