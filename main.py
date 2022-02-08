"""****************************************************************************
 1° Prova per la greazione grafica del gestionale.
 Utilizzo libreria TkInter

  Siciliano Francesco il 25/01/2022
****************************************************************************/"""

from cgitb import text
from itertools import tee
import tkinter as tk
import sqlite3 as db
from functools import partial
# partial(funzione, argomento) -> con questa funzione possiamo passare un argomento ad una funzione
#                                  richiamata al click di un pilsante.

class Main:
    def __init__(self, root):
        # --- Finestra Principale ---
        self.window= root
        self.window.title("Gestionale")
        Icona= tk.PhotoImage(file="C:\\Users\\cicci\\Desktop\\Francesco\\python\\1.Prova_Gestionale\\Icone\\icona.png")
        self.window.iconphoto (True, Icona )
        self.FONT= ("Calibrì", 13)

        # --- Frame menu grafico ---
        self.F_menu= tk.Frame(self.window)
        self.menu_imag= self.MenuImg(self.window)
        self.F_menu.pack()

        # --- Frame menu grafico ---
        self.F_corpo= tk.Frame(self.window)
        self.F_corpo.pack()
        # --- Pagine ---
        self.P_clienti= Clienti(root=self.window, app=self, font=self.FONT)

        # --- Barra inferiore
        self.barraInferiore= tk.Frame(self.window)
        self.BR= self.Barra_Inferiore(self.barraInferiore)
        self.barraInferiore.pack(side=tk.BOTTOM, fill=tk.BOTH)

    # --- Menu Grafico ----
    def MenuImg (self, root):
        self.window=root

        self.F_corpo=tk.Frame(self.window)
        # --- Pulsante Clienti ---
        self.img_clienti=tk.PhotoImage(file="C:\\Users\\cicci\\Desktop\\Francesco\\python\\1.Prova_Gestionale\\Icone\\clienti.png")
        self.btnClienti= tk.Button(self.F_corpo, command=self.C_Clienti)
        self.btnClienti.configure(image=self.img_clienti, cursor="hand2")
        self.btnClienti.pack(side=tk.LEFT)
        
        self.img_preconti=tk.PhotoImage(file="C:\\Users\\cicci\\Desktop\\Francesco\\python\\1.Prova_Gestionale\\Icone\\preconti.png")
        self.btnPreconti=tk.Button(self.F_corpo)
        self.btnPreconti.configure(image=self.img_preconti, cursor="hand2")
        self.btnPreconti.pack(side=tk.LEFT)

        self.F_corpo.pack()

    # --- Barra inferriore ---
    def Barra_Inferiore(self, root):
        self.window=root
        font=("Calibrì", 7)
        self.F_BI= tk.Frame(self.window)
        #   Creiamo la stringa da usare nella barra inferiore
        self.stato = tk.StringVar()
        self.stato.set ("Gestionale - 0.1 Ms.Bianco_PROGRAMMER")
        #   Creiamo l'etichetta per la visualizzazione della stringa
        label = tk.Label (self.F_BI, textvariable= self.stato, fg="black", bg="lightgrey", anchor=tk.E, font=font) #bd=1, relief=tk.SUNKEN, anchor=tk.W
        label.pack(side=tk.BOTTOM, fill=tk.BOTH)

        self.F_BI.pack(side=tk.BOTTOM, fill=tk.BOTH)
        
    # --- Cambio frame ----
    def C_Clienti(self):
        self.F_corpo.pack_forget()  
        self.P_clienti.start()


