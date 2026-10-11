import rclpy
from rclpy.node import Node
from taskone_msg.msg import TaskOne

class Publisher(Node):
    def __init__(self):
        super().__init__('publisher')
        self.pub = self.create_publisher(TaskOne, '/taskone', 10)
    def send_data(self):
        msg = TaskOne()
        msg.ang_vel = float(input("Enter angular velocity"))
        msg.radius = float(input("Enter radius"))
        self.pub.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    node = Publisher()
    node.send_data()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
