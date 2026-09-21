from repwise.crud.base import CRUDRepository
from repwise.models.level import Level

level_crud: CRUDRepository[Level] = CRUDRepository(model=Level)
