from flask import Flask, jsonify, request

app = Flask(__name__)

# Função que cria pastas de cliente
def criate():
    # Lógica para criar pastas
    print('pasta criada')
    return {"status": "success", "message": "Pasta criada com sucesso"}

# Função que importa notas de serviço
def import_serv():
    # Lógica para importar
    print('Importada')
    return {"status": "success", "message": "Nota de serviço importada com sucesso"}

# Função que baixa notas de serviço
def download():
    # Lógica para download
    print('baixando')
    return {"status": "success", "message": "Download iniciado com sucesso"}

# Endpoint para criar pastas de cliente
@app.route('/api/criate', methods=['POST'])
def api_criate():
    result = criate()
    return jsonify(result)

# Endpoint para importar notas de serviço
@app.route('/api/import_serv', methods=['POST'])
def api_import_serv():
    result = import_serv()
    return jsonify(result)

# Endpoint para baixar notas de serviço
@app.route('/api/download', methods=['POST'])
def api_download():
    result = download()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
