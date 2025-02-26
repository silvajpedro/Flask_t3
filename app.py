# Importa a classe (Veremos isso mais a frente) Flask do pacote flask
from flask import Flask

# Cria uma instância(Veremos isso mais a frente) do Flask, que será a base do nosso aplicativo web
app = Flask(__name__)

# Define uma rota para o endpoint "/devedora"
# Isso significa que quando o usuário acessar "http://127.0.0.1:5000/devedora", essa função será executada
@app.route('/devedora')
def pague():
    # Retorna uma resposta em HTML para ser exibida no navegador
    return "<h1>Quem não deve, não teme!</h1>"

# Inicia o servidor Flask para rodar a aplicação localmente
# O servidor será executado em "http://127.0.0.1:5000/"
app.run()
