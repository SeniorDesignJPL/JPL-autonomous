#!/usr/bin/env python
import rospy
import ros_numpy
import numpy as np
from sensor_msgs.msg import Image
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2

def depth_callback(msg):
    """Take in an image, convert it to a computer vision image, 
    then get the value of the center pixel which should be 
    the distance from the center of the camera."""
    # type: (Image) -> None

    depth = ros_numpy.image.image_to_numpy(msg)

    # Get the center of the image matrix
    u = len(depth) / 2
    v = len(depth[0]) / 2

    # Output the distance in meters from the center of the camera
    rospy.loginfo("Dist: %s m", depth[u][v])

def map_callback(msg):
    """Take in an image, convert it to a computer vision image, 
    then get the value of the center pixel which should be 
    the distance from the center of the camera."""
    # type: (PointCloud2) -> None
    
    points = sensor_msgs.point_cloud2.read_points(msg)
    point_list = []
    for point in points:
        point_list.append(point)

    np_point_list = np.array(point_list)

    # Get the center of the image matrix
    u = len(np_point_list) / 2

    # Output the distance in meters from the center of the camera
    rospy.loginfo("Dist: %s m", np_point_list[u])
    
def depth_subscriber():
    # Initialize the depth sensing node
    rospy.init_node('depth_sensing', anonymous=True)

    # Initialize the subscriber to take in an image message from the specified topic
    # rospy.Subscriber('/zedm/zed_node/depth/depth_registered', Image, depth_callback)
    rospy.Subscriber('/zedm/zed_node/mapping/fused_cloud', PointCloud2, map_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    depth_subscriber()
