cars = ['bmw','audi','toyota','subaru']
#sort将对列表进行永久排序（默认按照A-Z升序进行排列，需要倒序排列使用reverse=True(T一定要大写)）
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

print("\nsorted()函数临时排序，只生效一行代码")
cars = ['bmw','audi','toyota','subaru']
print(sorted(cars))
print(cars)

#反转顺序打印,reverse是将列表反转顺序，并非按照倒序方式展示（此方式会永久修改列表元素的排列顺序）
cars = ['bmw','audi','toyota','subaru']
cars.reverse()

print(cars)
