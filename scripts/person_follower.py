#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class PersonFollow:
	def __init__(self):
		rospy.init_node('person_follower', anonymous = True)
		self.vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size =10)
		self.vel_msg = Twist()
		self.vel_msg.linear.x = 0
		self.vel_msg.angular.z = 0
		self.vel_pub.publish(self.vel_msg)
		rospy.Subscriber('scan', LaserScan, self.process_scan)
	def process_scan(self,data):
		closest = float('inf')
		angle = 0
		for i in range(360):
			if data.ranges[i] < closest:
				closest = data.ranges[i]
				angle = i
		if (closest == float('inf')):
				closest = 0.5
		if (angle > 180):
			angle = angle - 360
		error_a = angle * 0.01745329
		error_d = closest - 0.5
		k_d = 0.55
		k_a = 2.3
		self.vel_msg.linear.x = k_d * error_d
		self.vel_msg.angular.z = k_a * error_a
		self.vel_pub.publish(self.vel_msg)
	def run(self):
		while not rospy.is_shutdown():
			rospy.spin()

if __name__ == "__main__":
	node = PersonFollow()
	node.run()




