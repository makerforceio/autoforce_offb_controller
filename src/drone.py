#!usr/bin/env python

import rospy
from geometry_msgs import PoseStamped
from mavros_msgs.srv import CommandBool
from mavros_msgs.srv import SetMode
from mavros_msgs.msg import State

class Drone:
	""" Class that abstracts the drone control mechanisms """
	
	def state_cb(updated_state):
		self.current_state = updated_state
		pass

	def __init__(self):
		# Define state variable
		self.current_state = State()
		self.offb_set_mode = SetMode()
		self.arm_cmd = CommandBool()

		# Start node
		rospy.init_node('offb_node_python', anonymous = True)
		
		# Subscribe/Publish to relavant channels
		self.state_sub = rospy.Subscriber('mavros/state', State, state_cb, queue_size=10)
		self.local_pos_pub = rospy.Publisher('mavros/setpoint_position/local', PoseStamped, queue_size = 10)
		
		# Connect to arming client
		rospy.wait_for_service('mavros/cmd/arming')
		try:
			self.arming_client = rospy.ServiceProxy('mavros/cmd/arming', CommandBool)
		except rospy.ServiceException, e:
			rospy.logerr("Service Call failed: %s", e)

		# Connect to setmode client
		rospy.wait_for_service('mavros/setmode')
		try:
			self.set_mode_client = rospy.ServicepROXY('mavros/setmode', SetMode)
		except rospy.ServiceException, e:
			rospy.logerr("Service Call failed: %s", e)

		# Set rate for ROS
		# self.rate = rospy.Rate(20.0)

	def arm(self):
		pass

	def disarm(self):
		pass

	def setMode(self);
		pass

