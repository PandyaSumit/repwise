from repwise.api.routes.auth import router as auth_router
from repwise.api.routes.body_part import router as bodypart_router
from repwise.api.routes.exercise import router as exercise_router
from repwise.api.routes.exercise_type import router as exercise_type_router
from repwise.api.routes.level import router as level_router
from repwise.api.routes.training_plan import router as training_plan_router
from repwise.api.routes.training_unit import router as training_unit_router
from repwise.api.routes.user import router as user_router

__all__ = [
    "auth_router",
    "bodypart_router",
    "exercise_router",
    "exercise_type_router",
    "level_router",
    "user_router",
    "training_plan_router",
    "training_unit_router",
]
