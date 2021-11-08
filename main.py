import socket
import _thread
from packs.BaseHeader import BaseHeader
from packs.BaseQuestion import BaseQuestion
from packs.BaseAnswer import BaseAnswer
from packs.BaseAdditional import BaseAdditional
from client.ListenerClient import ListenerClient


def dns_server(cmd):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('0.0.0.0', 53))
    data, ad = s.recvfrom(2048)

    if data[:6] == b'biubiu':
        return data

    header = BaseHeader(data)
    question = BaseQuestion(data)
    answer = BaseAnswer()
    additional = BaseAdditional(data)

    response = header.get_header() + question.get_question() + answer.get_answer() + additional.get_additional()
    s.sendto(response, ad)

    print('ad:', ad)

    return data


client = ListenerClient(b'')
while True:
    order = client.get_order()
    data = dns_server(order)
    if data[:6] == b'biubiu':
        client.order = data[6:]

