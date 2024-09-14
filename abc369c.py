# 時短方法不明
n = int(input())
a = list(map(int,input().split()))

count1 = 0
count2 = 0

for l in range(n-1) :
    for r in range(l+1,n) :
        for i in range(l,r) :
            if a[i+1]-a[i] != a[l+1]-a[l] :
                count1 = 0
                break
            else :
                count1 += 1
            
        count2 += count1 // (r-l)
        count1 = 0

count2 += n
print(count2)
