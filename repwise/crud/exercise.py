from repwise.crud.base import CRUDRepository
from repwise.models.exercise import Exercise

exercise_crud: CRUDRepository[Exercise] = CRUDRepository(model=Exercise)
