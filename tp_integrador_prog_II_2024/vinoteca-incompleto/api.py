from flask import Flask, jsonify


app=Flask(__name__)

from vinoteca import *

@app.route('/api/bodegas/')
@app.route('/api/bodegas')
@app.route('/api/cepas/')
@app.route('/api/cepas')
@app.route('/api/vinos/')
@app.route('/api/vinos')
def api():
    return jsonify({'mesaje':'holaaaaa'})

if __name__ == '__main__':
    app.run(port=5000)