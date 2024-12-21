#!/usr/bin/env python3
import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
import tf_transformations

def create_pose_stamped(navigator, position_x, position_y, orientation_z):
    q_x, q_y, q_z, q_w = tf_transformations.quaternion_from_euler(0.0, 0.0, orientation_z)
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = navigator.get_clock().now().to_msg()
    pose.pose.position.x = position_x
    pose.pose.position.y = position_y
    pose.pose.position.z = 0.0
    pose.pose.orientation.x = q_x
    pose.pose.orientation.y = q_y
    pose.pose.orientation.z = q_z
    pose.pose.orientation.w = q_w
    return pose

def main():
    # init
    rclpy.init()
    nav = BasicNavigator()
    # set initial pose
    initial_pose = create_pose_stamped(nav, 0.0, 0.0, 0.0)
    # q_x, q_y, q_z, q_w = tf_transformations.quaternion_from_euler(0.0, 0.0, 0.0)
    # initial_pose = PoseStamped()
    # initial_pose.header.frame_id = 'map'
    # initial_pose.header.stamp = nav.get_clock().now().to_msg()
    # initial_pose.pose.position.x = 0.0
    # initial_pose.pose.position.y = 0.0
    # initial_pose.pose.position.z = 0.0
    # initial_pose.pose.orientation.x = q_x
    # initial_pose.pose.orientation.y = q_y
    # initial_pose.pose.orientation.z = q_z
    # initial_pose.pose.orientation.w = q_w

    nav.setInitialPose(initial_pose=initial_pose)
    nav.waitUntilNav2Active()

    # set goal pose
    goal_pose_1 = create_pose_stamped(nav, 3.5, 1.0, 1.57)
    goal_pose_2 = create_pose_stamped(nav, 2.0, 2.5, 3.14)
    goal_pose_3 = create_pose_stamped(nav, 0.5, 1.0, -1.57)
    # q_x, q_y, q_z, q_w = tf_transformations.quaternion_from_euler(0.0, 0.0, 1.57)
    # goal_pose = PoseStamped()
    # goal_pose.header.frame_id = 'map'
    # goal_pose.header.stamp = nav.get_clock().now().to_msg()
    # goal_pose.pose.position.x = 1.5
    # goal_pose.pose.position.y = 1.0
    # goal_pose.pose.position.z = 0.0
    # goal_pose.pose.orientation.x = q_x
    # goal_pose.pose.orientation.y = q_y
    # goal_pose.pose.orientation.z = q_z
    # goal_pose.pose.orientation.w = q_w
    # nav.goToPose(goal_pose)

    waypoints = [goal_pose_1, goal_pose_2, goal_pose_3]
    nav.followWaypoints(waypoints)
    while not nav.isTaskComplete():
        feedback = nav.getFeedback()
        # print(feedback)
    
    print(nav.getResult())
    # shutdown
    rclpy.shutdown()



if __name__ == '__main__':
    main()