
# 1. dict 访问
# 已知存在的key
'''
info = {"name": "A", "age": 10}
print(info["name"])
print(info["age"])
'''
# 访问不存在的key

# print(info["gender"])
# 直接访问 抛出异常

# dict.get(key,default_val=None)
# 使用get方法,如果没有找到对应的key,则默认返回None

'''
info = {"name": "A", "age": 10}
print(info.get("gender"))  # 使用默认的None
print(info.get("gender", "male"))  # 使用自己的默认值

print(info.get("age", 20))  # result: 10
'''

# 2. dict [增]

'''
info = {"name": "A", "age": 10}
newID = input("请输入学号:")
info["ID"] = newID
print('info["ID"]:')
print(info["ID"])
'''

# 3. dict [删]

# del dict[key]

'''
info = {"name": "A", "age": 10}
print("before: %s" % info["name"])

del info["name"]  # 删除key+value

print("delete success")
print(info.get("name"))  # None

del info # 释放info的内存
'''

# dict.clear()

'''
info = {"name": "A", "age": 10}
print(info)
info.clear()
print(info)
'''

# 4. dict [改] == dict 访问

# 5. dict [遍历]

'''
info = {"name": "A", "age": 10}
print(info.keys())
print(info.values())
print(info.items())

keys = info.keys()
print(type(keys))  # <class 'dict_keys'> 类似于 list
for key in keys:
    print(key)

for key, value in info.items():
    print("key=%s,value=%s" % (key, value))
'''

