# 正解
# 二重ループを回避するために、予め要素数だけ0を持つ配列を作成する。

n = int(input())
a = list(map(int,input().split()))

# result = []
# for i in range(1,n+1):
#     b = 0
#     for j in range(len(a)):
#         if a[j] == i:
#             b += 1
#             if b == 2:
#                 result.append(j+1)
# ans = [i + 1 for i, _ in sorted(enumerate(result), key=lambda x: x[1])]
# print(" ".join(map(str,ans)))

b = [0 for _ in range(n+1)]
ans = []
for i in a:
    b[i] += 1
    if b[i] == 2:
        ans.append(i)
print(" ".join(map(str,ans)))
