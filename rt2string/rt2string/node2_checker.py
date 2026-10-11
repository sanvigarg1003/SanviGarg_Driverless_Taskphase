import rclpy
from rclpy.node import Node
from rt2string_msg.msg import RT2String
from std_msgs.msg import Int32, String

class PalindromeChecker(Node):
    def __init__(self):
        super().__init__('palindrome_checker')
        self.sub = self.create_subscription(
            RT2String, '/rt2_string', self.check_palindrome, 10)
        self.pub = self.create_publisher(
            Int32, '/palindrome_result', 10)
        self.response_sub = self.create_subscription(
            String, '/palindrome_response', self.receive_response, 10)
    def check_palindrome(self, msg):
        result = Int32()

        if msg.data == msg.data[::-1]:
            result.data = 1
        else:
            result.data = 0
        self.pub.publish(result)
    def receive_response(self, msg):
        print("Response", msg.data)
def main(args=None):
    rclpy.init(args=args)
    node = PalindromeChecker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
