from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Servidor da IA do Rover está online!"

@app.route("/api/dados", methods=["POST"])
def processar():
    dados = request.json
    print("Recebido:", dados)

    # IA simples com base nos sensores
    linha = dados.get("linha", 1)
    distancia_frente = dados.get("distancia_frente", 999)
    cor = dados.get("cor", "desconhecida")

    # Decisão baseada em regras
    if distancia_frente < 200:
        acao = "parar"
    elif linha == 0:
        acao = "ajustar_rota"
    elif cor == "vermelho":
        acao = "desviar"
    else:
        acao = "seguir"

    return jsonify({"acao": acao})
