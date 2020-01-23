#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

rospy.init_node('twice')
pub = rospy.Publisher('count_up2', Int32, queue_size=1)
rate = rospy.Rate(10)
n = 0

def cb(message):
    # rospy.loginfo(message.date*2)
    pub.publish(message.data*2)

if __name__ == '__main__':
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int32, cb)
    rospy.spin()

