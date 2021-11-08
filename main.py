import socket
from packs.BaseHeader import BaseHeader
from packs.BaseQuestion import BaseQuestion
from packs.BaseAnswer import BaseAnswer
from packs.BaseAdditional import BaseAdditional


def dns_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('0.0.0.0', 53))
    data, ad = s.recvfrom(2048)

    header = BaseHeader(data)
    header.print_header()

    question = BaseQuestion(data)
    print(question.get_domain())

    answer = BaseAnswer()
    additional = BaseAdditional()
    response = header.get_header() + question.get_question() + answer.get_answer() + additional.get_additional()
    print(response)

    s.sendto(response, ad)


while True:
    dns_server()
