n = tmp = int(input())
cnt = 0

while True :
    a = n // 10
    b = n % 10
    res = a + b
    cnt += 1

    n = int(str(n % 10) + str(res % 10))

    if n == tmp :
        break

print(cnt)