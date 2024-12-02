from pydantic import BaseModel, field_validator

from util.validators import is_project_name


class NovaCategoriaDTO(BaseModel):
    nome: str
    
    @field_validator("nome")
    def validar_nome(cls, v):
        msg = is_project_name(v, "Nome")
        if msg:
            raise ValueError(msg)
        return v