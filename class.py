class Trash:
    def __init__(self, limit):
        self.limit = limit

    def get_limit(self):
        print(f'The trash size is {self.limit}')

    def status(self, garb):
        if garb.size <= self.limit:
            print(f'{garb} is in the trash')
        else:
            print(f'The size of {garb} bigger than trash limit {self.limit}')

class Bag(Trash):
    def __init__(self, limit):
        self.limit = limit

    def get_limit(self):
        print(f'The bag size is {self.limit}')

    def status(self, garb):
        if garb.size <= self.limit:
            print(f'{garb} is in the bag')
        else:
            print(f'The size is bigger than bag limit {self.limit}')

class Put:
    def __init__(self, size):
        self.size = size

box1 = Trash(10)
box1.get_limit()
bag1 = Bag(5)
bag1.get_limit()
garb1 = Put(2)
garb2 = Put(3)
garb3 = Put(15)
box1.status(garb3)
bag1.status(garb1)


    