class Clienti:
    def __init__(self, root, app, font):
        self.window=root
        self.app=app
        self.FONT=font
        self.R=False
        self.sql=''
        self.RR=''

        #   Variabili
        #   Valori del OptionMenu
        self.v=('Cognome Nome', 'Numero cliente','Annulla')
        self.valori=tk.StringVar(self.window)
        self.valori.set("Modalità di ricerca")

        self.F_corpo= tk.Frame(self.window) 
        self.corpo=self.composizione(self.F_corpo)

    # --- Avvio frame ---
    def start(self):
        self.F_corpo.pack() 

    # --- Funzione con i widget
    def composizione(self, root):
        self.window=root
        # Widget
        L_titolo=tk.Label(self.window, text="CLIENTI", font=self.FONT, anchor=tk.N)
        B_AggCliente= tk.Button(self.window, text="Aggiungi Cliente", font=self.FONT, command=self.aggiungi)
        self.E_Ricerca= tk.Entry (self.window, font=self.FONT)        
        self.tipologia= tk.OptionMenu(self.window, self.valori, *self.v)
        B_Ricerca= tk.Button (self.window, text="Ricerca", font=self.FONT, command=self.ricerca)
    
        L_titolo.grid(row=0, columnspan=3, pady=5)
        B_AggCliente.grid(row=1, column=0, padx=5)
        self.E_Ricerca.grid(row=1, column=1, padx=5)
        self.tipologia.grid(row=1,column=2)
        B_Ricerca.grid(row=1, column=3, padx=5)   
  
            
        database= db.connect("C:\\Users\\cicci\\Desktop\\Francesco\\python\\1.Prova_Gestionale\\DB_Lavanderia.db")
        cursor=database.cursor()
        
        if (self.R== False):
            self.sql='SELECT id_cliente,cognome_nome, telefono, punti FROM clienti;'
        else :
            if (self.valori.get()== self.v[0]):
                self.sql="SELECT id_cliente,cognome_nome, telefono, punti FROM clienti WHERE cognome_nome='" + str(self.RR) + "';" 
                self.valori.set("Modalità di ricerca")
                
            if (self.valori.get()== self.v[1]):
                self.sql="SELECT id_cliente,cognome_nome, telefono, punti FROM clienti WHERE id_cliente='" + str(self.RR) + "';" 
                self.valori.set("Modalità di ricerca")

            if (self.valori.get() == self.v[2]):
                self.sql='SELECT id_cliente,cognome_nome, telefono, punti FROM clienti;'
                self.valori.set("Modalità di ricerca")

        cursor.execute(self.sql)
        
        self.frame=tk.Frame (self.window)
        L_tbID_cliente=tk.Label(self.frame, text="Numero cliente", font=self.FONT, anchor=tk.N)
        L_tbDenominazione=tk.Label(self.frame, text="Denominazione ", font=self.FONT, anchor=tk.N)
        L_tbTelefono= tk.Label (self.frame, text="Telefono ", font=self.FONT, anchor=tk.N)
        L_tbPunti= tk.Label (self.frame, text="Punti ", font=self.FONT, anchor=tk.N)

        L_tbID_cliente.grid(row=2, column=0)
        L_tbDenominazione.grid(row=2, column=1, columnspan=2)
        L_tbTelefono.grid(row=2, column=3)
        L_tbPunti.grid(row=2, column=4)
        tela=tk.Canvas(self.frame, width=800, height=1.5)
        tela.config (bg="black")
        tela.grid(row=3, columnspan=7)

        r=4
        for i in cursor.fetchall():
            self.id_clinte= tk.Label(self.frame, text=i[0], font=self.FONT, anchor=tk.N)
            self.denominazione= tk.Label(self.frame, text=i[1], font=self.FONT, anchor=tk.N)
            self.telefono= tk.Label (self.frame, text=i[2], font=self.FONT, anchor=tk.N)
            self.punti= tk.Label (self.frame, text=i[3], font=self.FONT, anchor=tk.N)
            b= tk.Button(self.frame, text="info", command=partial(self.info, i[0]), font=self.FONT)
           
            self.id_clinte.grid(row=r, column=0)
            self.denominazione.grid(row=r, column=1, columnspan=2)
            self.telefono.grid(row=r, column=3)
            self.punti.grid(row=r, column=4)
            b.grid (row=r, column=5)
           
            r=r+1
            self.tela=tk.Canvas(self.frame, width=800, height=1)
            self.tela.config (bg="black")
            self.tela.grid(row=r, columnspan=6)
            r=r+1
        
        self.frame.grid(row=2, columnspan=4)

        database.close()

    def ricerca(self):
        self.R=True
        self.RR=self.E_Ricerca.get()
        self.frame.destroy()
        self.c=self.composizione(self.window)        

    def aggiungi (self):
        self.F_corpo.destroy()
        self.F_corpo.pack()
        l=tk.Label(self.F_corpo, text="Ciao")
        l.grid(row=0, column=0)

    def info (self, indice):
        print (f"hai scelto l'elemento in posizione {indice}")
      

if __name__ == "__main__":
    window = tk.Tk()
    pt = Main (window)
    window.mainloop()
