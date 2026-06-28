
from step1_repository import Person, PersonRepository, InMemoryPersonRepository

# ---------------
#  — Service
# ---------------

class PersonService:
    def __init__(self, repository):
        self.repository = repository

    def list_people(self):
        return self.repository.find_all()

    def list_legal_age_people(self):
        return [p for p in self.list_people() if p.age >= 18]


repo = InMemoryPersonRepository()
service = PersonService(repo)

print('all people');
for p in service.list_people():
    print(p.name, p.age)
print('legal people');
for p in service.list_legal_age_people():
    print(p.name, p.age)