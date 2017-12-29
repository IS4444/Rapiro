import serial
ser = serial.Serial('/dev/ttyAMA0', 57600, timeout = 10)
num = 0
while num < 5:
    flag = input('Input an integer : ')
    if flag == 0:
        ser.write("#M0")#停止 青
    elif flag == 1:
        ser.write("#M1")#全身 青
    elif flag == 2:
        ser.write("#M2")#後退 青
    elif flag == 3:
        ser.write("#M7")#両手を振る 青
    else:
        print 'break'
        break
