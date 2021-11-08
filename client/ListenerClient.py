import socket
import struct


class ListenerClient:
    def __init__(self, order):
        # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # s.bind('0.0.0.0', 45645)
        # data, address = s.recvfrom(2048)
        # te = ''
        # for d in data:
        #     te = te + d
        # self.order = te
        self.order = order

    def get_order(self):
        return self.order.decode()
