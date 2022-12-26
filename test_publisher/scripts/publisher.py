#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def publisher():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(0.25) # 1hz
    count = 0
    while not rospy.is_shutdown():
        count += 1
        hello_str = 'hello world %s' % count
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
