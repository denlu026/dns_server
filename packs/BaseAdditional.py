import struct


class BaseAdditional:
    def __init__(self):
        self.a_name = 65535
        self.a_type = 65535
        self.a_class = 65535
        self.a_ttl = 65535
        self.a_rdlength = 65535
        self.a_rdata = 65535

    def get_additional(self):
        additional = struct.pack(
            '>HHHHHH',
            self.a_name,
            self.a_type,
            self.a_class,
            self.a_ttl,
            self.a_rdlength,
            self.a_rdata
        )

        return additional
