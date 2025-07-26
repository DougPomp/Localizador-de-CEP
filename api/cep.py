from flask import Flask, jsonify
import requests

# Inicializa a aplicação Flask
app = Flask(__name__)


# A única rota da nossa API
@app.route('/consulta/<cep>')
def consulta_cep(cep):
    """
    Busca os dados de um CEP na API do ViaCEP.
    Esta função é o nosso endpoint serverless.
    """
    # Limpa o CEP, mantendo apenas os dígitos
    cep_sanitizado = ''.join(filter(str.isdigit, cep))

    # Valida se o CEP possui 8 dígitos
    if len(cep_sanitizado) != 8:
        return jsonify({"erro": "Formato de CEP inválido. O CEP deve conter 8 dígitos."}), 400

    try:
        # Faz a requisição para a API ViaCEP
        response = requests.get(f'https://viacep.com.br/ws/{cep_sanitizado}/json/')

        # Lança uma exceção para respostas com erro (ex: 404)
        if "erro" in dados:
            return jsonify({"erro": "CEP não foi encontrado!"}), 404
        dados = response.json()

        # Retorna os dados obtidos como uma resposta JSON
        return jsonify(dados)

    except requests.exceptions.RequestException as e:
        # Em caso de erro na requisição, retorna uma mensagem de erro
        return jsonify({"erro": f"Erro ao consultar o serviço ViaCEP: {e}"}), 500
