num = list(input().split())
for i in range(len(num)):
    num[i] = int(num[i])

num.sort(reverse=True)
print(num[1])
