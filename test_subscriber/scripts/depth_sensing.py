#!/usr/bin/env python
import math
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def depth_callback(msg):
    # type: (Image) -> None
    # depths = msg.data
    
    try:
        cv_image = CvBridge().imgmsg_to_cv2(msg, "passthrough")
    except CvBridgeError as e:
        print(e)

    # (rows,cols,channels) = cv_image.shape
    # cv2.imshow("Image window", cv_image)
    # cv2.waitKey(3)
    u = len(cv_image) / 2
    v = len(cv_image[0]) / 2

    rospy.loginfo("Len: %s m", cv_image[u][v])
    # rospy.loginfo("size: %d m", msg.step * msg.height)
    
def depth_subscriber():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('depth_sensing', anonymous=True)

    rospy.Subscriber('/zedm/zed_node/depth/depth_registered', Image, depth_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    depth_subscriber()
