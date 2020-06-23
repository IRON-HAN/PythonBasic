str = "chengdu"

# random access
print("str[0]:")
print(str[0])
# 字符串切片操作
# [起始:结束:步进值]

print("str[0:5]:")
print(str[0:5])

print("str[0:5:2]:")
print(str[0:5:2])

print("str[:5]:")  # == print(str[0:5])
print(str[:5])

print("str[5:]:")
print(str[5:])

# 取消转义字符
print("hello\nchengdu")
print(r"hello\nchengdu")

# 多次打印
print((str+"\t")*3)
