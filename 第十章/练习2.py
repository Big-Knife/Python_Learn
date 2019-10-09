filename = 'text_files\guest.txt'

name = input("what's your name?")

with open(filename,'w') as file_object:
    file_object.write(name)
