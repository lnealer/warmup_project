#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class WallFollow:
	def __init__(self):
		rospy.init_node('wall_follower', anonymous =True)
		self.vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
		self.vel_msg = Twist()
		self.vel_msg.linear.x = 0
		self.vel_msg.angular.z = 0
		self.vel_pub.publish(self.vel_msg)
		rospy.Subscriber('scan', LaserScan, self.process_scan)
	def process_scan(self,data):
		forward_dist = data.ranges[0]
		right_dist = data.ranges[270]
		if (forward_dist<0.2):
			self.vel_msg.linear.x = -0.3
			self.vel_pub.publish(self.vel_msg)
		elif (forward_dist <= 0.9):
			self.vel_pub.publish(self.vel_msg)
			self.vel_msg.angular.z = 1.5707963267948966192313216916397514420985846996875529104874722961
			self.vel_pub.publish(self.vel_msg)
		elif (forward_dist > 0.9):
			self.vel_msg.linear.x = 0.4
			self.vel_pub.publish(self.vel_msg)
			k = 0.1
			error = 0.5 - right_dist
			self.vel_msg.angular.z = k * error
	def run(self):
		while not rospy.is_shutdown():
			rospy.spin()


if __name__  == '__main__':
	node = WallFollow()
	node.run()

