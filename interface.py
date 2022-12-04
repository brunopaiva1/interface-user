from PySimpleGUI import PySimpleGUI as sg #biblioteca para interface do python

#layout
sg.theme('DarkPurple6') #tema 

layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20, 1))], #layout definido para o usuario
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20,1))],
    [sg.Text('Email'), sg.Input(key='email', size=(20, 1))], #layout definido para senha
    [sg.Checkbox('Deseja salvar as informações de login?')], #checkbox definido para salvar informações de login
    [sg.Button('Login')] #butão definido para login
]

#janela
janela = sg.Window('Tela de login', layout) #tela de login

#ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED: #fechando janela
        break
    if eventos == 'Login':
        if valores['usuario'] == 'brunopaiva' and valores['senha'] == 'python3' and valores['email'] == 'brunopaiva@python.com': #se o usuario for o solicitado ira imprimir o testo ta linha a seguir
            print('Seja Bem-Vindo!')
