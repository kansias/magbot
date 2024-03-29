import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid
from std_msgs.msg import Header

class MapPublisher(Node):
    def __init__(self):
        super().__init__('map_publisher')
        self.publisher_ = self.create_publisher(OccupancyGrid, 'map', 10)
        self.timer = self.create_timer(1.0, self.publish_map)

    def publish_map(self):
        map_msg = OccupancyGrid()
        map_msg.header = Header()
        map_msg.header.stamp = self.get_clock().now().to_msg()
        map_msg.header.frame_id = 'map'
        map_msg.info.resolution = 0.05  # 격자 하나당 5cm
        map_msg.info.width = 100  # 100 격자
        map_msg.info.height = 100  # 100 격자
        map_msg.info.origin.position.x = 0.0
        map_msg.info.origin.position.y = 0.0
        map_msg.info.origin.position.z = 0.0
        map_msg.info.origin.orientation.w = 1.0
        map_msg.data = [-1 for _ in range(100 * 100)]  # 모든 격자를 알 수 없는 상태(-1)로 초기화
        self.publisher_.publish(map_msg)

def main(args=None):
    rclpy.init(args=args)
    map_publisher = MapPublisher()
    rclpy.spin(map_publisher)
    map_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
