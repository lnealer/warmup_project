#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def wait_t_secs(t):
	dt=0
	t0 = rospy.Time.now().to_sec() # start time
	while (dt <= t) :
		t1 =  rospy.Time.now().to_sec()
		dt = t1 - t0

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
		print("Dist:")
		print(forward_dist)
		print(right_dist)
		if (right_dist < 0.2 and forward_dist< 0.2):
			#stuck in corner	
			self.vel_msg.angular.z = -0.15
			self.vel_msg.linear.x =-0.15
			self.vel_pub.publish(self.vel_msg)
		elif (right_dist <0.2):
			#stuck on wall
			self.vel_msg.linear.x = 0.3
			self.vel_msg.angular.z =  0.1
			self.vel_pub.publish(self.vel_msg)
		elif (forward_dist < 0.5):
			self.vel_msg.linear.x = 0
			self.vel_pub.publish(self.vel_msg)
			self.vel_msg.angular.z = 1.0707963267948966192313216916397514420985846996875529104874722961
			self.vel_pub.publish(self.vel_msg)
		elif (forward_dist >= 0.5):
			self.vel_msg.angular.z = 0
			self.vel_msg.linear.x = 0.3
			self.vel_pub.publish(self.vel_msg)
			if (right_dist < 0.2):
				self.vel_msg.angular.z = 0.08
				self.vel_pub.publish(self.vel_msg)
			elif (right_dist > 0.47) :
				self.vel_msg.angular.z = -0.1
				self.vel_pub.publish(self.vel_msg)
			else:
				self.vel_msg.angular.z = 0
				self.vel_pub.publish(self.vel_msg)
		elif (forward_dist >= 0.5):
			self.vel_msg.angular.z = 0
			self.vel_msg.linear.x = 0.3
			self.vel_pub.publish(self.vel_msg)
				
	def run(self):
		while not rospy.is_shutdown():
			rospy.spin()


if __name__  == '__main__':
	node = WallFollow()
	node.run()

