from flask import Flask, jsonify, render_template
import json
import os

app = Flask(__name__)

# Cargar el archivo JSON
with open('vinoteca.json', 'r') as f:
    data = json.load(f)

bodegas = data['bodegas']
cepas = data['cepas']
vinos = data['vinos']

# Ruta principal para renderizar el HTML
@app.route('/')
def index():
    return render_template('index.html')

# Rutas de datos para los botones
@app.route('/data/listado_bodegas')
def listado_bodegas():
    return jsonify(bodegas)

@app.route('/data/listado_cepas')
def listado_cepas():
    return jsonify(cepas)

@app.route('/data/listado_vinos')
def listado_vinos():
    return jsonify(vinos)

# Ruta para obtener una bodega por ID
@app.route('/data/bodega/<string:bodega_id>')
def obtener_bodega(bodega_id):
    bodega = next((b for b in bodegas if b['id'] == bodega_id), None)
    if bodega:
        return jsonify(bodega)
    else:
        return jsonify({"error": "Bodega no encontrada"}), 404

# Ruta para obtener una cepa por ID
@app.route('/data/cepa/<string:cepa_id>')
def obtener_cepa(cepa_id):
    cepa = next((c for c in cepas if c['id'] == cepa_id), None)
    if cepa:
        return jsonify(cepa)
    else:
        return jsonify({"error": "Cepa no encontrada"}), 404

# Ruta para obtener un vino por ID
@app.route('/data/vino/<string:vino_id>')
def obtener_vino(vino_id):
    vino = next((v for v in vinos if v['id'] == vino_id), None)
    if vino:
        return jsonify(vino)
    else:
        return jsonify({"error": "Vino no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
