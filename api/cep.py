from flask import Flask, jsonify
import requests
from serverless_wsgi import handle

# Inicializa a aplicação Flask
app = Flask(__name__)


@app.route('/consulta/<cep>')
def consulta_cep(cep):
    """
    Busca os dados de um CEP na API do ViaCEP.
    """
    cep_sanitizado = ''.join(filter(str.isdigit, cep))

    if len(cep_sanitizado) != 8:
        return jsonify({"erro": "Formato de CEP inválido. O CEP deve conter 8 dígitos."}), 400

    try:
        response = requests.get(f'https://viacep.com.br/ws/{cep_sanitizado}/json/')
        # Lança uma exceção para respostas com erro (ex: 404)
        if "erro" in dados:
            return jsonify({"erro": "CEP não foi encontrado!"}), 404
        dados = response.json()
        return jsonify(dados)

    except requests.exceptions.RequestException as e:
        return jsonify({"erro": f"Erro ao consultar o serviço ViaCEP: {e}"}), 500


def handler(event, context):
    """
    Esta é a função handler explícita que o Netlify (AWS Lambda) irá chamar.
    Ela usa a biblioteca serverless-wsgi para traduzir o evento da Lambda
    para um formato que o Flask entende.
    """
    return handle(app, event, context)
