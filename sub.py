#!/usr/bin/env python

import rospy
import serial
from std_msgs.msg import Int32

#ser = serial.Serial('/dev/ttyAMA0', 57600, timeout = 10)

def cb(message):
    #rospy.loginfo(message.data*2)
    ser = serial.Serial('/dev/ttyAMA0', 57600, timeout = 10)
    if message.data == 1:
        ser.write("#M1")
    elif message.data == 2:
        ser.write("#M2")
    elif message.data == 3:
        ser.write("#M7")
    else:
        ser.write("#M0")

if __name__ == '__main__':
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int32, cb)
    rospy.spin()
