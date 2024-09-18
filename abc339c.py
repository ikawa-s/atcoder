# 正解
# 時間計算量を減らす
n = int(input())
a = list(map(int,input().split()))

b = 0
for i in a:
    b += i
    if b < 0:
        b = 0

print(b)
