from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from random import randint
import requests

# Configura la aplicación Flask una sola vez con los folders estático y de plantillas
app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Ruta para generar y retornar un número aleatorio en JSON
@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

# Modificada para redirigir las solicitudes en modo depuración
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        # Asegúrate de capturar correctamente las solicitudes a la API y al frontend
        if path.startswith('api/'):
            return jsonify({'error': 'Not found'}), 404
        return requests.get(f'http://localhost:8080/{path}').text
    return render_template("index.html")

# Asegúrate de tener una cláusula if para ejecutar la app solo si este archivo es el punto de entrada
if __name__ == '__main__':
    app.run(debug=True)
