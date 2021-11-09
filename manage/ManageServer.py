import socket
from packs.BaseHeader import BaseHeader
from packs.BaseQuestion import BaseQuestion
from packs.BaseAnswer import BaseAnswer
from packs.BaseAdditional import BaseAdditional
from manage.ManageOrder import ManageOrder
from manage.ManageResult import ManageResult


class ManageServer:
    def __init__(self, cmd):
        self.cmd = cmd
        print('')

    def dns_server(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('0.0.0.0', 53))
        data, ad = s.recvfrom(2048)

        # 响应头
        header = BaseHeader(data)
        header_index = header.index

        # 问题区
        question = BaseQuestion(data)
        question_index = question.index
        q_name = question.q_name

        # A记录
        answer = BaseAnswer(data, q_name, question_index)
        answer_index = answer.index

        # 附加区
        additional = BaseAdditional(self.cmd, data, answer_index)

        response = header.get_header() + question.get_question() + answer.get_answer() + additional.get_additional()
        s.sendto(response, ad)

