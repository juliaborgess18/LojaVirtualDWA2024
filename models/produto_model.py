from dataclasses import dataclass
from typing import Optional


@dataclass
class Produto():
    id: Optional[int] = None
    nome: Optional[str] = None
    preco: Optional[float] = None
    descricao: Optional[str] = None
<<<<<<< HEAD
    estoque: Optional[int] = None
    id_categoria: Optional[int] = None
=======
    estoque: Optional[int] = None
>>>>>>> aae658d356c8ba08adc33219f8cb390ce4cb0981
