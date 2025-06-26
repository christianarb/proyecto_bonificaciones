from flask import Flask,send_from_directory
from main.adapters.controllers import bonificaciones_bp
import os
app = Flask(__name__)
app.register_blueprint(bonificaciones_bp)

@app.route('/')
def serve_frontend():
    return send_from_directory(os.path.join(app.root_path, 'frontend'), 'index.html')

if __name__ == '__main__':
    app.run(debug=True)