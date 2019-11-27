max_n = 0
max_idx = 0

for i in range(9):
    a = int(input())

    if (a > max_n):
        max_n = a
        max_idx = i + 1

print('%d\n%d'%(max_n, max_idx))