from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota simples para teste
@app.route('/')
def index():
    return 'Servidor Flask online!'

# Exemplo de rota para receber dados do robô (POST)
@app.route('/dados', methods=['POST'])
def receber_dados():
    dados = request.get_json()
    print(f"Dados recebidos: {dados}")
    return jsonify({"status": "ok", "mensagem": "Dados recebidos com sucesso"})

if __name__ == '__main__':
    app.run()
