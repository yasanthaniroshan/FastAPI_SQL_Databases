from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    nickname: str
    
 