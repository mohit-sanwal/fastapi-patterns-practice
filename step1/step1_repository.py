class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

class PersonRepository:
    def find_all(self):
        raise NotImplementedError

class InMemoryPersonRepository(PersonRepository):
    def find_all(self):
        return [
            Person(1, 'Rohit', 25),
            Person(1, 'Jack', 27),
            Person(1, 'Jill', 26),
        ]

repo = InMemoryPersonRepository()
for person in repo.find_all():
    print(person.name, person.age)