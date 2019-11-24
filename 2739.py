a = int(input())

if a < 1 or a > 10 :
    pass

else :
    for i in range(1, 10) :
        print(str(a) + ' * ' + str(i) + ' = ' + str(a*i))
