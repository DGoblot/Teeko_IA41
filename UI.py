from tkinter import *
import Game
import IA

class UIJ:
    def __init__(self):#On intitialise l'objet UI
        self.jeu = Game.GameJ()
        self.fen = Tk()
        self.fen.title('TEEKO')
        self.can = Canvas(self.fen, height=500, width=500)
        self.niveau = 0
        self.slider = Scale(self.fen, from_=0, to=2, orient=HORIZONTAL, length=220, sliderlength=40, showvalue=False)
        self.ia1 = IA.Ia(self.jeu, -1, 1)
        self.ia2 = IA.Ia(self.jeu, 1, 1)

    def menu(self):#Fonction créant le menu principal
        lab1 = Label(self.fen, text="TEEKO", font=('Arial', 40, 'bold','italic'))
        lab1.pack()

        lab2 = Label(self.fen,
                    text="Bienvenue sur le projet TEEKO d'IA41 de" + '\n' + "Youssef , David , Nisrine et Mouad",
                    font=('Arial', 16, 'bold'))
        lab2.pack(side=TOP, padx=15, pady=15)  # On crée une étiquette (un texte) de presentation

        bou1 = Button(self.fen, text='Joueur VS Joueur', font=('Arial', 15, 'normal'), padx=25, pady=5,
                      command=self.jeuUI)
        bou1.pack(side=LEFT, padx=10, pady=4)  # On crée un bouton pour lancer une partie Joueur contre Joueur

        bou2 = Button(self.fen, text='Joueur VS Ordinateur', font=('Arial', 15, 'normal'), padx=10, pady=5,
                      command=self.selectIA)
        bou2.pack(side=LEFT, padx=10, pady=4)

        bou3 = Button(self.fen, text='Ordinateur VS Ordinateur', font=('Arial', 15, 'normal'), padx=10, pady=5,
                      command=self.jeuUIia2)
        bou3.pack(side=LEFT, padx=10, pady=4)

        self.fen.mainloop()

    def selectIA(self):#Fonction du bouton 'Joueur contre Ordinateur' qui ouvre la fenêtre de selection de l'IA
        liste = self.fen.pack_slaves()
        for i in range(len(liste)):
            liste[i].destroy()
        lab = Label(self.fen,text="Choisissez votre difficulté",font=('Arial', 16, 'bold'))
        lab.pack(side=TOP, padx=15, pady=15)

        fen_lab = Frame(self.fen)

        lab1 = Label(fen_lab, text="Facile",font=('Arial', 12), padx=15)
        lab2 = Label(fen_lab, text="Normal",font=('Arial', 12), padx=15)
        lab3 = Label(fen_lab, text="Difficile",font=('Arial', 12), padx=15)
        lab1.pack(side=LEFT)
        lab2.pack(side=LEFT)
        lab3.pack(side=LEFT)

        fen_lab.pack()

        self.slider.pack()

        bou = Button(self.fen, text='Confirmer', font=('Arial', 15, 'normal'), padx=25, pady=5,
                     command=self.jeuUIia)
        bou.pack(side=BOTTOM, padx=10, pady=4)

    def jeuUI(self):#Lance le jeu 'Joueur contre Joueur'
        liste = self.fen.pack_slaves()
        for i in range(len(liste)):
            liste[i].destroy()
        self.can.pack()
        self.terrain()
        self.can.focus_set()
        self.can.bind('<Button-1>', self.clique)

    def clique(self, event):#Fonction appelé lorsque l'utilisateur clique sur la fenêtre
        x = int(event.x / 100)
        y = int(event.y / 100)
        if (self.jeu.phase == 'Mettre'):#En fonction de la phase du jeu, on appelle la bonne fonction pour l'intéraction
                                        #avec les jetons et le plateau
            self.jeu.mettrePions(x, y)
        elif self.jeu.phase == 'movePrendre':
            self.jeu.movePionsPrendre(x, y)
        elif self.jeu.phase == 'movePoser':
            self.jeu.movePionsPoser(x, y)
        self.update()#On actualise l'interface aprés chaque coup



    def jeuUIia(self):#Lance le jeu 'Joueur contre Ordinateur'
        self.niveau = self.slider.get()
        liste = self.fen.pack_slaves()
        for i in range(len(liste)):
            liste[i].destroy()
        self.can.pack()
        self.terrain()
        self.can.focus_set()
        self.can.bind('<Button-1>', self.cliqueIA)

    def cliqueIA(self, event):#Fonction appelé lorsque l'utilisateur clique sur la fenêtre
        x = int(event.x / 100)
        y = int(event.y / 100)
        if self.jeu.phase == 'Mettre':
            self.jeu.mettrePions(x, y)
            if self.niveau == 0:#Aprés chaque coup de l'utilisateur, l'IA fait son coup(en fonction de sa difficulté)
                self.ia1.niveauFacile()
            elif self.niveau == 1:
                self.ia1.alphaBeta(2)
            elif self.niveau == 2:
                self.ia1.alphaBeta(4)
        elif self.jeu.phase == 'movePrendre':
            self.jeu.movePionsPrendre(x, y)
        elif self.jeu.phase == 'movePoser':
            if self.jeu.movePionsPoser(x, y):
                if self.niveau == 0:
                    self.ia1.niveauFacile()
                elif self.niveau == 1:
                    self.ia1.alphaBeta(2)
                elif self.niveau == 2:
                    self.ia1.alphaBeta(4)
        self.update()

    def jeuUIia2(self):#Lance le jeu 'Ordinateur contre Ordinateur'
        liste = self.fen.pack_slaves()
        for i in range(len(liste)):
            liste[i].destroy()
        self.can.pack()
        self.terrain()
        self.can.focus_set()
        self.can.bind('<Button-1>', self.cliqueIA2)

    def cliqueIA2(self,event):#Lorsque l'utilisateur clique sur la fenêtre, les deux IA effectues un coup chacunes
        self.ia2.alphaBeta(2)
        self.ia1.alphaBeta(2)
        self.update()

    def terrain(self):#Fonction dessinant le terrain de TEEKO
        for i in range(5):
            for j in range(5):
                self.can.create_oval(10 + (i * 100), 10 + (j * 100), 90 + (i * 100), 90 + (j * 100), width=5,
                                     outline='black')

    def update(self):#Fonction actualisant la vue graphique en fonction du modèle
        self.can.delete('all')
        self.terrain()
        for i in range(5):
            for j in range(5):
                if self.jeu.plateau[i][j] == 1:
                    self.can.create_oval(20 + (i * 100), 20 + (j * 100), 80 + (i * 100), 80 + (j * 100), width=5,
                                         outline='blue', fill='blue')
                if self.jeu.plateau[i][j] == -1:
                    self.can.create_oval(20 + (i * 100), 20 + (j * 100), 80 + (i * 100), 80 + (j * 100), width=5,
                                         outline='red', fill='red')
                if self.jeu.visualisation[i][j] == 1:
                    self.can.create_oval(20 + (i * 100), 20 + (j * 100), 80 + (i * 100), 80 + (j * 100), width=5,
                                         outline='green')

ui = UIJ()
ui.menu()
