motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0]='ducati'
print(motorcycles)

#将元素添加至末尾
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#在指定位置插入元素
motorcycles.insert(0,'ducati')
print(motorcycles)

#使用del删除元素
del motorcycles[0]
print(motorcycles)

#使用pop()方法删除元素
motorcycles = ['honda','yamaha','suzuki']
popped_motorcycles = motorcycles.pop()
#pop实际可以删除任意位置的值，给予位置即可
print(popped_motorcycles)
print(motorcycles)

#使用remove删除元素,在不得知元素位置时=可以通过名称将其删除
motorcycles = ['honda','yamaha','suzuki','ducati']
motorcycles.remove('ducati')
print(motorcycles)