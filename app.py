from flask import Flask,send_from_directory
from main.adapters.controllers import bonificaciones_bp
import os
app = Flask(__name__)
app.register_blueprint(bonificaciones_bp)


# Archivo: main/adapters/controllers.py
from flask import Blueprint, request, jsonify
from main.use_cases.simulate import simular_bonificaciones_use_case

bonificaciones_bp = Blueprint('bonificaciones', __name__)

@bonificaciones_bp.route('/simular', methods=['POST'])
def simular():
    pedido = request.get_json()
    resultado = simular_bonificaciones_use_case(pedido)
    return jsonify(resultado)


@app.route('/')
def serve_frontend():
    return send_from_directory(os.path.join(app.root_path, 'frontend'), 'index.html')

if __name__ == '__main__':
    app.run(debug=True)