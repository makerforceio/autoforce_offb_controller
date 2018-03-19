#!/usr/bin/env python
import rospy
from autoforce_mixer.msg import NodeWeightArray
import json

results = None
def callback(data):
	results = data

def main():
	with open('ambrose.json') as data_file:
		data = json.load(data_file)
		stages = data["stages"]
		pub = rospy.Publisher('autoforce_offb_controller', NodeWeightArray, queue_size=10)
		ros.init_node('autoforce_offb_controller')
		rate = rospy.Rate(10)

		current_stage = 0
		while current_stage < len(stages):
			stage = stages[current_stage]
			sub = rospy.Subscribe(stage['node'])
			while True:
				if results = None:
					continue
				##check ifs
				rate.sleep()
			sub.shutdown()
			rate.sleep()

if __name__ == "__main__":
	main()
