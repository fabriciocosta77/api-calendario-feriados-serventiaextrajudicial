from pydantic import BaseModel

class Holiday(BaseModel):
    dia: int
    mes: int
    descricao: str