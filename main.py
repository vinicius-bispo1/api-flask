from flask import Flask, jsonify, render_template, request
from config import Config
from models import banco_dados, Cadastro

app = Flask(__name__)
app.config.from_object(Config)
banco_dados.init_app(app)

# PEGAR TODOS


@app.route('/login')
def login():
    cadastros = Cadastro.query.all()
    dados_json = [cadastro.to_dict() for cadastro in cadastros]
    return jsonify(dados_json)

# SELECIONAR UM INDIVIDUAL


@app.route('/atualizar/<int:id>')
def atualizar(id):
    cadastro = Cadastro.query.filter_by(id=id).first()
    dados_json = cadastro.to_dict()
    print(dados_json)
    return jsonify(dados_json)

# CADASTRAR


@app.route('/usuario', methods=['POST'])
def cria_cadastro():
    dados = request.get_json()
    cadastro = Cadastro(nome=dados['nome'], idade=dados['idade'], endereco=dados['endereco'],
                        email=dados['email'], cpf=dados['cpf'], bairro=dados['bairro'], cep=dados['cep'])
    try:
        banco_dados.session.add(cadastro)
        banco_dados.session.commit()
        return jsonify('Dados cadastrado com sucesso !')
    except Exception as e:
        print(e)
        return f'Erro ao cadastrar produto', 400


@app.route('/atualizar/<int:id>', methods=['PUT'])
def atualizacao(id):
    cadastro = Cadastro.query.filter_by(id=id).first()
    dados = request.get_json()
    try:
        if ('nome' in dados):
            cadastro.nome = dados['nome']
        if ('idade' in dados):
            cadastro.idade = dados['idade']
        if ('endereco' in dados):
            cadastro.endereco = dados['endereco']
        if ('email' in dados):
            cadastro.email = dados['email']
        if ('cpf' in dados):
            cadastro.cpf = dados['cpf']
        if ('bairro' in dados):
            cadastro.bairro = dados['bairro']
        if ('cep' in dados):
            cadastro.cep = dados['cep']

        print(cadastro.nome)
        print(banco_dados.session.add(cadastro))
        banco_dados.session.commit()
        return f'Atualização feita com sucesso !', 200
    except Exception as e:
        print(e)
        return render_template('Erro ao cadastrar produto'), 400


@app.errorhandler(404)
def pagina_nao_encontrada(erro):
    return render_template('erro.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
