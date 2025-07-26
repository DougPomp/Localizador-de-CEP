from flask import Flask, render_template, jsonify
import requests

# Inicializa a aplicação Flask
app = Flask(__name__)


@app.route('/')
def index():
    """Renderiza a página principal da aplicação."""
    return render_template('index.html')


@app.route('/consulta/<cep>')
def consulta_cep(cep):
    """
    Busca os dados de um CEP na API do ViaCEP.
    A rota recebe um CEP, faz a consulta e retorna os dados em formato JSON.
    """
    # Limpa o CEP, mantendo apenas os dígitos
    cep_sanitizado = ''.join(filter(str.isdigit, cep))

    # Valida se o CEP possui 8 dígitos
    if len(cep_sanitizado) != 8:
        return jsonify({"erro": "Formato de CEP inválido. O CEP deve conter 8 dígitos."}), 400

    try:
        # Faz a requisição para a API ViaCEP
        response = requests.get(f'https://viacep.com.br/ws/{cep_sanitizado}/json/')
        dados = response.json()

        # Lança uma exceção para respostas com erro (ex: 404)
        if "erro" in dados:
            return jsonify({"erro": "CEP não foi encontrado!"}), 404

        # Retorna os dados obtidos como uma resposta JSON
        return jsonify(dados)

    except requests.exceptions.RequestException as e:
        # Em caso de erro na requisição, retorna uma mensagem de erro
        return jsonify({"erro": f"Erro ao consultar o serviço ViaCEP: {e}"}), 500


# Executa a aplicação em modo de depuração
if __name__ == '__main__':
    app.run(debug=True)
