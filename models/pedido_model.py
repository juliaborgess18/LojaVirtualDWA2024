from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

<<<<<<< HEAD
from models.item_pedido_model import ItemPedido
from models.usuario_model import Usuario

=======
>>>>>>> aae658d356c8ba08adc33219f8cb390ce4cb0981

class EstadoPedido(Enum):
    CARRINHO = "carrinho"
    PENDENTE = "pendente"
    PAGO = "pago"
    FATURADO = "faturado"
    SEPARADO = "separado"
    ENVIADO = "enviado"
    ENTREGUE = "entregue"
    CANCELADO = "cancelado"


@dataclass
class Pedido:
    id: Optional[int] = None
    data_hora: Optional[datetime] = None
    valor_total: Optional[float] = None
    endereco_entrega: Optional[str] = None
    estado: Optional[EstadoPedido] = None
    id_cliente: Optional[int] = None
<<<<<<< HEAD
    cliente: Optional[Usuario] = None
    itens: Optional[list[ItemPedido]] = None

=======
>>>>>>> aae658d356c8ba08adc33219f8cb390ce4cb0981
