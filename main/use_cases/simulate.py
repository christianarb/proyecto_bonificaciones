from main.domain.entities import Producto
from main.domain.services import calcular_bonificaciones

def simular_bonificaciones_use_case(payload: list) -> list:
    productos = [Producto(**item) for item in payload]
    bonificados = calcular_bonificaciones(productos)
    return [bon.__dict__ for bon in bonificados]
