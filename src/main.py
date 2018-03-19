#!/usr/bin/env python
import rospy
from autoforce_mixer.msg import NodeWeightArray

def main():
	pub = rospy.Publisher('autoforce_offb_controller', NodeWeightArray, queue_size=10)
	ros.init_node('autoforce_offb_controller')
	rate = rospy.Rate(10)

	while rospy.is_shutdown():
		#something something
		rate.sleep()

if __name__ == "__main__":
	main()
