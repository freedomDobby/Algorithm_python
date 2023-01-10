real_list = list(map(int, input().split()))
answer_list = []

for i in range(10):
    for r in range(10):
        max_value = real_list[i][r]
        if real_list[i][r] > real_list[i][r + 1]:
            max_value = real_list[i][r]

print(max_value)
print(i, r)
