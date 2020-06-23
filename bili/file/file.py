# 1. 写文件: file.write

'''
f = open("e:/VSC_PY/bili/file/test.txt", "w")
f.write("hello world")
f.close()
'''
# II. 读文件
# 1. file.read(cnt) 文件指针
# 2. file.read()根据当前指针位置把文件读完
'''
f = open("e:/VSC_PY/bili/file/test.txt", "r")
content = f.read(5)
print(content)
print("-"*30)
content = f.read()
print(content)
f.close()
'''
# 2. file.readlines()
'''
f = open("e:/VSC_PY/bili/file/test.txt", "r")

content = f.readlines()

print(type(content))  # <class 'list'>

i = 1
for elem in content:
    print("%d:%s" % (i, elem))
    i += 1

f.close()
'''
# III. file.readline()
'''
f = open("e:/VSC_PY/bili/file/test.txt", "r")

content = f.readline()
print("1:%s" % content, end="")

content = f.readline()
print("2:%s" % content)

f.close()
'''
