from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api-via-cep', methods=['GET'])
def dados_cep():
    cep = request.args['cep']
    return render_template('dados_cep.html', cep_consultado=cep)
    
if __name__ == '__main__':
    app.run(debug=True)

