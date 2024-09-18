# 一旦諦めた
n = int(input())
s = list(input())

ans = 0
print(s)
for i in n-1:
    if s[i] == s[i+1]:
        