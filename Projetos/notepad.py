import tkinter as tk


# Passo 6 : Desenvolver as funções dos botões
def Botao_Novo():
    campo_texto.delete(1.0, 'end')


def Botao_Salvar():
    container = campo_texto.get(1.0, 'end')
    arquivo = open('Campo de texto.txt', 'w')
    arquivo.write(container)
    arquivo.close


def Botao_Abrir():
    arquivo = open('Campo de texto.txt', 'r')
    container = arquivo.read()
    campo_texto.insert(1.0, container)
    arquivo.close()


def Botao_Mudar():
    fonte = op_fonte.get()
    tamanho = op_tamanho.get()
    campo_texto.config(font='{} {}'.format(fonte, tamanho))


# Passo1: Criar e configurar minha janela
janela = tk.Tk()
janela.title('Notepad')
janela.minsize(height=600, width=400)
janela.geometry('600x400')


# Pass2: Criar barra de formatação (Font e Font Size)
barra = tk.Frame(janela, height=30)
barra.pack(fill='x')

fonte = tk.Label(barra, text='   Fonte:   ')
fonte.pack(side='left')

op_fonte = tk.Spinbox(barra, values=('arial', 'verdana', 'System', 'Times', 'Symbol'))
op_fonte.pack(side='left')

fonte_tamanho = tk.Label(barra, text='   Tamanho da Fonte:   ')
fonte_tamanho.pack(side='left')

op_tamanho = tk.Spinbox(barra, from_=10, to=40)
op_tamanho.pack(side='left')


# Passo 3: Criar botão Update
botao_mudar = tk.Button(barra, text='Mudar', command=Botao_Mudar)
botao_mudar.pack(side='left')


# Passo 4:Criar botão File para opções (Novo, Salvar, Abri e Sair)
file = tk.Menu(janela)
menu = tk.Menu(file, tearoff=0)

menu.add_command(label='Novo', command=Botao_Novo)
menu.add_command(label='Salvar', command=Botao_Salvar)
menu.add_command(label='Abrir', command=Botao_Abrir)
menu.add_command(label='Sair', command=janela.destroy)

file.add_cascade(label='File', menu=menu)
janela.config(menu=file)


# Passo 5: Criar o campo de digitação
campo_texto = tk.Text(janela, font='arial 12', height=600, width=400)
campo_texto.pack()


# Mantém a janela aberta
janela. mainloop()
