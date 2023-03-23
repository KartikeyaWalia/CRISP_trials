#include "dynamixel_workbench_controllers/dynamixel_workbench_controllers.h"

DynamixelController::DynamixelController()
  :node_handle_(""),
   priv_node_handle_("~"),

void DynamixelController::initClient()
{
  dynamixel_command_client_ = node_handle_.serviceClient<dynamixel_workbench_msgs::DynamixelCommand>("dynamixel_command");
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "connect_serverclient");
  ros::NodeHandle node_handle("");  
  if (argc != 3)
  {
    ROS_INFO("usage: dynamixel_command id addr_name value");
    return 1;
  }

  DynamixelController dynamixel_controller;

  dynamixel_controller.initClient();


  dynamixel_workbench_msgs::DynamixelCommand srv;
  srv.request.id = atoll(argv[1]);
  srv.request.addr_name = atoll(argv[2]);
  srv.request.value = atoll(argv[3]);

  if (client.call(srv))
  {
    ROS_INFO("Did it work %ld", (long int)srv.response.comm_result);
  }
  else
  {
    ROS_ERROR("Failed to call service");
    return 1;
  }

  return 0;
}

