# 正解
# 集合を使うことで二重ループを回避した
n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

c = a + b
c.sort()
ans1 = []
ans2 = []

# for i in range(n):
#     for j in range(n+m):
#         if a[i] == c[j]:
#             ans1.append(j+1)
#             break
# print(" ".join(map(str,ans1)))

# for i in range(m):
#     for j in range(n+m):
#         if b[i] == c[j]:
#             ans2.append(j+1)
#             break
# print(" ".join(map(str,ans2)))

d = set(a)
for i in range(n+m):
    if c[i] in d:
        ans1.append(i+1)
    else:
        ans2.append(i+1)
print(" ".join(map(str,ans1)))
print(" ".join(map(str,ans2)))
