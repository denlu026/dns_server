import time


class ManageResult:
    def __init__(self, data_map):
        self.map = data_map
        self.file = open('temp', 'a+')
        self.update_temp()

    def select_temp(self, user_id):
        print(self.map)

        result = ''
        for f in self.file.readlines():
            if f.strip('\t')[0] == user_id:
                result = result + f
        return result

    def update_temp(self):
        for key in self.map.keys():
            if key == 'user_id':
                u_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                print('更新：', self.map['user_id'], self.map['manage'], u_time)
                self.file.write(self.map['user_id'].decode() + '\t')
                self.file.write(self.map['manage'].decode() + '\t')

                self.file.write(self.map['address'][0] + '\t')
                self.file.write(str(self.map['address'][1]) + '\t')
                self.file.write(u_time)
                self.file.write('\n')
