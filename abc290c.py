# 正解
# Listを使わずに集合を使うことでループを1つ削除
n,k = map(int,input().split())
a = set(map(int,input().split()))

for i in range(k):
    if i not in a:
        print(i)
        break
else:
    print(k)
