#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import cv2
from cv_bridge import CvBridge
from std_msgs.msg import String


class ValidaAmbiente(Node):
    def __init__(self):
        super().__init__('valida_ambiente')
        self.ponte = CvBridge()
        self.publicador = self.create_publisher(String, 'dog_ia/status', 10)
        self.temporizador = self.create_timer(2.0, self.publicar_status)
        self.get_logger().info('No de validacao do DOG-IA iniciado')

    def publicar_status(self):
        mensagem = String()
        mensagem.data = 'DOG-IA Operacional: ROS 2 + OpenCV Prontos!'
        self.publicador.publish(mensagem)
        self.get_logger().info(f'Mensagem publicada: "{mensagem.data}"')


def main(args=None):
    rclpy.init(args=args)
    no = ValidaAmbiente()
    try:
        rclpy.spin(no)
    except KeyboardInterrupt:
        pass
    finally:
        no.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
