#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
def wait_t_secs(t):
	dt=0
	t0 = rospy.Time.now().to_sec() # start time
	while (dt <= t) :
		t1 =  rospy.Time.now().to_sec()
		dt = t1 - t0
class square:
	def __init__(self): 
		rospy.init_node('my_drive_square', anonymous = True)
		self.velocity_publisher = rospy.Publisher("cmd_vel", Twist, queue_size=10)
	def run(self):
		vel_msg = Twist()
		vel_msg.linear.y=0
		vel_msg.linear.z = 0
		vel_msg.angular.x = 0
		vel_msg.angular.y = 0
		while not rospy.is_shutdown():
			for i in range(5) :
				vel_msg.linear.x = 0.2
				self.velocity_publisher.publish(vel_msg)
				wait_t_secs(5)
				vel_msg.linear.x = 0
				self.velocity_publisher.publish(vel_msg)
				vel_msg.angular.z = 1.5707963267948966192313216916397514420985846996875529104874722961
				self.velocity_publisher.publish(vel_msg)
				wait_t_secs(1)
				vel_msg.angular.z = 0
				self.velocity_publisher.publish(vel_msg)
			rospy.spin()
if __name__ == '__main__':
	node = square()
	node.run()
