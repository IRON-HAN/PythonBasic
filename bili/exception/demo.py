import time

# 1. 捕获异常
'''
try:
    print("---test1---")

    f = open("123.txt", "r")

    print("---test2---")
except IOError:
    print("IOerror!")
'''
# 2.捕获多个异常
'''
try:
    print("---test1---")

    f = open("123.txt", "r")

    print("---test2---")

    print(num)

    print("---test3---")
except (NameError, IOError) as result:
    print("error is : ")
    print(result)
'''
# 3. 捕获所有异常
'''
try:
    print("---test1---")

    f = open("123.txt", "r")

    print("---test2---")

    print(num)

    print("---test3---")
except Exception as result:
    print("error is : ")
    print(result)
'''

# 4. try的嵌套和finally

# try 内部是局部变量
try:
    f = open("e:/VSC_PY/bili/file/test.txt", "r")

    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(1)
            print(content)
    finally:
        f.close()
        print("file closed")
except Exception as result:
    print("error is:")
    print(result)
