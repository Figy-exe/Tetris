import tkinter
import modele

DIM=30
COULEURS = ["red","blue","green","yellow","orange","purple","pink","dark grey","black"]
SUIVANT=6

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
        
        suiv=tkinter.Label(fram,text="Forme suivante :")
        suiv.pack()
        
        self.__can_fsuivante=tkinter.Canvas(fram,width=DIM*SUIVANT,height=DIM*SUIVANT)
        self.__can_fsuivante.pack()
        
        col=[]
        for i in range(SUIVANT):
            li=[]
            for j in range(SUIVANT):
                rect=self.__can_fsuivante.create_rectangle((i*DIM),(j*DIM),((i+1)*DIM),((j+1)*DIM),fill=COULEURS[-1],outline="grey",width=2)
                li.append(rect)
            col.append(li)
        self.__les_suivant=col
        self.dessine_forme_suivante(self.__modele.get_coords_suivante(),self.__modele.get_couleur_suivante())
        
        self.__lbl_score=tkinter.Label(fram, text="Score : 0")
        self.__lbl_score.pack()
        
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
        
    def met_a_jour_score(self,val):
        """
        VueTetris,int->None
        met à jour le score avec la valeur en paramètre
        """
        self.__lbl_score['text']="Score : "+str(val)
        
    def dessinne_case_suivante(self,x,y,coul):
        """
        VueTetris,int,int,int->None
        change la couleur de la case dont les coordonnées sont en paramètre avec la couleur coul
        """
        self.__can_fsuivante.itemconfigure(self.__les_suivant[x][y],fill=COULEURS[coul])
        
    def nettoie_forme_suivante(self):
        """
        VueTetris->None
        remet du noir sur tous les carrés de __can_fsuivante
        """
        for i in range(SUIVANT):
            for j in range(SUIVANT):
                self.dessinne_case_suivante(i,j,-1)
                
    def dessine_forme_suivante(self,coords,coul):
        """
        VueTetris,list(tuple(int)),int->None
        dessine la forme dont les coordonnées et la couleur sont données en paramètre
        """
        self.nettoie_forme_suivante()
        for coord in coords:
            self.__can_fsuivante.itemconfigure(self.__les_suivant[coord[0]+2][coord[1]+2],fill=COULEURS[coul])
        
        
        
        
        
        
            