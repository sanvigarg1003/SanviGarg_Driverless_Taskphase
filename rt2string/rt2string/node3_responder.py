import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String

class Responder(Node):
    def __init__(self):
        super().__init__('responder')
        self.sub = self.create_subscription(
            Int32, '/palindrome_result', self.send_response, 10)
        self.pub = self.create_publisher(
            String, '/palindrome_response', 10)
    def send_response(self, msg):
        response = String()

        if msg.data == 1:
            response.data = 'Yes'
        else:
            response.data = 'No'
        self.pub.publish(response)
def main(args=None):
    rclpy.init(args=args)
    node = Responder()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
