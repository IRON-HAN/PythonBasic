# no param

def print_hello():
    print("hello")


print_hello()

# with param


def print_str(s):
    print(s)
    return s * 2


print_str("fuck")
str2 = print_str("fuck")
print(str2)

# with default args


def print_default(s="hello"):
    print(s)


print_default()
print_default("default")

# 不定长参数


def print_args(s, *arg):
    print(s)
    for a in arg:
        print(a)
    return


print_args("hello")
print_args("hello", "world", "1")
