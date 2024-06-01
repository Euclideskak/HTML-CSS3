from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/dub', methods=['POST'])
def dub():
    file = request.files['audioFile']
    # Aqui você processaria o áudio para dublagem usando PLN e síntese de voz
    # Por enquanto, apenas retornamos o nome do arquivo para teste
    return f'Dublagem do arquivo {file.filename} concluída!'

if __name__ == '__main__':
    app.run(debug=True)
