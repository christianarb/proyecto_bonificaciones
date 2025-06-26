from dataclasses import dataclass

@dataclass
class Producto:
    codigo: str
    grupo: str
    cantidad: int

@dataclass
class ResultadoBonificacion:
    codigo: str
    bonificacion: int