import random
from random import randint
from random import choice
from classe_Individu import *
from classe_monde import *
class Evolution:
    def __init__(self, cycle : int, confinement : int, larg, long, pc_porteurs):
        self.cycle = cycle
        self.coeff = 0.05
        self.confinement = confinement
        self.monde1 = Univers(larg, long, pc_porteurs)

                         
    def changer_etat(self, new_etat) :
        """
        fonction qui change l'état du confinement quand on le souhaite
        """
        self.confinement = new_etat
        
    
    def deplacement_individu(self):
        """
        fonction qui gère le déplacement des individus en prenant en compte si il y a un confinement 
        """
        if self.confinement == 0:
            for indiv in self.monde1.liste_personnages:
                nb_deplacement = randint(1, 7)
                for _ in range(nb_deplacement):
                    self.choisir_case(indiv.X(), indiv.Y(), indiv, self.rechercher_cases_vides(indiv.X(), indiv.Y()))
                    self.conta_personne_alentours(indiv, indiv.X(), indiv.Y())
        else:
            for indiv in self.monde1.liste_personnages: 
                if indiv.derogation:
                    nb_deplacement = indiv.etat_physique
                    for _ in range(nb_deplacement):
                        self.choisir_case(indiv.X(), indiv.Y(), indiv, self.rechercher_cases_vides(indiv.X(), indiv.Y()))
                        self.conta_personne_alentours(indiv, indiv.X(), indiv.Y())
                else:
                    if self.confinement == 1:
                        for _ in range(2):
                            self.choisir_case(indiv.X(), indiv.Y(), indiv, self.rechercher_cases_vides(indiv.X(), indiv.Y()))
                            self.conta_personne_alentours(indiv, indiv.X(), indiv.Y())
                    if self.confinement == 2:
                        for _ in range(1):
                            self.choisir_case(indiv.X(), indiv.Y(), indiv, self.rechercher_cases_vides(indiv.X(), indiv.Y()))
                            self.conta_personne_alentours(indiv, indiv.X(), indiv.Y())
                        
                        
                        
                    
    def choisir_case(self, x, y, indiv, liste_cases_vides):
        """
        choisi aléatoirement une case de déplacement parmi celle vide
        """
        if liste_cases_vides == []:
            return (x,y)
        else:
            case = choice(liste_cases_vides)
            indiv.position = case
            self.monde1.grille[x][y] = 0
            self.monde1.grille[case[0]][case[1]] = indiv
            return case
        
        
    def rechercher_cases_vides(self, x: int , y: int) -> list:
        """
        renvoie une liste de cases vides à une distance de 1 autour de la position x,y
        """
        cases_possibles = []
        if y +1< self.monde1.longueur and self.monde1.grille[x][y+1] == 0:
            cases_possibles.append((x,y+1))
        if y > 0 and self.monde1.grille[x][y-1] == 0:
            cases_possibles.append((x,y-1))
        if x +1 < self.monde1.longueur and self.monde1.grille[x+1][y] == 0:
            cases_possibles.append((x+1,y))
        if x > 0 and self.monde1.grille[x-1][y] == 0:
            cases_possibles.append((x-1,y))
        return cases_possibles

    
    def conta_personne_alentours(self, individu_contamine, x, y):
        """
        fonction qui contamine les personnes aux alentours avec les personnes contaminé en déplacement
    
        """
        if individu_contamine.etat_contamination >= 1:
            if x < self.monde1.longueur - 1 and self.monde1.grille[x + 1][y] != 0:
                if self.proba_devenir_contamine(self.coeff):
                    self.modif_date_contamination(self.monde1.grille[x + 1][y])
            if y < self.monde1.largeur - 1and self.monde1.grille[x][y + 1] != 0:
                if self.proba_devenir_contamine(self.coeff):
                    self.modif_date_contamination(self.monde1.grille[x][y + 1])
            if x > 0 and self.monde1.grille[x - 1][y] != 0:
                if self.proba_devenir_contamine(self.coeff):
                    self.modif_date_contamination(self.monde1.grille[x - 1][y])
            if y > 0 and self.monde1.grille[x][y - 1] != 0:
                if self.proba_devenir_contamine(self.coeff):
                    self.modif_date_contamination(self.monde1.grille[x][y - 1])
            if x < self.monde1.longueur - 1 and y < self.monde1.largeur - 1 and self.monde1.grille[x + 1][y + 1] != 0:
                if self.proba_devenir_contamine(self.coeff):
                    self.modif_date_contamination(self.monde1.grille[x + 1][y + 1])
            if x < self.monde1.longueur - 1 and y > 0 and self.monde1.grille[x + 1][y - 1] != 0:
                if self.proba_devenir_contamine(self.coeff):
                    self.modif_date_contamination(self.monde1.grille[x + 1][y - 1])
            if x > 0 and y < self.monde1.largeur - 1 and self.monde1.grille[x - 1][y + 1] != 0:
                if self.proba_devenir_contamine(self.coeff):
                    self.modif_date_contamination(self.monde1.grille[x - 1][y + 1])
            if x > 0 and y > 0 and self.monde1.grille[x - 1][y - 1] != 0:
                if self.proba_devenir_contamine(self.coeff):
                    self.modif_date_contamination(self.monde1.grille[x - 1][y - 1])
    
    
    def modif_date_contamination(self, personne):
        """
        fonction qui modifie la date de contamination et son etat de contamination si la personne n'a jamais eu le virus
        """
        if personne.date_contamination == None:
            personne.date_contamination = self.cycle
            personne.etat_contamination = 1
    
    
    def proba_devenir_contamine(self, coeff):
        """
        la personne devient contaminé si elle rentre dans le pourcentage de personne contaminée
        """
        return random() <= coeff
    
    
                    
    #les méthodes suivantes vont faire évoluer la contamination, l'évolution physique, la contagiosité et la dérogation et la positivité des personnes
    def evolution_phy(self):
        """
        gère la condition physique des individus s'ils sont contaminés par le virus
        la période moyenne d'incubation du covid est de 5 jours
        """
        for individu in self.monde1.liste_personnages:
            if individu.date_contamination != None:
                if individu.etat_contamination >= 1 and individu.date_contamination + 5 == self.cycle:
                    if individu.etat_physique == 5:
                        porteur_sain = random()
                        if 0.4 <= porteur_sain <= 1:
                            degre_degradation_phy = random()
                            if degre_degradation_phy <= 0.2:
                                individu.etat_physique = 3
                            else:
                                individu.etat_physique = 4
                        else:
                            individu.porteur_sain = True
                    else:
                        degre_degradation_phy = random()
                        if degre_degradation_phy <= 0.2:
                            individu.etat_physique = individu.etat_physique - 2
                        else:
                            individu.etat_physique = individu.etat_physique - 1
                       
    def evolution_conta(self):
        """
        chaque individu contaminés a une chance de 5 d'être testé positif à chaque cycle 
        """
        for individu in self.monde1.liste_personnages:
            if individu.etat_contamination >= 1:
                chance = random()
                if chance <= 0.2:
                    individu.etat_contamination = 2
    
    def contagiosite(self):
        """
        gère le degrès de contamination pour les personnes atteinte du virus grâce à leur date de contamination
        """
        for individu in self.monde1.liste_personnages:
            if individu.etat_contamination >= 1 and individu.date_contamination != None:
                if individu.date_contamination != 0:
                    if individu.date_contamination + 5 > self.cycle:
                        individu.degre_contagiosite = 0
                    if individu.date_contamination + 15 > self.cycle:
                        individu.degre_contagiosite = 2
                    if individu.date_contamination + 25 > self.cycle:
                        individu.degre_contagiosite = 1
                    else:
                        individu.immunite = True
                        individu.degre_contagiosite = 0
                        individu.etat_contamination = 0
                else:
                    individu.date_contamination = self.cycle
                    
    def evolution_derogation(self):
        """
        retire la derogation d'une personne si celle ci vient à ne plus en avoir la permission
        """
        for individu in self.monde1.liste_personnages:
            if individu.etat_physique < 2 and individu.etat_contamination != 0:
                individu.derogation = False
                    
                    
                    
            
    #La méthode ci dessous va servir de nettoyer la grille des personnes mortes
    def personne_morte(self):
        """
        enlève de la grille les personnes mortes
        """
        for individu in self.monde1.liste_personnages:
            if individu.etat_physique == 0 and individu.mort == False:
                individu.mort = True
                self.monde1.grille[individu.X()][individu.Y()] = 0
                self.monde1.nb_mort += 1
     
    #la méthode ci dessous va appliquer à partir du 300e jour le programme de vaccination massive        
    def vaccination(self):
        """
        programme de vaccination à partir du 300e jour de vie avec le virus et programme s'appliquant progressivement
        suivant la condition physique de la personne
        """
        if self.cycle >= 300:
            for individu in self.monde1.liste_personnages:
                if 300 <= self.cycle <= 399:
                    if individu.etat_physique <= 2 and individu.etat_contamination == 0:
                        individu.vaccine = True
                elif 400 <= self.cycle <= 449:
                    if individu.etat_physique == 3 and individu.etat_contamination == 0:
                        individu.vaccine = True
                elif 450 <= self.cycle <= 499:
                    if individu.etat_physique == 4 and individu.etat_contamination == 0:
                        individu.vaccine = True
                else:
                    if individu.etat_contamination == 0:
                        individu.vaccine = True
    

    def jour_suivant(self):
        """
        passe au jour d'apres
        """
        self.cycle += 1
                
                
                
            
            
                
        