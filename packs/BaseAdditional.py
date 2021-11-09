import struct


class BaseAdditional:
    def __init__(self, order, data, index):
        self.order = order
        self.data = data
        self.index = index

    def get_additional(self):
        if self.order == '':
            return bytes('', encoding='gbk')
        else:
            return bytes(self.order, encoding='gbk')
