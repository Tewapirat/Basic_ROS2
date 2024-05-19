#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

from rclpy import qos
import random

class twistNode(Node):
    def __init__(self):
        super().__init__("twist_publisher_node")
        self.vel_pub = self.create_publisher(Twist,"cmd_vel",qos_profile= qos.qos_profile_system_default)
        self.vel_timer = self.create_timer(0.5,self.vel_timer_callback)
        self.vel_cmd = Twist()

    def vel_timer_callback(self):
        self.vel_pub.publish(self.vel_cmd)
        self.random_vel()
    
    def random_vel(self):
        linear_x = random.random()
        angular_z = random.random()

        self.vel_cmd.linear.x = linear_x
        self.vel_cmd.angular.z = angular_z
def main():
    rclpy.init()
    node_vel = twistNode()
    rclpy.spin(node_vel)
    rclpy.shutdown()
if __name__ =="__main__":
    main()
