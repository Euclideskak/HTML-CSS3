from flask import Flask

# Criando uma instância da aplicação Flask
app = Flask(__name__)

# Definindo a rota para a página inicial
@app.route('/')
def index():
    return '<h1>Bem-vindo ao meu site em Python!</h1>'

# Executando a aplicação
if __name__ == '__main__':
    app.run(debug=True)