

class ManageOrder:
    def __init__(self, order):
        self.order = order

    def get_order(self):
        return self.order.decode()
