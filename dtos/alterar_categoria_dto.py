from pydantic import BaseModel, field_validator

from util.validators import is_greater_than, is_project_name


class AlterarCategoriaDTO(BaseModel):
    id: int
    nome: str
    
    @field_validator("id")
    def validar_id_produto(cls, v):
        msg = is_greater_than(v, "Id da Categoria", 0)
        if msg: raise ValueError(msg)
        return v
    
    @field_validator("nome")
    def validar_nome(cls, v):
        msg = is_project_name(v, "Nome")
        if msg:
            raise ValueError(msg)
        return v