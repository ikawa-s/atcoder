# 正解
# 集合を使うことで二重ループを避けた（集合にタプルも渡せる）
import sys
n = int(input())
s = list(input())

x = y = 0
a = {(0,0)}
for i in s:
    if i == "R":
        x += 1
    elif i == "L":
        x -= 1
    elif i == "U":
        y += 1
    else:
        y -= 1

    if (x,y) in a:
        # print(x,y)
        print("Yes")
        sys.exit()
    else:
        a.add((x,y))
        # print(a)
print("No")
