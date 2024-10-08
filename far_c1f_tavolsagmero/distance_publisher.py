import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range
import random

class DistancePublisher(Node):
    def __init__(self):
        super().__init__('distance_publisher')
        self.publisher_ = self.create_publisher(Range, 'distance', 10)
        timer_period = 1.0  # másodpercenkénti publikálás
        self.timer = self.create_timer(timer_period, self.publish_distance)

    def publish_distance(self):
        msg = Range()
        msg.range = random.uniform(0.0, 10.0)  # Szimulált távolság (0.0-10.0 között)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing distance: {msg.range:.2f} meters')

def main(args=None):
    rclpy.init(args=args)
    node = DistancePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
