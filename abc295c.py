# 正解
# 先にsortすることで二重ループを解消した
n = int(input())
a = list(map(int,input().split()))

# b = [0 for _ in range(n)]
# ans = 0
# # print(b)
# for i in range(n-1):
#     if b[i] == 0:
#         for j in range(i+1,n):
#             if b[j] == 0 and a[i] == a[j]:
#                 b[i] = b[j] = 1
#                 ans += 1
#                 break
# print(ans)

a.sort()
ans = 0
for i in range(n-1):
    if a[i] == a[i+1]:
        ans += 1
        a[i] = a[i+1] = 0
print(ans)
