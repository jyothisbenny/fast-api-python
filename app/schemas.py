from pydantic import BaseModel


class PostCreate(BaseModel):
    title: str
    content: str


class PostUpdate(BaseModel):
    title: str
    content: str


class Post(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        orm_mode = True
