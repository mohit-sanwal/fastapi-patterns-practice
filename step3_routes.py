from fastapi import FastAPI, Depends
from step4_dependencies import get_service
from step2_service import PersonService

# comment
app = FastAPI()

@app.get("/people")
def list_all(service: PersonService = Depends(get_service)):
    people = service.list_people()
    return [{'id': p.id, 'name': p.name, 'age': p.age} for p in people]

@app.get("/people/legal-age")
def list_legal_age(service: PersonService = Depends(get_service)):
    people = service.list_legal_age_people()
    return [{'id': p.id, 'name': p.name, 'age': p.age} for p in people]




