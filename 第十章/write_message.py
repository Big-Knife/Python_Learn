filename = 'text_files\programming.txt'

with open(filename,'w') as file_object:
    file_object.write("I Love programming.\n")
    file_object.write("I Love creating new games.\n")
    #写入多行是记得添加换行符避免内容挤在一起

#附加内容
# 如果你想给文件添加内容而不是覆盖原有的内容，可以使用附加模式打开文件
# 当使用附加模式打开文件时Python不会在返回文件对象钱清空文件#

filename = 'text_files\programming.txt'

with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a beowser.\n")