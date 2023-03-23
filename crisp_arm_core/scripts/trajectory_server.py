#!/usr/bin/env python3 
import rospy
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryFeedback, FollowJointTrajectoryResult, FollowJointTrajectoryGoal 
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

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
        # result = FollowJointTrajectoryResult
        rate = rospy.Rate(1)
        if self.a_server.is_preempt_requested():
            success=False
            break 
                
        crisp_trajectory_data = goal.trajectory

        return crisp_trajectory_data

        #     #feedback.header.joint_names= action_feedback
        #     result.error_string = action_result
        #     self.a_server.publish_feedback(feedback)
        
        # if success:
        #     self.a_server.set_succeeded(result)

def crisp_trajectory_publisher():
    #control
    rospy.init_node('publisher_control')
    crisp_joint_trajectory_publisher = rospy.Publisher('/dynamixel_workbench/joint_trajectory', JointTrajectory, queue_size=100)

    while not rospy.is_shutdown():
        msg = JointTrajectory()

        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = 'world' #string
        msg.joint_names = ['crisp_1_j1', 'crisp_1_j2', 'crisp_1_j3', 'crisp_1_j4', 'crisp_1_j5', 'crisp_1_j6', 
        'crisp_2_j1', 'crisp_2_j2', 'crisp_2_j3', 'crisp_2_j4', 'crisp_2_j5', 'crisp_2_j6', 
        'crisp_3_j1', 'crisp_3_j2', 'crisp_3_j3', 'crisp_3_j4', 'crisp_3_j5', 'crisp_3_j6', 
        'crisp_4_j1', 'crisp_4_j2', 'crisp_4_j3', 'crisp_4_j4', 'crisp_4_j5', 'crisp_4_j6'] 
        
        point = JointTrajectoryPoint()
        point.positions = []
        point.velocities = []
        point.accelerations = []
        point.effort = []
        point.time_from_start = rospy.Duration() #in how much time??   secs

        msg.points.append( point )

        rospy.loginfo( msg ) #print 
        crisp_joint_trajectory_publisher.publish( msg )


if __name__ == '__main__':
    
    
    crisp_server = ActionServer()


    
    rospy.spin()