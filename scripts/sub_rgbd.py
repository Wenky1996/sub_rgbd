#!/usr/bin/env python2
import rospy
import cv2
import cv_bridge
import sensor_msgs.msg

from std_msgs.msg import String


def callbackImage(data):
     #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
     cv_image = cv_bridge.CvBridge().imgmsg_to_cv2(data, "bgr8")
     cv2.imshow("image rgb",cv_image)
     cv2.waitKey(3)

def callbackDepth(data):
     cv_image_depth = cv_bridge.CvBridge().imgmsg_to_cv2(data, "32FC1")
     cv2.imshow("image depth",cv_image_depth)
     cv2.waitKey(3)


def listener():
     # In ROS, nodes are uniquely named. If two nodes with the same
     # name are launched, the previous one is kicked off. The
     # anonymous=True flag means that rospy will choose a unique
     # name for our 'listener' node so that multiple listeners can
     # run simultaneously.

     rospy.init_node('listener', anonymous=True)
     print 'start node'
     rospy.loginfo("start subscribe image")
     rospy.Subscriber("/camera/color/image_raw", sensor_msgs.msg.Image, callbackImage)
     rospy.Subscriber("/camera/aligned_depth_to_color/image_raw", sensor_msgs.msg.Image, callbackDepth)

     # spin() simply keeps python from exiting until this node is stopped

     rospy.spin()


if __name__ == '__main__':
    listener()