#!/usr/bin/env python3 
import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

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

    crisp_trajectory_publisher()