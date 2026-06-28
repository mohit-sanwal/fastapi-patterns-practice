from fastapi import FastAPI 
from step1_repository import Person, PersonRepository, InMemoryPersonRepository
from step2_service import PersonService

# comment
app = FastAPI()

repo = InMemoryPersonRepository()
service = PersonService(repo)

@app.get("/people")
def list_all():
    people = service.list_people()
    return [{'id': p.id, 'name': p.name, 'age': p.age} for p in people]

@app.get("/people/legal-age")
def list_legal_age():
    people = service.list_legal_age_people()
    return [{'id': p.id, 'name': p.name, 'age': p.age} for p in people]




