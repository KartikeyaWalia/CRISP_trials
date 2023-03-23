#!/usr/bin/env python3 
import rospy
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryFeedback, FollowJointTrajectoryResult, FollowJointTrajectoryGoal 
from sensor_msgs.msg import JointState

class ActionServer():

    def __init__(self):
        rospy.init_node("action_server")
        self.a_server = actionlib.SimpleActionServer("/crisp_arm/follow_joint_trajectory", FollowJointTrajectoryAction, execute_cb=self.execute_cb, auto_start= False)
        self.a_server.start()
    
    def execute_cb(self, goal):
        success = True
        # action_result= 'I tried'
        # action_feedback='I am trying' 
        # feedback = FollowJointTrajectoryFeedback
        result = FollowJointTrajectoryResult
        rate = rospy.Rate(1)
        while (True):
            if self.a_server.is_preempt_requested():
                success=False
                break 
        crisp_trajectory_data = goal.trajectory
        
        

        #     #feedback.header.joint_names= action_feedback
        #     result.error_string = action_result
        #     self.a_server.publish_feedback(feedback)
        rospy.loginfo(crisp_trajectory_data)
        if success:
            self.a_server.set_succeeded(result)
            return crisp_trajectory_data

if __name__ == '__main__':
    
    crisp_server = ActionServer()
    
    rospy.spin()