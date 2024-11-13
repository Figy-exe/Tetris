from random import randint

LES_FORMES=[[(0,-1),(0,0),(0,1),(0,2)],[(0,-1),(0,0),(1,-1),(1,0)],[(-1,0),(0,0),(0,-1),(1,-1)],\
            [(-1,-1),(0,-1),(0,0),(1,0)],[(-1,1),(-1,0),(0,0),(1,0)],[(-1,0),(0,0),(1,0),(1,1)],[(-1,0),(0,0),(1,0),(0,-1)]]

class ModeleTetris():
    """
    classe pour construire le modele du tetris
    """
    def __init__(self,lig=20,col=14):
        """ModeleTetris,int,int-> None
        constructeur du modele du tetris
        """
        self.__haut=lig+4
        self.__larg=col
        self.__base=4
        colo=[]
        for i in range(self.__haut):
            lign=[]
            for j in range(self.__larg):
                if i<4:
                    lign.append(-2)
                else:
                    lign.append(-1)
            colo.append(lign)
        self.__terrain=colo
        self.__forme = Forme(self)
        self.__suivant=Forme(self)
        
        
    def get_largeur(self):
        """ModeleTetris->int
        retourne la largueur du tetris
        """
        return self.__larg
    
    def get_hauteur(self):
        """ModeleTetris->int
        retourne la hauteur du tetris
        """
        return self.__haut
    
    def get_valeur(self,lig,col):
        """ModeleTetris,int,int->int
        retourne la valeur de la case dont les coordonées sont en paramètre
        """
        return self.__terrain[lig][col]
        
    def est_occupe(self,lig,col):
        """ModeleTetris,int,int->bool
        retourne la valeur si la case dont les coordonées sont en paramètre est occupé
        """
        return (self.get_valeur(lig,col)>=0)
        
    def fini(self):
        """ModeleTetris->bool
        retourne si le jeu de tetris est terminé ou non
        """
        for i in range(self.__larg):
            if self.__terrain[self.__base][i]!=-1:
                return True
        return False
    
    def ajoute_forme(self):
        """ModeleTetris-> None
        ajoute une forme sur le tetris
        """
        for coord in self.__forme.get_coords():
            self.__terrain[coord[1]][coord[0]]=self.__forme.get_couleur()
    
    def forme_tombe(self):
        """ModeleTetris->bool
        fait tomber self.__forme. Si elle n’est pas tombee
        (il y a eu collision), alors self.__forme est ajoutêe sur le terrain,
        et self.__forme est reinitialisé à une nouvelle forme.
        Cette mèthode retourne vrai s’il y a eu collision, faux sinon 
        """
        if not(self.__forme.tombe()):
            self.ajoute_forme()
            self.__forme = Forme(self)
            self.__forme = self.__suivant
            self.__suivant = Forme(self)
            return False
        return True
    
    
    def get_couleur_forme(self):
        """ModeleTetris->int
        retourne la couleur de self.__forme
        """
        return self.__forme.get_couleur()
    
    def get_coords_forme(self):
        """ModeleTetris->list(tuple(int))
        retourne les coordonnées absolues de self.__forme
        """
        return self.__forme.get_coords()
    
    def forme_a_gauche(self):
        """ModeleTetris->None
        décale la forme vers la gauche
        """
        self.__forme.a_gauche()

    
    def forme_a_droite(self):
        """ModeleTetris->None
        décale la forme vers la droite
        """
        self.__forme.a_droite()
    
    def forme_tourne(self):
        """ModeleTetris->None
        fait tourner la forme
        """
        self.__forme.tourne()
    
class Forme():
    """
    classe pour construire une forme de tetris
    """
    def __init__(self,mod_tetris):
        """Forme,ModeleTetrisNone
        initialisateur d'une forme de tetris
        """
        self.__modele=mod_tetris
        self.__couleur=randint(0,6)
        self.__forme= LES_FORMES[self.__couleur]
        self.__x0=randint(2,self.__modele.get_largeur()-2)
        self.__y0=0
    
    def get_couleur(self):
        """Forme->int
        retourne la couleur de la forme
        """
        return self.__couleur
    
    def get_coords(self):
        """Forme->list(tuple(int))
        retourne une liste de couples (int,int) representant
        les coordonnées absolues de la forme sur le terrain du modèle
        """
        res=[]
        for coord in self.__forme:
            res.append((coord[0]+self.__x0,coord[1]+self.__y0))
        return res
        
    def collision(self):
        """Forme->bool
        retourne vrai si la forme doit se poser, faux sinon.
        Il y a collision lorsque pour l’une des coordonnees absolues de la forme,
        soit est arrivé sur la dernière ligne la plus basse du terrain,
        soit est sur une cellule juste au-dessus d’une cellule occupée sur le terrain
        """
        for case in self.get_coords():
            if case[1]>=self.__modele.get_hauteur()-1 or (self.__modele.est_occupe(case[1]+1,case[0])):
                return True
        return False

        
    
    def tombe(self):
        """Forme->bool
        fait tomber d’une ligne la forme s’il n’y a pas collision
        """
        if not(self.collision()):
            self.__y0 += 1
            return True
        else:
            return False
                
    def position_valide(self):
        """Forme->bool
        vérifie si la position de la forme sur le terrain est valide
        """
        for coord in self.get_coords():
            if coord[1] < 0 or coord[1] >= self.__modele.get_hauteur():
                return False
            if coord[0] < 0 or coord[0] >= self.__modele.get_largeur():
                return False
            if self.__modele.est_occupe(coord[1],coord[0]):
                return False
        return True
        
    def a_gauche(self):
        """Forme->None
        décale la forme vers la gauche
        """
        self.__x0-=1
        if not self.position_valide():
            self.__x0+=1
        
    def a_droite(self):
        """Forme->None
        décale la forme vers la droite
        """
        self.__x0+=1
        if not self.position_valide():
            self.__x0-=1
    
    def tourne(self):
        """Forme->None
        fait tourner la forme
        """
        forme_prec=self.__forme
        self.__forme=[]
        for coord in forme_prec:
            self.__forme.append((-coord[1],coord[0]))
        if not self.position_valide():
            self.__forme=forme_prec
        
        
        
        
        
        