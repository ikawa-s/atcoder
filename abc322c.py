# 正解
# 二重ループではなく、ループを分けることで試行数を減らす
n,m = map(int,input().split())
a = list(map(int,input().split()))

# for i in range(1,n+1):
#     for j in a:
#         b = j - i
#         if b >= 0:
#             print(b)
#             break

cnt = [0] * (n+1)
ans = [0] * (n+1)
nxt = n

for i in a:
    cnt[i] = 1

for j in range(n,0,-1):
    if cnt[j] == 1:
        nxt = j
    ans[j] = nxt - j

print(*ans[1:], sep="\n")
