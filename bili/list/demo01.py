import random

offices = [[], [], []]

names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

for name in names:
    index = random.randint(0, 2)  # 闭区间!!!
    offices[index].append(name)

i = 1
for office in offices:
    print("办公室%d的人数为: %d" % (i, len(office)))
    i += 1
    for name in office:
        print("%s" % name)
    print("\n")
    print("-"*20)
