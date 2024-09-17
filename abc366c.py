# 正解
# 長さが不変の配列にしたため。　
# 要素数のカウントでsetの使用をやめたため。
q = int(input())
# Q = []
# for _ in range(q):
#     result = input().split()
#     if result[0] == "1":
#         Q.append(result[1])
#     elif result[0] == "2":
#         Q.remove(result[1])
#     else:
#         print(len(set(Q)))

count = [0] * 1000000
answer = 0

for _ in range(q):
    result = list(map(int,input().split()))
    # print(result)
    if result[0] == 1:
        result[1] -= 1
        count[result[1]] += 1
        if count[result[1]] == 1:
            answer += 1
    elif result[0]  == 2:
        result[1] -= 1
        count[result[1]] -= 1
        if count[result[1]] == 0:
            answer -= 1
    else:
        print(answer)
        