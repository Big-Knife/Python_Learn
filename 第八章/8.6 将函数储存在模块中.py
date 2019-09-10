#导入整个模块
import pizza

pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')

#导入指定函数
from pizza import make_pizza

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

#使用as给函数重命名
from pizza import make_pizza as sb

sb(16,'pepperoni')

#使用as给模块重命名
import pizza as bbc

bbc.make_pizza(16,'pepperoni')

#导入模块中的所有函数
#import语句中的星号让Python将模块pizza中的每个函数都复制到这个程序文件中。

from pizza import *

'''
编写函数时，需要牢记几个细节。应给函数指定描述性名称，
且只在其中使用小写字母和下划线。描述性名称可帮助你和别人
明白代码想要做什么。给模块命名时也应遵循上述约定。每个函数
都应包含简要地阐述其功能的注释，该注释应紧跟在函数定义后面，
并采用文档字符串格式。文档良好的函数让其他程序员只需阅读
文档字符串中的描述就能够使用它：他们完全可以相信代码如描述的
那样运行；只要知道函数的名称、需要的实参以及返回值的类型，就
能在自己的程序中使用它。
'''