#Classes nécessaires
from random import *

class Balle :
    """Classe permettant de créer une balle d'une certaine couleur"""
    
    def __init__(self, c):
        """construit un objet d'une couleur"""
        self.couleur = c
        
    def __str__(self):
        if self.couleur == "R" :
            c = "rouge"
        if self.couleur == "V" :
            c = "vert"
        if self.couleur == "J" :
            c = "jaune"
        if self.couleur == "B" :
            c = "bleue"
        chaine = "balle " + c
        return(chaine)
  
#class Tube qui contient les instances de balles sous forme de tableau gérés comme des piles et possède des methodes pour les gerer
class Tube:
    def __init__(self):
        self.balles = []
        
    def empile(self,e):
        """Empile l'élément e sur pile balles"""
        self.balles.append(e)

    def depile(self):
        """Dépile une pile non vide et retourne le sommet s"""
        s = self.sommet()
        self.balles.pop(len(self.balles)-1)
        return(s)
    
    def sommet(self):
        print(len(self.balles))
        return self.balles[len(self.balles)-1]
    
    
    def est_vide(self):
        """Retourne True si la pile est vide, False sinon"""
        return(self.balles==[])

    def est_plein(self):
        """Retourne True si la pile est pleine (=4), False sinon"""
        return(len(self.balles)==4)
    
    def est_plein_monochrome(self):
        """Retourne True si la pile est pleine (=4) et monochrome, False sinon"""
        if self.est_plein():
            reference = self.balles[0].couleur
            for i in range(4):
                if self.balles[i].couleur != reference:
                    return False
            return True
        return False



    def __str__(self):
        char = ''
        for balle in self.balles:
            char += balle.couleur
        return char
    
class Plateau :
    """Classe permettant d'ajouter des balles dans des tubes, de déplacer des balles d'un tubes à un autre, de vérifier si le jeu est gagnant et d'afficher le plateau"""
    def __init__(self):
        """créer un nouveau plateau"""
        t1 = Tube()
        t2 = Tube()
        t3 = Tube()
        t4 = Tube()
        t5 = Tube()
        t6 = Tube()
        self.tubes = [t1, t2, t3, t4, t5, t6]
        
    def mettre_dans(self, balle, tube):
        """ajouter une balle dans un tube"""
        self.tubes[tube].empile(balle)
    
    
    def deplace_balle(self, tube1, tube2):
        """
        Déplace une balle d'un tube à un autre.

        Codes de retour :
        0 : La balle a bien été déplacée.
        1: Les tubes selectionnés n'existent pas
        2 : Les tubes sont les mêmes.
        3 : Le tube receveur est déjà plein
        4: Vous essayez de deplacer une balle sur une couleur autre que la bonne
        """

                
        if not(self.tubes[tube1].est_vide()): #verifie quele tube de depart n'est pas vide
            bmoved = self.tubes[tube1].sommet()
            color1 = bmoved.couleur #recupere la couleur du sommet du tube de depart
            if not(self.tubes[tube2].est_vide()): #verifie quele tube receveur n'est pas vide ou plein
                if not(self.tubes[tube2].est_plein()): #verifie quele tube receveur n'est pas  plein
                    bmax = self.tubes[tube2].sommet()
                    color2 = bmax.couleur #recupere la couleur du sommet du tube receveur
                    if color2 != color1: #verifie que les couleurs de la balle qu'on veut deplacer et le sommet du tube de depart est identiques
                        return 4
                else:
                    return 3 #si plein retourne le code erreur plein
            
        
        
        if tube1 < 0 or tube2 < 0 or tube1 > 6 or tube2 > 6:
            return 1
   
        if tube1 == tube2:
            return 2
      
        
        """déplacer une balle d'un tube à un autre"""
        self.tubes[tube2].empile(self.tubes[tube1].depile())
        return 0
    
    def est_gagnant(self):
        """renvoie un booléen pour savoir si le jeu est gagnant"""
        n = 0
        for i in range(6):
            if self.tubes[i].est_vide() == True:
                n += 1
            elif self.tubes[i].est_plein_monochrome() == True:
                n += 1
        if n == 6 :
            return True
        else :
            return False
            
    def __str__(self):
        """Affiche le plateau p"""
        chaine = ""
        for i in range(6):
            chaine += str(i+1)
            chaine += " : "
            chaine += str(self.tubes[i])
            chaine += "\n"
        
        return(chaine)

class Jeu :
    """Classe permettant d'initialiser le plateau et de mettre en relation les autres classe pour faire fonctionner le jeu"""
    def __init__(self):
        """créer un nouveau jeu"""
        self.plateau = Plateau()
        self.score = 500
    
    def initialise_plateau(self):
        """initialise un plateau avec des tubes avec des balles de couleurs"""
        p = self.plateau
        liste_balles_couleur = ['R','R','R','R','B','B','B','B','J','J','J','J','V','V','V','V']
        shuffle(liste_balles_couleur)
        for i in range(4):
            for _ in range(4):
                p.mettre_dans(Balle(liste_balles_couleur[0]), i)
                del liste_balles_couleur[0]
        return p
        
        
    def deplace(self, d, a):
        """déplace une balle d'un tube à un autre"""
        code = self.plateau.deplace_balle(d, a)
        if code ==0:
            self.score -=10 #si il n'y a aucune erreur diminue le score de 10
        return code