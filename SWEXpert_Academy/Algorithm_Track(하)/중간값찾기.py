N = int(input())
mid = N // 2

num = map(int, input().split())
num1 = sorted(num)

print(num1[mid])
