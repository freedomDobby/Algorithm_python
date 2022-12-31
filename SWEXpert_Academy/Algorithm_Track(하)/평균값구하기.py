num = int(input())

for i in range(num):
    arr = list(map(int, input().split()))
    answer = sum(arr)/len(arr)
    print("#%d %d" % (i+1, round(answer)))
