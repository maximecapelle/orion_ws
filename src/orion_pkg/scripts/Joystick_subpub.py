#!/usr/bin/env python3
import rclpy
import numpy as np
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Joy

# Logitech Gamepad F710
F710_BUTTON_MAP = {
    'A': 0,
    'B': 1,
    'X': 2,
    'Y': 3,
    'LB': 4,
    'RB': 5,
    'EMPTY': 6,
    'BACK': 7,
    'START': 8,
    'HOME': 9,
    'L3': 10,
    'R3': 11
}

ButtonNameConversion = ['A', 'B', 'X', 'Y', 'LB', 'RB', 'EMPTY', 'BACK', 'START', 'HOME', 'L3', 'R3']

class Joystick_Command_Interpreter(Node):
    def __init__(self):
        super().__init__("hw_sub_node")
        self.sub = self.create_subscription(Joy, "joy", self.subscriber_callback, 10)
    
    def subscriber_callback(self, msg):
        # print(f"Buttons:  {msg.buttons[1]}")
        button_array = np.array(msg.buttons)
        if np.sum(button_array) >= 1:
            idxs = np.where(button_array == 1)
            # print(idxs, type(idxs))
            for idx in idxs:
                # print(idx[0])
                print(f"\n\n YOU PRESSED: {ButtonNameConversion[idx[0]]}")


def main(args=None):
    rclpy.init()
    my_sub = Joystick_Command_Interpreter()
    print("Waiting for data to be published...")

    try: 
        rclpy.spin(my_sub)
    except KeyboardInterrupt:
        print("Terminating Node")
        my_sub.destroy_node()


if __name__ == '__main__':    #This means that this file can be run as a script but isnt actually redefined in the other file.
    main()
