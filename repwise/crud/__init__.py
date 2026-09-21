from repwise.crud.body_part import bodypart_crud
from repwise.crud.exercise import exercise_crud
from repwise.crud.exercise_type import exercise_type_crud
from repwise.crud.level import level_crud
from repwise.crud.training_plan import training_plan_crud
from repwise.crud.training_unit import training_unit_crud
from repwise.crud.user import user_crud

__all__ = [
    "exercise_crud",
    "exercise_type_crud",
    "level_crud",
    "user_crud",
    "bodypart_crud",
    "training_plan_crud",
    "training_unit_crud",
]
