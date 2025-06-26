# main/adapters/controllers.py
from flask import Blueprint, request, jsonify
from main.use_cases.simulate import simular_bonificaciones_use_case

bonificaciones_bp = Blueprint('bonificaciones', __name__)

@bonificaciones_bp.route('/simular', methods=['POST'])
def simular():
    pedido = request.get_json()
    resultado = simular_bonificaciones_use_case(pedido)
    return jsonify(resultado)
