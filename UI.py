from tkinter import *
import Game
import IA


class UIJ:
    def __init__(self):
        self.jeu = Game.GameJ()
        self.fen = Tk()
        self.fen.eval('tk::PlaceWindow . center')
        self.fen.title('TEEKO')
        self.can = Canvas(self.fen, height=500, width=500)
        self.niveau = 0
        self.slider = Scale(self.fen, from_=0, to=2, orient=HORIZONTAL, length=300, sliderlength=40, showvalue=False)
        self.ia = IA.Ia(self.jeu, -1, 1)

    def menu(self):
        lab = Label(self.fen,
                    text="Bienvenue sur le projet TEEKO d'IA41 de" + '\n' + "Youssef , David , Nisrine et Mouad",
                    font=('Arial', 16, 'bold'))
        lab.pack(side=TOP, padx=15, pady=15)  # On crée une étiquette (un texte) de presentation

        bou1 = Button(self.fen, text='Joueur VS Joueur', font=('Arial', 15, 'normal'), padx=25, pady=5,
                      command=self.jeuUIsolo)
        bou1.pack(side=LEFT, padx=10, pady=4)  # On crée un bouton pour lancer une partie Joueur contre Joueur

        bou2 = Button(self.fen, text='Joueur VS Ordinateur', font=('Arial', 15, 'normal'), padx=10, pady=5,
                      command=self.selectIA)
        bou2.pack(side=RIGHT, padx=10, pady=4)

        bou3 = Button(self.fen, text='Ordinateur VS Ordinateur', font=('Arial', 15, 'normal'), padx=10, pady=5,
                      command=self.selectIA)
        bou3.pack(side=RIGHT, padx=10, pady=4)

        self.fen.mainloop()

    def selectIA(self):
        liste = self.fen.pack_slaves()
        for i in range(len(liste)):
            liste[i].destroy()
        lab = Label(self.fen,text="Choisissez votre difficulté",font=('Arial', 16, 'bold'))
        lab.pack(side=TOP, padx=15, pady=15)

        fen_lab = Frame(self.fen)

        lab1 = Label(fen_lab, text="Très facile",font=('Arial', 12), padx=15)
        lab2 = Label(fen_lab, text="Facile",font=('Arial', 12), padx=15)
        lab3 = Label(fen_lab, text="Normal",font=('Arial', 12), padx=15)
        lab4 = Label(fen_lab, text="Difficile",font=('Arial', 12), padx=15)
        lab1.pack(side=LEFT)
        lab2.pack(side=LEFT)
        lab3.pack(side=LEFT)
        lab4.pack(side=LEFT)

        fen_lab.pack()

        self.slider.pack()

        bou = Button(self.fen, text='Confirmer', font=('Arial', 15, 'normal'), padx=25, pady=5,
                     command=self.jeuUIia)
        bou.pack(side=BOTTOM, padx=10, pady=4)

    def jeuUIsolo(self):
        liste = self.fen.pack_slaves()
        for i in range(len(liste)):
            liste[i].destroy()
        self.can.pack()
        self.terrain()
        self.can.focus_set()
        self.can.bind('<Button-1>', self.clique)

    def clique(self, event):
        x = int(event.x / 100)
        y = int(event.y / 100)
        if (self.jeu.phase == 'Mettre'):
            self.jeu.mettrePions(x, y)
        elif self.jeu.phase == 'movePrendre':
            self.jeu.movePionsPrendre(x, y)
        elif self.jeu.phase == 'movePoser':
            self.jeu.movePionsPoser(x, y)
        self.update()

    def jeuUIia(self):
        self.niveau = self.slider.get()
        liste = self.fen.pack_slaves()
        for i in range(len(liste)):
            liste[i].destroy()
        self.can.pack()
        self.terrain()
        self.can.focus_set()
        self.can.bind('<Button-1>', self.cliqueIA)

    def cliqueIA(self, event):
        x = int(event.x / 100)
        y = int(event.y / 100)
        if (self.jeu.phase == 'Mettre'):
            self.jeu.mettrePions(x, y)
        elif self.jeu.phase == 'movePrendre':
            self.jeu.movePionsPrendre(x, y)
        elif self.jeu.phase == 'movePoser':
            self.jeu.movePionsPoser(x, y)
        self.update()
        if self.jeu.phase != 'movePrendre':
            if self.niveau == 0:
                self.ia.niveauFacile()
        self.update()

    def terrain(self):
        for i in range(5):
            for j in range(5):
                self.can.create_oval(10 + (i * 100), 10 + (j * 100), 90 + (i * 100), 90 + (j * 100), width=5,
                                     outline='black')

    def update(self):
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
