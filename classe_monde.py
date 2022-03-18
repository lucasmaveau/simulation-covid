from tkinter import *
from classe_Individu import *
from random import randint

#####################          Définition de la classe Univers

class Univers :
    
    def __init__ (self, longueur = 30, largeur = 30, pc_porteurs =  0.20 ) :  # longueur et largeur
        self.temps = 0
        self.largeur = largeur
        self.longueur = longueur
        self.pc_porteurs = pc_porteurs
        self.nb_initial = (longueur*largeur)*100/pc_porteurs                   
        self.grille = [ [0]* self.largeur for i in range(self.longueur)]
        self.liste_personnages = self.creer_personnages()
        self.nb_mort = 0
                    
    # la fonction qui change l'état du confinement est déjà dans la classe évolution
        
    def creation_personnes(self, liste_perso) :
        larg = randint(0, self.largeur - 1)
        long = randint(0, self.longueur - 1)
        if self.grille[larg][long] == 0:
            personne = Individu(larg, long, self.pc_porteurs)
            self.grille[larg][long] = personne
            liste_perso.append(personne)
        else:
            self.creation_personnes(liste_perso)
        
    def creer_personnages(self):
        nb = (self.largeur * self.longueur) // 4
        liste_perso = []
        for _ in range(nb):
            self.creation_personnes(liste_perso)
        return liste_perso