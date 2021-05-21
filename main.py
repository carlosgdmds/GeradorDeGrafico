from matplotlib.pyplot import title, xlabel,ylabel,plot,show
from tkinter import *

class Inicia():
    def __init__(self):
        self.root = Tk()
        self.root.title('Gerador de grafico')
        self.root.geometry("800x500")
        self.azul = '#00BFFF'
        self.root['bg'] = self.azul

        #variveis para o grafico
        self.gcampox = ""
        self.gcampoy = ""
        self.listadadosx = []
        self.listadadosy = []
        
        #parametros do lado x e y do grafico
        self.branco = 'white'
        self.lCampox = Label(self.root, text="Digite o campo x",bg=self.azul, fg=self.branco)
        self.lCampoy = Label(self.root, text="Digite o campo y",bg=self.azul, fg=self.branco)

        self.entCampox = Entry(self.root)
        self.entCampoy = Entry(self.root)

        #dados do lados x e y
        self.lDadosx = Label(self.root, text="Digite os dados para o campo  ",bg=self.azul, fg=self.branco)
        self.lDadosy = Label(self.root, text="Digite os dados para o campo  ",bg=self.azul, fg=self.branco)

        self.entDadosx = Entry(self.root,width=30)
        self.entDadosy = Entry(self.root,width=30)


        #botoes
        self.btnAddcampo = Button(self.root, text="Adicionar Campos", command=self.AddCampo)

        self.btnAdddados = Button(self.root, text="Adicionar Dados", command=self.Adddados)

        self.btnGerargrafico = Button(self.root, text="Gerar Grafico", command=self.Geragrafico)

        self.lista = Listbox(self.root,width=85, height=20)
        self.lbErro = Label(self.root, text="", bg=self.azul, fg=self.branco)
        self.empacota()
        self.root.mainloop()
        
    def Geragrafico(self):
        title('grafico')
        xlabel(self.gcampox)
        ylabel(self.gcampoy)
        plot(self.listadadosx, self.listadadosy)
        show()

    def Adddados(self):
        dadosx = self.entDadosx.get()
        dadosy = self.entDadosy.get()
        if len(dadosx) > 0 and len(dadosy) > 0:
            self.listadadosx.append(dadosx)
            self.listadadosy.append(dadosy)
            self.dadoslista = str(dadosx) +(" "*10) + str(dadosy)
            self.lista.insert(END, self.dadoslista)
            self.entDadosx['text'] = ''
            self.entDadosy['text'] = ''
        else:
            self.lbErro['text']= "informacao x ou informacao y vazio"

    def AddCampo(self):
        campox = self.entCampox.get()
        campoy = self.entCampoy.get()
        if len(campox) > 0 and len(campoy) > 0:
            self.gcampox = campox
            self.gcampoy = campoy
            self.camposlista = campox + (" "* 10) + campoy
            self.lista.insert(END,self.camposlista)

            self.lDadosx['text'] = 'Digite os dados para o campo ' + campox
            self.lDadosy['text'] = 'Digite os dados para o campo ' + campoy
         
        else:
            self.lbErro['text'] = 'Campo x ou campo y vazio'

    def empacota(self):
        
        self.lCampox.place(x=15,y=10)
        self.lCampoy.place(x=150,y=10)
        
        self.entCampox.place(x=15,y=40)
        self.entCampox.focus_set()
        self.entCampoy.place(x=150,y=40)


        self.lDadosx.place(x=15,y=80)
        self.lDadosy.place(x=350,y=80)

        self.entDadosx.place(x=15,y=120)
        self.entDadosy.place(x=350,y=120)

        self.btnAddcampo.place(x=650,y=40)
        self.btnAdddados.place(x=650,y=120)
    
        self.btnGerargrafico.place(x=650,y=300)
        self.lista.place(x=10,y=160)

        self.lbErro.place(x=600,y=400)
 
if __name__=="__main__":
    Inicia()
