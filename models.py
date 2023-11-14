from pydantic import BaseModel

class Project(BaseModel):
    title: str
    description: str
    client: str


hostURL: str = 'http://127.0.0.1:8000/'