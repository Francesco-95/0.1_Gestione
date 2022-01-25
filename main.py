import tkinter as tk

class Main:
    def __init__(self, root):
        # --- Finestra Principale ---
        self.window= root
        self.window.title("Gestionale")
        Icona= tk.PhotoImage(file="C:\\Users\\cicci\\Desktop\\Francesco\\python\\1.Prova_Gestionale\\Icone\\icona.png")
        self.window.iconphoto (True, Icona )
        self.font= ("Calibrì", 13)

        # --- Frame menu grafico ---
        self.F_menu= tk.Frame(self.window)
        self.menu_imag= self.MenuImg(self.F_menu)
        self.F_menu.pack()

        # --- Frame menu grafico ---
        self.F_corpo= tk.Frame(self.window)
        self.corpo= self.Home(self.F_corpo)
        self.F_corpo.pack()

    # --- Menu Grafico ----
    def MenuImg (self, root):
        self.window=root
        # --- Pulsante Clienti ---
        self.img_clienti=tk.PhotoImage(file="C:\\Users\\cicci\\Desktop\\Francesco\\python\\1.Prova_Gestionale\\Icone\\clienti.png")
        self.btnClienti= tk.Button(self.window)
        self.btnClienti.configure(image=self.img_clienti, cursor="hand2")
        self.btnClienti.pack(side=tk.LEFT)
        
        self.img_preconti=tk.PhotoImage(file="C:\\Users\\cicci\\Desktop\\Francesco\\python\\1.Prova_Gestionale\\Icone\\preconti.png")
        self.btnPreconti=tk.Button(self.window)
        self.btnPreconti.configure(image=self.img_preconti, cursor="hand2")
        self.btnPreconti.pack(side=tk.LEFT)

    # --- Home ----
    def Home (self, root):
        self.window=root

        self.L1=tk.Label(self.window, text="CORPO")
        self.L1.pack()


if __name__ == "__main__":
    window = tk.Tk()
    pt = Main (window)
    window.mainloop()
