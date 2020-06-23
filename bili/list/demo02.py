products = [["iphone", 6888], ["mac", 14800],
            ["小米", 2000], ["coffee", 30], ["book", 60]]

print("-"*5+"商品列表"+"-"*5)

i = 0
for product in products:
    print("%d\t%s\t%d" % (i, product[0], product[1]))
    i += 1


indexs = []
while True:
    ans = input("想要啥?(q to quit)\n")
    if ans == "q":
        break
    else:
        indexs.append(int(ans))

print("您的购物车:")
for index in indexs:
    print("%d\t%s\t%d"
          % (index, products[index][0], products[index][1]))
