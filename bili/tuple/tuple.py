

tup1 = ("abc", "def", 200, 300, 333, 444, 555, 666)

print(tup1[0])
print(tup1[-1])
print(tup1[1:5])

# 1. tuple的拼接

tup2 = (111, 222)
tup3 = ("aaa", "bbb")
mergeTup = tup2+tup3
print(mergeTup)

# 2. 删
tup1 = (12, 34, 56)
print(tup1)
del tup1  # 直接释放整个内存
print("delete success")
