class Log(object):
    def __init__(self):
        self.total = 0
        self.fail = 0
        self.success_rate = 0

    def calculate_rate(self, num1, num2):
        total = num1
        fail = num2
        success_rate = (total - fail) / total * 100
        return success_rate

    def product_log(self):
        pass
