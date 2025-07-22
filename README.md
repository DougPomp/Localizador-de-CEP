# 🌍 Localizador de CEP

Aplicação web desenvolvida como projeto colaborativo da comunidade Zeronauta. O sistema permite ao usuário digitar um CEP e receber automaticamente as informações de endereço, integrando front-end e back-end com a API pública ViaCEP.

---

## 🚀 Tecnologias Utilizadas

- **HTML** & **CSS** — Estrutura e estilização da interface
- **JavaScript** — Lógica de interação no front-end
- **Python** com **Flask** — Back-end leve e rápido
- **API ViaCEP** — Busca de dados de endereço via CEP (https://viacep.com.br)

---

## 🧠 Como funciona?

1. O usuário insere um CEP na interface.
2. O front-end envia uma requisição para o back-end Flask.
3. O Flask faz uma chamada à API ViaCEP.
4. Os dados retornam e são exibidos na tela com formatação amigável.

---

## 📦 Como rodar o projeto localmente

```bash
# Clone este repositório
git clone https://github.com/seu-usuario/localizador-cep.git
cd localizador-cep

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python app.py
