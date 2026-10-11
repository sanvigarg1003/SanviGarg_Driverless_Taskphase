import rclpy
from rclpy.node import Node
from rt2string_msg.msg import RT2String

class StringPublisher(Node):
    def __init__(self):
        super().__init__('string_publisher')
        self.pub = self.create_publisher(RT2String, '/rt2_string', 10)
    def publish_string(self):
        text = input("Enter a string")
        msg = RT2String()
        msg.data = text
        self.pub.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    node = StringPublisher()
    node.publish_string()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
