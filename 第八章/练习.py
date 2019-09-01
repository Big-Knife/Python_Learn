#编写一个名为make_shirt()的函数，它接受一个尺码以及要印到T恤上的字样。这个函数应打印一个句子，概要地说明T恤衫的尺码和字样。
#使用位置实参调用这个函数来制作一件T恤；再使用关键字实参来调用这个函数。

def make_shirt(size, message):
    """指出要制作的T恤什么样。"""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt('large', 'I love Python!')
make_shirt(message="Readability counts.", size='medium')

'''修改函数make_shirt()，使其在默认情况下制作一件印有字样I love Python的大号T恤。
调用这个函数来制作如下T恤：一件印有默认字样的大号T恤、一件印有默认字样的中号T恤、
一件印有其他字样的T恤（尺码无关紧要）。'''

def make_shirt(size='large', message='I love Python!'):
    """指出要制作的T恤什么样。"""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')

'''编写一个名为describe_city()的函数，它接受一座城市的名字以及该城市所属的国家。
这个函数应打印一个简单的句子，如Reykjavik is in Iceland。给用于存储国家的形参指定默认值。
为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。'''

def describe_city(city, country='chile'):
    """描绘城市。"""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('santiago')
describe_city('reykjavik', 'iceland')
describe_city('punta arenas')
