do:

git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git
catkin_make

to run:

>> roslaunch crisp_arm_core control_crisp_arm_core.launch  
    //dynamixel_workbench_controllers.cpp: 
        connects dynamixels and subscribes to /dynamixel_workbench/joint_trajectory topic
                                                        
    //crisp_trajectory_server.cpp:  
        subscribes to /crisp_arm/follow_arm_trajectory_action/goal
        publishes to /dynamixel_workbench/joint_trajectory topic


>> roslaunch multiple_arm_simulation bringit_up.launch 
    >crisp_arm_planning_execution.launch
        //joint_state_publisher
        >planning_context.launch ??
        >move_group.launch ??
        >initialises joint_names.yaml
        

    >start_simulation.launch
        //empty_world.launch -------- we can define our own empty_world for gazebo, currently default
        //gazebo_ros ------ connection between gazebo and ros
            spawns multiple_crisp.urdf.xacro from multiple_arm_description
                -applies ${prefix} for 4 crisp.urdf.xacro
                                            -urdf
                                            -transmission
                                            -gazebo_ros
                -creates conveyor 
                -connect the robots to world frame


    >control_utils.launch
        //control_manager ------- this loads joint_state_controller
            joint_state_controller.yaml
        //controller_manager ------ this loads joint_trajectory_controller
            trajectory_controller.yaml
        //robot_state_publisher

    >moveit_rviz.launch
        //rviz




    
    
    
    
    
    
    
    
    
    // moveit+gazebo /publishes on action server with follow trajectory action goal
