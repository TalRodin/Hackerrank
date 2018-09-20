import calendar
Y = ([int(i) for i in input().split(' ')])
c=calendar.weekday(int(Y[2]), int(Y[0]), int(Y[1]))
if c==0:
    print('MONDAY')
elif c==1:
    print('TUESDAY')
elif c==2:
    print('WEDNESDAY')
elif c==3:
    print('THURSDAY')
elif c==4:
    print('FRIDAY')
elif c==5:
    print('SATURDAY')
elif c==6:
    print('SUNDAY')
