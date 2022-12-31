num = int(input())

for i in range(num):
    list = map(int, input().split())
    answer = max(list)
    print("#%d %d" % (i+1, answer))
