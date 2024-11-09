#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def rectangular_movement():
    # Initialize the publisher
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('tsim_rectmove_driver', anonymous=True)
    rate = rospy.Rate(1)  # 1 Hz

    # Initialize variables
    del_t = 0
    direction = 0
    sides_completed = 0  # Counter for completed sides
    
    # Define rectangle dimensions (different speeds for length and width)
    length_speed = 2.0  # Longer side
    width_speed = 1.0   # Shorter side

    while not rospy.is_shutdown() and sides_completed < 4:  # Stop after 4 sides
        robo_vel = Twist()
        
        if del_t % 20:  # Change direction every 20 iterations
            if direction == 0:  # Move along length
                robo_vel.linear.x = length_speed
                robo_vel.linear.y = 0
                direction = 1
                sides_completed += 1
            elif direction == 1:  # Move along width
                robo_vel.linear.x = 0
                robo_vel.linear.y = width_speed
                direction = 2
                sides_completed += 1
            elif direction == 2:  # Move along length (opposite direction)
                robo_vel.linear.x = -length_speed
                robo_vel.linear.y = 0
                direction = 3
                sides_completed += 1
            elif direction == 3:  # Move along width (opposite direction)
                robo_vel.linear.x = 0
                robo_vel.linear.y = -width_speed
                direction = 0
                sides_completed += 1

        del_t += 1
        pub.publish(robo_vel)
        rate.sleep()
    
    # Stop the turtle after completing the rectangle
    stop_msg = Twist()
    pub.publish(stop_msg)
    rospy.loginfo("Rectangle completed!")

if __name__ == '__main__':
    try:
        rectangular_movement()
    except rospy.ROSInterruptException:
        pass