#!/usr/bin/env python
import math
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def depth_callback(msg):
    """Take in an image, convert it to a computer vision image, 
    then get the value of the center pixel which should be 
    the distance from the center of the camera."""
    # type: (Image) -> None
    
    try:
        cv_image = CvBridge().imgmsg_to_cv2(msg, "passthrough")
    except CvBridgeError as e:
        print(e)

    # Get the center of the image matrix
    u = len(cv_image) / 2
    v = len(cv_image[0]) / 2

    # Output the distance in meters from the center of the camera
    rospy.loginfo("Dist: %s m", cv_image[u][v])
    
def depth_subscriber():
    # Initialize the depth sensing node
    rospy.init_node('depth_sensing', anonymous=True)

    # Initialize the subscriber to take in an image message from the specified topic
    rospy.Subscriber('/zedm/zed_node/depth/depth_registered', Image, depth_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    depth_subscriber()
