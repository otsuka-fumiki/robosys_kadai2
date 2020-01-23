#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def cb(message):
    rospy.loginfo(message.data*2)

if __name__ == '__main__':
    rospy.init_node('multi')
    sub = rospy.Subscriber('count_up2', Int32, cb)
    rospy.spin()
