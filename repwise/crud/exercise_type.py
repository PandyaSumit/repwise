from repwise.crud.base import CRUDRepository
from repwise.models.exercise import ExerciseType

exercise_type_crud: CRUDRepository[ExerciseType] = CRUDRepository(model=ExerciseType)
