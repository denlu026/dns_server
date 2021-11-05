import struct


class BaseQuestion:
    def __init__(self, data):
        self.data = data

        i = 0
        for q in data[12:]:
            if q == 0:
                break
            i += 1
        self.len = i+12+1
        self.q_name = data[12:self.len]
        (
            self.q_type,
            self.q_class
        ) = struct.unpack('>HH', self.data[self.len:self.len + 5])

    def print_question(self):
        print('data[12:]:', self.data[12:])
        print('data[12:]:', len(self.data[12:]))
        print('q_name:', self.q_name)
        print('q_name:', len(self.q_name))
        print('q_type:', self.q_type)
        print('q_class:', self.q_class)

    def get_domain(self):
        domain = ''
        i = 1
        while True:
            d = self.q_name[i]
            if d == 0:
                break
            if d < 32:
                domain = domain + '.'
            else:
                domain = domain + chr(d)

            i = i + 1
        return domain

    def get_question(self):
        question = (
                    self.q_name +
                    struct.pack(
                        '>HH',
                        self.q_type,
                        self.q_class
                    )
        )
        return question
