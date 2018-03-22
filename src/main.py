#!/usr/bin/env python
import rospy
from autoforce_mixer.msg import NodeWeightArray, NodeWeight
import json
from geometry_msgs.msg import Twist

results = None
def callback(data):
	results = data

def main():
	with open('ambrose.json') as data_file:
		data = json.load(data_file)
		stages = data["stages"]
		pub = rospy.Publisher('autoforce_offb_controller', NodeWeightArray, queue_size=10)
		pub_constants = rospy.Publisher('autoforce_offb_controller_constants', Twist, queue_size=10)
		ros.init_node('autoforce_offb_controller')
		rate = rospy.Rate(10)

		current_stage = 0
		while current_stage < len(stages):
			stage = stages[current_stage]
			sub = rospy.Subscribe(stage['node'])
			out = []
			nodes = stage["then"]
			for node in nodes.keys():
				node_weight = NodeWeight()
				if node == "twist":
					node_weight.name = "/autoforce_offb_controller_constants"
				else:
					node_weight.name = "/" + node
				node_weight.weight = nodes[node]
			while True:
				if results = None:
					continue
				if stage["type"] == "boolean":
					if results == stage["value"]:
						break
				if stage["type"] == "range":
					if stage["min"] < results < stage["max"]:
						break
				rate.sleep()
			pub.publish(NodeWeightArray(out))
			if "twist" in nodes and "object" in nodes["twist"]:
				twist = Twist()
				params = node["twist"]["object"]
				twist.linear.x = params["linear"]["x"]
				twist.linear.y = params["linear"]["y"]
				twist.linear.z = params["linear"]["z"]
				twist.angular.x = params["angular"]["x"]
				twist.angular.y = params["angular"]["y"]
				twist.angular.z = params["angular"]["z"]
				pub_constants.publish(twist)
							
			sub.shutdown()
			rate.sleep()

if __name__ == "__main__":
	main()
