from tkinter import *
from tkinter import colorchooser
import pyscreenshot

class Paintk:
    def __init__(self):
        
        # Criação e configuração da janela
        self.janela = Tk()
        self.janela.title('PainTk')
        self.janela.minsize(width=1280, height=680)
        self.janela.resizable(0, 0)

        # Estilho de fonte padrão
        self.oval_True = True
        self.linha_True = False

        # Pegando as imagens e colocando nas variáveis para por nos botões
        self.imagem_paleta = PhotoImage(file='C:\\Users\\usuaraio\\Downloads\\Python\icons\\square.png')
        self.imagem_oval = PhotoImage(file='C:\\Users\\usuario\\Downloads\\Python\icons\\oval.png')
        self.imagem_linha= PhotoImage(file='C:\\Users\\usuario\\Downloads\\Python\icons\\line.png')
        self.imagem_borracha = PhotoImage(file='C:\\Users\\usuario\\Downloads\\Python\icons\\eraser.png')
        self.imagem_novo = PhotoImage(file='C:\\Users\\usuario\\Downloads\\Python\icons\\new.png')
        self.imagem_salvar = PhotoImage(file='C:\\Users\\usuario\\Downloads\\Python\icons\\save.png')

        # Criação do local onde ficará a barra de ferramentas
        self.barra = Frame(self.janela, height=80, bg='gray')
        self.barra.pack(fill='x')

        # Criação do texto (Cores)
        self.cores = Label(self.barra, text='   Cores:   ', bg='gray', fg='white')
        self.cores.pack(side='left')

        # Criação e cofiguração dos botões cores
        self.cor_escolhida = 'black' # Black como cor padrão para desenhar
        self.lista_cores = ('black', 'blue', 'red', 'yellow', 'green', 'brown', 'orange', 'pink')
        for i in self.lista_cores:
            self.botao_cor = Button(self.barra, width=4, height=2, bg=i,
                                    command=lambda cor=i:self.troca_cor(cor)).pack(side='left')

        # Criando texto(Paleta de cores)
        self.paleta_cores = Label(self.barra, text='   Paleta de Cores:   ', bg='gray', fg='white')
        self.paleta_cores.pack(side='left')
        
        # Criação do botão de Paleta de cores
        self.botao_paleta = Button(self.barra, image=self.imagem_paleta, width=40, height=40,
                                   bd=0, command=self.paletaDeCores)
        self.botao_paleta.pack(side='left')

        # Criação do texto (Fonte)
        self.fonte = Label(self.barra, text='   Fonte:   ', bg='gray', fg='white')
        self.fonte.pack(side='left')

        # Criação da caixa de tamanho das fontes
        self.tamanhos = Spinbox(self.barra, from_=4, to=40)
        self.tamanhos.pack(side='left')

        # Criação do texto (Ferramentas)
        self.ferramentas = Label(self.barra, text='   Ferramentas:   ', bg='gray', fg='white')
        self.ferramentas.pack(side='left')
        
        # Botões da área Ferramentas
        self.botao_oval = Button(self.barra, image=self.imagem_oval, width=40, height=40, bd=0,
                                 command=self.F_oval)
        self.botao_oval.pack(side='left')
        
        self.botao_linha = Button(self.barra, image=self.imagem_linha, width=40, height=40, bd=0,
                                  command=self.F_linha)
        self.botao_linha.pack(side='left')
        
        self.botao_borracha = Button(self.barra, image=self.imagem_borracha, width=40, height=40,
                                     bd=0, command=self.F_borracha)
        self.botao_borracha.pack(side='left')
        
        self.botao_novo = Button(self.barra, image=self.imagem_novo, width=40, height=40, bd=0,
                                 command=self.novo)
        self.botao_novo.pack(side='left')
        
        self.botao_salvar = Button(self.barra, image=self.imagem_salvar, width=40, height=40,
                                   bd=0, command=self.salvar)
        self.botao_salvar.pack(side='left')

        # Criação da area de desenho
        self.area_desenho = Canvas(self.janela, height=680, bg='white')
        self.area_desenho.pack(fill='both')

        # Faz o mouse desenhar na tela
        self.area_desenho.bind('<B1-Motion>', self.desenhar)
        
        # A tecla (F1) limpar totalmente a tela como atalho
        self.janela.bind('<F1>', self.novo)

        # Mantém a janela funcionando
        self.janela.mainloop()

    # Função que faz o mouse desenha na tela
    def desenhar(self, event):
        x,y = (event.x), (event.y)
        x1, y1 = (event.x), (event.y)

        if self.oval_True:
            self.area_desenho.create_oval(x, y, x1, y1, fill=self.cor_escolhida,
                                          outline=self.cor_escolhida,width=self.tamanhos.get())
        elif self.linha_True:
            self.area_desenho.create_line(x-10, y-10, x1, y1, fill=self.cor_escolhida,
                                          width=self.tamanhos.get())
        else:
            self.area_desenho.create_oval(x, y, x1, y1, fill='white',
                                          outline='white',width=self.tamanhos.get())

    # Função que trocar a cor
    def troca_cor(self, cor):
        self.cor_escolhida = cor

    # Função que abre a aba de paleta de cores
    def paletaDeCores(self):
        cor =colorchooser.askcolor()
        self.cor_escolhida = cor[1]

    # As três funções a seguir define qual das ferramentas esta ativa
    def F_oval(self):
        self.oval_True = True
        self.linha_True = False

    def F_linha(self):
        self.oval_True = False
        self.linha_True = True
    
    def F_borracha(self):
        self.oval_True = False
        self.linha_True = False

    # Limpa a tela de desenho totalmente
    def novo(self, event):
        self.area_desenho.delete('all')

    # Função que salva o desenho como uma imagem .jpeg
    def salvar(self):
        x = self.janela.winfo_rootx() + self.area_desenho.winfo_rootx()
        y = self.janela.winfo_rooty() + self.area_desenho.winfo_rooty()
        x1 = self.janela.winfo_rootx() + self.area_desenho.winfo_width()
        y1 = self.janela.winfo_rooty() + self.area_desenho.winfo_height()
        
        img = pyscreenshot.grab(bbox=(x, y, x1, y1))
        img.save('teste.jpeg', 'jpeg')


Paintk()
