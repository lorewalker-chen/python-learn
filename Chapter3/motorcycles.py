motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#修改列表元素
motorcycles[0] = 'ducati'
print(motorcycles)
#在列表末尾添加元素
motorcycles.append('ducati')
print(motorcycles)
#在列表中插入元素
motorcycles.insert(0, 'ducati')
print(motorcycles)
#从列表中删除元素,del 删除后无法再次访问
del motorcycles[0]
print(motorcycles)
#从列表中删除元素,pop()方法从列表中弹出
popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)
#从列表中删除元素，remove()根据值删除第一个出现的对应元素
motorcycles.remove('ducati')
print(motorcycles)
