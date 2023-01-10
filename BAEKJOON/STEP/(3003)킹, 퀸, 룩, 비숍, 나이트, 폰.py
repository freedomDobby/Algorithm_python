chess = [1, 1, 2, 2, 2, 8]
subValue = list(map(int, input().split()))

answer = [chess[i] - subValue[i] for i in range(len(chess))]

# for i in range(len(answer)):
#     if answer[i] < 0:
#         answer[i] = 0

print(*answer)
