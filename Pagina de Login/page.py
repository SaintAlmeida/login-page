import PySimpleGUI as psg

layout = [
[psg.Text('Usuário')],
[psg.Input(key='usuario')],
[psg.Text('Senha')],
[psg.Input(key='senha')],
[psg.Button('login')],
[psg.Text(key='mensagem')]

]

window = psg.Window('Login',layout=layout)

while True:
    event, values = window.read()
    
    if event == psg.WIN_CLOSED:
        break
    elif event == 'login':
        senha_cor = 'ALmeida@2022'
        usuario_cor = 'Saint'
        usuario = values['usuario']
        senha = values['senha'] 
        if usuario == usuario_cor and senha == senha_cor:
           window['mensagem'].update('Login Efetuado com Sucesso')
        else:
            window['mensagem'].update('Usuário ou Senha Incorreto')
                   
