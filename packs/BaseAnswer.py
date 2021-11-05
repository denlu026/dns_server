import struct


class BaseAnswer:
    def __init__(self):
        self.a_name = 49164
        self.a_type = 1
        self.a_class = 1
        self.a_ttl = 190
        self.a_rdlength = 4
        self.a_rdata = '127.0.0.1'

    def get_answer(self):
        res = struct.pack(
            '>HHHLH',
            self.a_name,
            self.a_type,
            self.a_class,
            self.a_ttl,
            self.a_rdlength
        )
        s = self.a_rdata.split('.')
        ip = struct.pack('BBBB', int(s[0]), int(s[1]), int(s[2]), int(s[3]))

        answer = res + ip
        return answer
