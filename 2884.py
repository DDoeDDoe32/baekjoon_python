H, M = list(map(int, input().split()))

alarm = H * 60 + M - 45

if(alarm < 0):
        alarm = 23 * 60 + 60 + alarm

alarm_H = alarm // 60
alarm_M = alarm % 60

print('%d %d' % (alarm_H, alarm_M))