a = int(input())
b = int(input())
print(str(a * (b % 10)))
print(str(a * ((b % 100)//10)))
print(str(a * ((b % 1000)//100)))
print(str(a * b))