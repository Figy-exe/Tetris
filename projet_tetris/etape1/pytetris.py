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
        self.__delai=320
        self.joue()
        self.__fen.mainloop()
        
        
    def joue(self):
        """Controleur -> None
        boucle principale du jeu. Fait tomber une forme d’une ligne.
        """
        if not self.__tetris.fini():
            self.affichage()
            self.__fen.after(self.__delai,self.joue)
        
            
        
    def affichage(self):
        """Controleur -> None
        le contrôleur indique au module qu’il doit faire tomber la forme,
        puis il demande a la vue de redessiner son terrain,
        puis de redessiner la forme
        """
        self.__tetris.forme_tombe()
        self.__vue.dessine_terrain()
        self.__vue.dessine_forme()
        
        
        
if __name__ == "__main__" :
    # création du modèle
    tetris = modele.ModeleTetris()
    # création du contrôleur. c’est lui qui créé la vue
    # et lance la boucle d’écoute des évts
    ctrl = Controleur(tetris)
    
