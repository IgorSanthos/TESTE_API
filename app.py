from flask import Flask, jsonify

app = Flask(__name__)

# Rota para retornar a versão do software
@app.route('/api/version', methods=['GET'])
def get_version():
    return jsonify({"version": "1.0.0"})

# Rota de exemplo para futuros endpoints
@app.route('/api/dados', methods=['GET'])
def get_dados():
    return jsonify({"message": "Dados recebidos com sucesso!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
