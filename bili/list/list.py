# 1. 列表可以存储不同的数据类型
'''
testList = [1, "zhangsan"]

print(testList)

print("type(testList[0]):")
print(type(testList[0]))
print("type(testList[1]):")
print(type(testList[1]))
'''
# 2. 切片操作==string

# 3. list [遍历]

'''
testList = [1, "zhangsan"]
for i in testList:
    print(i)

for index, elem in enumerate(testList):
    print(index, elem)

'''

# 4. list [增]

# list.append(value) :末尾增加元素 (将加入的元素视为与其他元素并列)
# list.extend(container) :末尾增加list中的元素

# list.insert(index,value)

# 5. list [删除]

# del list[index]

# list.remove(value) 移除列表中和value值相等的第一个元素
# 若没有找到,则throw

# list.pop() 移除末尾元素

# 6. list [查] -- 包含关系

'''
demoList = ["A", "B", "C"]
# findName = input("你想找谁?")

# if findName in demoList:
#     print("找到了")
# else:
#     print("没找到")

'''
# list.index(value,l_bound,u_bound)
# 返回该值在上界和下界中的最小的下标
'''
demoList = ["A", "B", "C"]
print(demoList.index("B", 0, 2))
print(demoList.count("B"))
'''
# list.sort() 升序

# list.sort(reverse=True) 降序
