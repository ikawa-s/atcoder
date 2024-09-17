# 正解
# 最初に全ての和をsetに入れることでループの回数を減らせるため

# n = int(input())
# a = list(map(int,input().split()))
# m = int(input())
# b = list(map(int,input().split()))
# l = int(input())
# c = set(map(int,input().split()))
# q = int(input())
# x = list(map(int,input().split()))

# for h in range(q):
#     y = 0
#     for i in range(n):
#         for j in range(m):
#             if x[h] - a[i] - b[j] in c:
#                 print("Yes")
#                 y = 1
#                 break
#         else:
#             continue
#         break
#     if y == 0:
#         print("No")

n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
l = int(input())
c = list(map(int,input().split()))
q = int(input())
x = list(map(int,input().split()))

y = set()
for i in a:
    for j in b:
        for k in c:
            y.add(i+j+k)

for i in x:
    if i in y:
        print("Yes")
    else:
        print("No")
