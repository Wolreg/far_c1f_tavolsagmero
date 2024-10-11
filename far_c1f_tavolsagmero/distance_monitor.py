#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range

class DistanceMonitor(Node):
    def __init__(self):
        super().__init__('distance_monitor')
        self.subscription = self.create_subscription(Range, 'distance', self.listener_callback, 10)
        self.subscription  

    def listener_callback(self, msg):
        self.get_logger().info(f'Received distance: {msg.range:.2f} meters')
        if msg.range < 1.0:  # Ha a távolság kisebb, mint 1 méter, figyelmeztetés jelenik meg
            self.get_logger().warn('Warning: Distance is below 1 meter!')

def main(args=None):
    rclpy.init(args=args)
    node = DistanceMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
