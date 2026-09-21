from repwise.crud.base import CRUDRepository
from repwise.models.body_part import BodyPart

bodypart_crud: CRUDRepository[BodyPart] = CRUDRepository(model=BodyPart)
