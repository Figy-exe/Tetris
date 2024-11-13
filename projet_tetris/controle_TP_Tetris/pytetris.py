import vue
import modele

class Controleur():
    """
    classe pour le controle du tetris
    """
    def __init__(self,mod_tetris):
        """
        initialisation du controle du tetris
        """
        self.__tetris=mod_tetris
        self.__vue=vue.VueTetris(self.__tetris)
        self.__fen=self.__vue.fenetre()
        self.__fen.bind("<Key-Left>",self.forme_a_gauche)
        self.__fen.bind("<Key-Right>",self.forme_a_droite)
        self.__fen.bind("<Key-Down>",self.forme_tombe)
        self.__fen.bind("<Key-Up>",self.forme_tourne)
        self.__fen.bind("<Key-a>",self.change_forme)
        self.__delai=320
        self.joue()
        self.__fen.mainloop()
        
        
        
    def joue(self):
        """Controleur -> None
        boucle principale du jeu. Fait tomber une forme d’une ligne.
        """
        if not self.__tetris.fini() and not self.__vue.pause():
            self.affichage()
        elif self.__tetris.fini():
            self.__vue.btn_recommencer()
        self.__fen.after(self.__delai,self.joue)
        
        
        
    def affichage(self):
        """Controleur -> None
        le contrôleur indique au module qu’il doit faire tomber la forme,
        puis il demande a la vue de redessiner son terrain,
        puis de redessiner la forme
        """
        pose=self.__tetris.forme_tombe()
        self.__vue.dessine_terrain()
        self.__vue.dessine_forme(self.__tetris.get_coords_forme(),self.__tetris.get_couleur_forme())
        if not pose:
             self.__delai=320
             self.__vue.dessine_forme_suivante(self.__tetris.get_coords_suivante(),self.__tetris.get_couleur_suivante())
        self.__vue.met_a_jour_score(self.__tetris.get_score())
        
        
    def forme_a_gauche(self,event):
        """
        Controleur,event->None
        décale la forme vers la gauche
        """
        if not self.__vue.pause():
            self.__tetris.forme_a_gauche()
        
    def forme_a_droite(self,event):
        """
        Controleur,event->None
        décale la forme vers la droite
        """
        if not self.__vue.pause():
            self.__tetris.forme_a_droite()
    
    def forme_tombe(self,event):
        """
        Controleur,event->None
        fait tomber la forme plus vite
        """
        if not self.__vue.pause():
            self.__delai=180
    
    def forme_tourne(self,event):
        """Controleur,event->None
        fait tourner la forme
        """
        if not self.__vue.pause():
            self.__tetris.forme_tourne()
        
    def change_forme(self,event):
        """Controleur,event->None
        change la forme si cela a été fait moins de 10 fois durant la partie
        """
        if not self.__vue.pause():
            self.__tetris.forme_change()
        
if __name__ == "__main__" :
    # création du modèle
    tetris = modele.ModeleTetris()
    # création du contrôleur. c’est lui qui créé la vue
    # et lance la boucle d’écoute des évts
    ctrl = Controleur(tetris)
    