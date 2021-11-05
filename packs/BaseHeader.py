import struct
import prettytable as pt


class BaseHeader:
    def __init__(self, data):
        self.data = data
        (
            self.tid,
            self.flags,
            self.quests,
            self.answers,
            self.author,
            self.addition
        ) = struct.unpack('>HHHHHH', data[:12])

    def print_header(self):
        tid = bin(self.tid + 65536)[3:]
        flags = bin(self.flags + 65536)[3:]
        quests = bin(self.quests + 65536)[3:]
        answers = bin(self.answers + 65536)[3:]
        author = bin(self.author + 65536)[3:]
        addition = bin(self.addition + 65536)[3:]

        print('Header：')
        title = [
            '',
            '0 ', '1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ',
            '8 ', '9 ', '10', '11', '12', '13', '14', '15',
            'hex'
        ]
        tab = pt.PrettyTable(title)
        tab.add_row(['transactionID'] + list(tid) + [hex(self.tid)])
        tab.add_row(['flags'] + list(flags) + [hex(self.flags)])
        tab.add_row(['quests'] + list(quests) + [hex(self.quests)])
        tab.add_row(['answers'] + list(answers) + [hex(self.answers)])
        tab.add_row(['author'] + list(author) + [hex(self.author)])
        tab.add_row(['addition'] + list(addition) + [hex(self.addition)])

        print(tab)

    def get_header(self):
        answers = 1
        flags = 33152
        header = struct.pack(
            '>HHHHHH',
            self.tid,
            flags,
            self.quests,
            answers,
            self.author,
            self.addition
        )
        return header
