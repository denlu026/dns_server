import struct


class BaseAnswer:
    def __init__(self, data, q_name, index):
        self.data = data
        self.index = index

        self.a_name = q_name
        self.a_type = 1
        self.a_class = 1
        self.a_ttl = 190
        self.a_length = 4
        self.a_rdata = '127.0.0.1'

    def get_answer(self):
        res = struct.pack(
            '>HHLH',
            self.a_type,
            self.a_class,
            self.a_ttl,
            self.a_length
        )
        s = self.a_rdata.split('.')
        ip = struct.pack('BBBB', int(s[0]), int(s[1]), int(s[2]), int(s[3]))

        answer = self.a_name + res + ip
        self.index = self.index + len(answer) - 1
        return answer
