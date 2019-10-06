#使用文件的内容
file_name = 'text_files\pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

#包含一百万位的大型文件
file_name = 'text_files\pi_million_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string[:50] + "...")
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddy:")
if birthday in pi_string:
    print("Yes")
else:
    print("NO")