from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Servidor da IA do Rover está online!"

@app.route("/api/dados", methods=["POST"])
def processar():
    dados = request.json
    print("Recebido:", dados)

    # Regras simples de IA
    if dados.get("distancia_frente", 1000) < 200:
        acao = "parar"
    elif dados.get("linha", 1) == 0:
        acao = "ajustar_rota"
    else:
        acao = "seguir"

    return jsonify({"acao": acao})
