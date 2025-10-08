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
        self.tubes[tube-1].empile(balle)
    
    def deplace_balle(self, tube1, tube2):
        """déplacer une balle d'un tube à un autre"""
        self.tubes[tube2-1].empile(self.tubes[tube1-1].depile())
    
    def est_gagnant(self):
        """renvoie un booléen pour savoir si le jeu est gagnant"""
        n = 0
        for i in range(6):
            print(i)
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
    def __init__(self, p):
        """créer un nouveau jeu"""
        self.plateau = p
    
    def initialise_plateau(self):
        """initialise un plateau avec des tubes avec des balles de couleurs"""
        p = Plateau()
        liste_balles_couleur = ['R','R','R','R','B','B','B','B','J','J','J','J','V','V','V','V',]
        random.shuffle(liste_balles_couleur)
        for i in range(4):
            for j in range(4):
                p.mettre_dans(Balle(liste_balles_couleur[j]), i)
                liste_balles_couleur.pop(j)
        return p
        
        
    def deplace(self, p, d, a):
        """déplace une balle d'un tube à un autre"""
        p.deplace(d, a)
        
p = Plateau()
p.mettre_dans( Balle("R") ,1)
p.mettre_dans( Balle("R") ,1)
p.mettre_dans( Balle("R") ,1)
p.mettre_dans( Balle("R") ,1)
p.mettre_dans( Balle("V") ,4)
p.mettre_dans( Balle("J") ,2)
p.mettre_dans( Balle("B") ,3)
p.mettre_dans( Balle("V") ,4)
p.mettre_dans( Balle("J") ,2)
p.mettre_dans( Balle("B") ,3)
p.mettre_dans( Balle("V") ,4)
p.mettre_dans( Balle("J") ,2)
p.mettre_dans( Balle("B") ,3)
p.mettre_dans( Balle("V") ,4)
p.mettre_dans( Balle("J") ,2)
p.mettre_dans( Balle("B") ,3)
print(p)