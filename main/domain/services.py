from typing import List
from main.domain.entities import Producto, ResultadoBonificacion
from config import GRUPO_BONIFICABLE

def calcular_bonificaciones(productos: List[Producto]) -> List[ResultadoBonificacion]:
    jugos = [p for p in productos if p.grupo == GRUPO_BONIFICABLE]
    total_jugos = sum(p.cantidad for p in jugos)
    total_bonificaciones = (total_jugos // 10) * 2

    if total_bonificaciones == 0:
        return []

    resultado = []
    for p in jugos:
        proporcion = p.cantidad / total_jugos
        bonificacion = round(proporcion * total_bonificaciones)
        if bonificacion > 0:
            resultado.append(ResultadoBonificacion(codigo=p.codigo, bonificacion=bonificacion))

    return resultado