'''
无序
可更改
查找速度快
空间换时间
'''

# 声明
name = {
    1: 'alan',
    2: 'bob',
    3: 'lucy',
}

# 访问属性的值
print("name[1]= "+name[1])
print("name[3]= "+name[3])

# 查找：方法1
print("5 in name:")
print(5 in name)  # False

# 查找：方法2
print("name.get(5):")
print(name.get(5))  # None
print("name.get(5, 'default'):")
print(name.get(5, 'default'))  # default

# 更改：直接赋值
name[4] = 'mac'
print("names are:")
print(name)

# 删除
name.pop(1)
print("after popping, names are:")
print(name)

# 元素个数
print("len is:")
print(len(name))

# 获取所有key
print("keys are: ")
print(name.keys())

# 获取所有value
print("values are: ")
print(name.values())

# 获取所有的属性和它的值
print("items are:")
print(name.items())
