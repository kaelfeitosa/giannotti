from bottle import post, request, run

@post('/apoiar')
def apoiar():
    nome = request.forms.get('apoio_nome')
    email = request.forms.get('apoio_email')
    mensagem = request.forms.get('apoio_mensagem')

    print('%s (%s) apoia.\nMensagem: %s' % (nome, email, mensagem))

    return "<p>Obrigada pelo apoio!</p>"

run(host='localhost', port=8081, debug=True)
