from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('DarkPurple6')

layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20,1))],
    [sg.Checkbox('Deseja salvar as informações de login?')],
    [sg.Button('Login')]
]

#janela
janela = sg.Window('Tela de login', layout)

#ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Login':
        if valores['usuario'] == 'brunopaiva' and valores['senha'] == 'python3':
            print('Seja Bem-Vindo!')
