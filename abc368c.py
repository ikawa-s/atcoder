# 正解
n = int(input())
h = list(map(int,input().split()))

t = 0

# while h[n-1] > 0:
#     t += 1
#     # print(t)
#     if t % 3 == 0:
#         h[i] -= 3
#     else:
#         h[i] -= 1
#     # print(h)
#     if h[i] <= 0:
#         i += 1
#     # print(i)
# print(t)
b = 0
for i in range(n):
    t += (h[i] // 5) * 3
    b = h[i] % 5
    while b > 0:
        t += 1
        if t % 3 == 0:
            b -= 3
        else:
            b -= 1
print(t)
