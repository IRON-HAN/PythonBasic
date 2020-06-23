# 多个返回值
'''
def divid(a, b):
    shang = a//b
    yushu = a % b
    return shang, yushu


sh, yu = divid(5, 2)

print("商: %d, 余数: %d" % (sh, yu))

'''

# global local
'''
a = 100


def test1():
    a = 300
    print("test1::a is %d" % a)


def test2():
    print("a = %d" % a)


def test3():
    global a
    print("before modified: %d" % a)
    a = 200
    print("after modified: %d" % a)


def test4():
    print("a = %d" % a)


test1()
test2()
test3()
test4()
'''
