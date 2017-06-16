from bottle import get, post, request, run, static_file
from os import path

@get('/')
def home():
    caminho_servidor = path.dirname(path.realpath(__file__))
    return static_file('index.html', caminho_servidor)

@get('/<filepath:path>')
def server_static(filepath):
    caminho_servidor = path.dirname(path.realpath(__file__))
    return static_file(filepath, root=caminho_servidor)

@post('/apoiar')
def apoiar():
    nome = request.forms.get('apoio_nome')
    email = request.forms.get('apoio_email')
    mensagem = request.forms.get('apoio_mensagem')

    print('%s (%s) apoia.\nMensagem: %s' % (nome, email, mensagem))

    return '<p>Obrigada pelo apoio!</p>'

run(host='localhost', port=8080, debug=True)
