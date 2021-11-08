import struct


class BaseAdditional:
    def __init__(self, data):
        print(data)
        self.data = b'\x00'

    def get_additional(self):
        return self.data
