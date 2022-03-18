from random import random
class Individu:
    def __init__(self, x_position, y_position, pourcentage_porteur = 0.10):
        self.position = (x_position, y_position)
        self.etat_contamination = self.creer_etat_contamination(pourcentage_porteur)
        self.date_contamination = 0
        #0 il n'est pas contaminé, 1 contaminé non reconnu, 2 contaminé reconnu
        self.immunite = False
        self.etat_physique = self.creer_etat_physique()
        self.degre_contagiosite = 0
        self.derogation = self.creer_derogation()
        self.porteur_sain = False
        self.vaccine = False
        self.date_contamination = None
        self.mort = False
        
    def creer_etat_physique(self):
        """
        fonction qui crée l'état physique de la personne selon les statistiques du cahier des charges
        """
        etat = random()
        if etat <= 0.35:
            self.etat_physique = 5
        elif 0.36 <= etat <= 0.70:
            self.etat_physique = 4
        elif 0.71 <= etat <= 0.85:
            self.etat_physique = 3
        elif 0.86 <= etat <= 0.90:
            self.etat_physique = 2
        else:
            self.etat_physique = 1
        return self.etat_physique
            
    def creer_derogation(self):
        """
        fonction qui crée la dérogation de la personne selon son etat physique
        """
        derog = random()
        if self.etat_physique > 2 :
            if derog <= 0.1:
                self.derogation = True
            else:
                self.derogation = False
        else:
            self.derogation = False
        return self.derogation
    
    def creer_etat_contamination(self, pourcentage_porteur):
        """
        fonction qui crée l'état physique de la personne selon les statistiques du cahier des charges
        """
        if random() <= pourcentage_porteur:
            self.etat_contamination = 1
            self.date_contamination = 0
        else:
            self.etat_contamination = 0
        return self.etat_contamination

    def X(self):
        """
        fonction qui renvoie la coordonnée x du personnage
        """
        return self.position[0]
    
    def Y(self):
        """
        fonction qui renvoie la coordonnée y du personnage
        """
        return self.position[1]
   
        