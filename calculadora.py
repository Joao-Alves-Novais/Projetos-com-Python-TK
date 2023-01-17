from tkinter import *

class Calculadora:
    
    def __init__(self):
        # Configurações da janela (Criação, titulo e tamanho)
        self.janela = Tk()
        self.janela.title('Calculadora')
        self.janela.resizable(0, 0)

        # Campo onde será inserido os números para cálculo
        self.caixa_texto = Entry(self.janela, width=20, font='arial 30 bold')
        self.caixa_texto.pack()

        # Um quadro para armazenar os botões
        self.quadro = Frame(self.janela)
        self.quadro.pack()

        # Criação dos botões numéricos
        self.botao_1 = Button(self.quadro, text='1', font='arial 20 bold',
                              width=6, height=3, command=lambda:self.click('1'))
        self.botao_2 = Button(self.quadro, text='2', font='arial 20 bold',
                              width=6, height=3, command=lambda:self.click('2'))
        self.botao_3 = Button(self.quadro, text='3', font='arial 20 bold',
                              width=6, height=3, command=lambda:self.click('3'))
        self.botao_4 = Button(self.quadro, text='4', font='arial 20 bold',
                              width=6, height=3, command=lambda:self.click('4'))
        self.botao_5 = Button(self.quadro, text='5', font='arial 20 bold',
                              width=6, height=3, command=lambda:self.click('5'))
        self.botao_6 = Button(self.quadro, text='6', font='arial 20 bold',
                              width=6, height=3, command=lambda:self.click('6'))
        self.botao_7 = Button(self.quadro, text='7', font='arial 20 bold',
                              width=6, height=3, command=lambda:self.click('7'))
        self.botao_8 = Button(self.quadro, text='8', font='arial 20 bold',
                              width=6, height=3, command=lambda:self.click('8'))
        self.botao_9 = Button(self.quadro, text='9', font='arial 20 bold',
                              width=6, height=3, command=lambda:self.click('9'))
        self.botao_0 = Button(self.quadro, text='0', font='arial 20 bold',
                              width=6, height=3, command=lambda:self.click('0'))

        # Criação dos botões aritméticos
        self.botao_adicao = Button(self.quadro, text='+', font='arial 20 bold',
                                   width=6, height=3, command=lambda:self.click('+'))
        self.botao_sub = Button(self.quadro, text='-', font='arial 20 bold',
                                width=6, height=3, command=lambda:self.click('-'))
        self.botao_divisao = Button(self.quadro, text='/', font='arial 20 bold',
                                    width=6, height=3, command=lambda:self.click('/'))
        self.botao_mult= Button(self.quadro, text='*', font='arial 20 bold',
                                width=6, height=3, command=lambda:self.click('*'))
        self.botao_igual = Button(self.quadro, text='=', font='arial 20 bold',
                                  width=6, height=3, command=self.calcular)
        self.botao_limpar = Button(self.quadro, text='C', font='arial 20 bold',
                                   width=6, height=3, command=self.limpar)

        # Organizando e colocando os botões numéricos
        self.botao_1.grid(row=0, column=1)
        self.botao_2.grid(row=0, column=2)
        self.botao_3.grid(row=0, column=3)
        self.botao_4.grid(row=1, column=1)
        self.botao_5.grid(row=1, column=2)
        self.botao_6.grid(row=1, column=3)
        self.botao_7.grid(row=2, column=1)
        self.botao_8.grid(row=2, column=2)
        self.botao_9.grid(row=2, column=3)
        self.botao_0.grid(row=3, column=2)

        # Organizando e colocando os aritméticos em seus lugares        
        self.botao_adicao.grid(row=0, column=4)
        self.botao_sub.grid(row=1, column=4)
        self.botao_divisao.grid(row=2, column=4)
        self.botao_mult.grid(row=3, column=4)
        self.botao_igual.grid(row=3, column=1)
        self.botao_limpar.grid(row=3, column=3)
        
        # Mantém a janela aberta
        self.janela.mainloop()

    # Função que faz os botões aparecerem na caixa de texto
    def click(self, num):
        self.caixa_texto.insert(END, num)

    # Função que apaga os ultimos números digitados
    def limpar(self):
        self.caixa_texto.delete(len(self.caixa_texto.get())-1,END)

    # Função que faz o cálculo 
    def calcular(self):
        resultado = eval(self.caixa_texto.get())
        self.caixa_texto.delete(0, END)
        self.caixa_texto.insert(END, resultado)
