from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel
class Gender(str, Enum):
    admin:"admin"
    user:"user"
    student:"student"

class Role(str, Enum):
    male:"male"
    female:"female"
    
class User(BaseModel):
    id: Optional[UUID]=uuid4
    first_name:str
    last_name:str
    middle_name:Optional[str]
    gender:Gender
    roles:List[Role]