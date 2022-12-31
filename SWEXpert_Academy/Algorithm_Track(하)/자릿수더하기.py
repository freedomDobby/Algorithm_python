a = input()
a = int(a)

if a < 10:
    print(a)
elif a < 100:
    print((a//10) + (a % 10))
elif a < 1000:
    print((a // 100) + ((a % 100)//10) + ((a % 100) % 10))
elif a < 10000:
    print((a//1000) + ((a % 1000) // 100) +
          ((a % 100) // 10) + ((a % 100) % 10))
