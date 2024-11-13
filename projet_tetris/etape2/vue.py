import tkinter
import modele

DIM=30
COULEURS = ["red","blue","green","yellow","orange","purple","pink","dark grey","black"]

class VueTetris():
    """
    classe pour construire le visuel d'un tetris
    """
    def __init__(self,mod_tetris):
        """VueTetris,ModeleTetris->None
        constructeur du visuel du tetris
        """
        self.__modele=mod_tetris
        self.__fen=tkinter.Tk()
        self.__fen.title("tetris")
        self.__can_terrain=tkinter.Canvas(self.__fen,width=DIM*mod_tetris.get_largeur(),height=DIM*mod_tetris.get_hauteur())
        self.__can_terrain.pack(side="left")
        col=[]
        for i in range(mod_tetris.get_largeur()):
            li=[]
            for j in range(mod_tetris.get_hauteur()):
                rect=self.__can_terrain.create_rectangle((i*DIM),(j*DIM),((i+1)*DIM),((j+1)*DIM),fill=COULEURS[self.__modele.get_valeur(j,i)],outline="grey",width=2)
                li.append(rect)
            col.append(li)
        self.__les_cases=col
        fram=tkinter.Frame(self.__fen)
        fram.pack(side="right")
        btn_quitter = tkinter.Button(fram, text="Quitter", command = self.__fen.destroy)
        btn_quitter.pack()
        
    def fenetre(self):
        """VueTetris->Tk
        retourne l’instance de Tk de l’application
        """
        return self.__fen
        
    def dessine_case(self,i,j,col):
        """VueTetris,int,int,int->None
        remplit la case en ligne i et en colonne j de la couleur a l’indice col
        """
        self.__can_terrain.itemconfigure(self.__les_cases[i][j],fill=COULEURS[col])
        
    def dessine_terrain(self):
        """VueTetris->None
        met à jour la couleur de tout le terrain en fonction des valeurs du modèle
        """
        for i in range(self.__modele.get_largeur()):
            for j in range(self.__modele.get_hauteur()):
                self.dessine_case(i,j,self.__modele.get_valeur(j,i))
        
        
    def dessine_forme(self,coord,couleur):
        """VueTetris->None
        remplit de couleur les cases dont les coordonnées sont données dans coords
        """
        for coor in coord:
            self.dessine_case(coor[0],coor[1],couleur)
        
        