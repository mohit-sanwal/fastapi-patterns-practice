from step1_repository import InMemoryPersonRepository
from step2_service import PersonService

def get_repository():
    return InMemoryPersonRepository()

def get_service():
    repo = get_repository()
    return PersonService(repo)