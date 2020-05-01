class Person(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.known = []

    def know(self, person):
        if person not in self.known:
            self.known.append(person)
        else:
            print(f'The {self.name} already know the {person.name}.')

    def is_known(self, person):
        text_out = {True: ' is known with', False: ' is unknown with'}
        check = person in self.known
        print(f'{self.name} {text_out[check]} {person}')


person1 = Person(22, 'Ivan')
person1.know('Roma')
person1.is_known('Roma')

    