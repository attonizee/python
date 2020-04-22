class Animals(object):
    def __init__(self, animal):
        self.animal = animal

class Human(Animals):
    def is_danger(self, animal):
        self.danger = ['poison', 'predator']
        if self.animal in self.danger:
            print(f'{self.animal} is dangerous for you')
        else:
            print(f'{self.animal} its good to go')

panda = Human('panda')
panda.is_danger('panda')
