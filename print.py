class Printer(object):
    def __init__(self):
        self.values = []

    def log(self, *values):
        self.values = [v for v in values]
        print(self.values)

class FormattedPrinter(Printer):
    
    def formated_log(self, *values):
        print('*****************************')
        self.log(*values)
        print('*****************************')

pr1 = Printer()
pr1.log(10, 20, 50)

pr2 = FormattedPrinter()
pr2.formated_log(20, 40, 60)