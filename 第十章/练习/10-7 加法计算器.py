#将你为完成练习10-6而编写的代码放在一个while循环中，
# 让用户犯错（输入的是文本而不是数）后能够继续输入数。#

print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input("\nGive me a number: ")
        if x == 'q':
            break
        x = int(x)

        y = input("Give me another number: ")
        if y == 'q':
            break
        y = int(y)

    except ValueError:
        print("Sorry, I really needed a number.")

    else:
        sum = x + y
        print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")
