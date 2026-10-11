import rclpy
from rclpy.node import Node
from taskone_msg.msg import TaskOne

class Subscriber(Node):
	def __init__(self):
         super().__init__('subscriber')
         self.sub = self.create_subscription(TaskOne, '/taskone', self.callback, 10)
	def callback(self, msg):
         speed = msg.ang_vel * msg.radius
         print("Longitudinal speed=", speed, "m/s")
def main(args=None):
    rclpy.init(args=args)
    node = Subscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
