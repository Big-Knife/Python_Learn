filename = 'text_files\learning_python.txt'

print("--- Reading in the entire file:")
with open(filename) as f:
    contents = f.read()
print(contents)

print("\n--- Looping over the lines:")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\n--- Storing the lines in a list:")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())

#C语言学习笔记
filename = 'text_files\learning_python.txt'

with open(filename) as f:
    lines = f.readlines()

print('\n')

for line in lines:
    #删除末尾的换行符，再将Python替换为C
    print(line.rstrip().replace('Python','C'))