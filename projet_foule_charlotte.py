#-*- coding: utf-8 -*-
from random import randint,shuffle

##############################
######### CLASSES ###########
############################

class Voyageur:
    def __init__(self,x_entree,y_entree,x_sortie,y_sortie,identifiant):
        '''coordonnées d'entrée (chercher dans la liste des accès) et coordonnées de sortie du voyageur en terme de case'''
        self.identifiant=identifiant
        #position courante du voyageur
        self.x_courant=x_entree 
        self.y_courant=y_entree
        #position de la sortie
        self.x_sortie=x_sortie
        self.y_sortie=y_sortie
        self.est_arrive=False #statut du voyageur : arrivé ou non
        
    def meilleure_direction(self):
        '''Calcul de la meilleure direction (en terme de case) à prendre, renvoie un couple -1, 0 ou 1 selon la direction à prendre'''
        if self.x_courant>self.x_sortie: #si on a dépassé la sortie horizontalement
            x_deplacement=-1
        elif self.x_courant<self.x_sortie: #si on n'a pas dépassé la sortie horizontalement
            x_deplacement=1
        else: #si on est au niveau de la sortie horizontalement
            x_deplacement=0
        if self.y_courant>self.y_sortie: #si on a dépassé la sortie verticalement
            y_deplacement=-1
        elif self.y_courant<self.y_sortie: #si on n'a pas dépassé la sortie verticalement
            y_deplacement=1
        else:  #si on est au niveau de la sortie verticalement
            y_deplacement=0
        return x_deplacement,y_deplacement #on peut utiliser ce résultat pr savoir si le voyageur est arrivé
        if x_deplacement==0 and y_deplacement==0:
            self.est_arrive=True
    

    def change_coordonnees_voyageur(self,nv_x,nv_y):
        '''deplace le voyageur dans la meilleure_case_libre'''
        self.x_courant=nv_x
        self.y_courant=nv_y

            
        

class Case:
    '''classe créant les cases et gérant leur représentation graphique'''
    def __init__(self,x,y,etat):
        self.etat=etat #etat : libre=0, obstacle fixe=1, accès=2, voyageur=3
        self.x=int(x) #abscisse de la case           attention dans la représentation graphique ça doit correspondre à un carré 
        self.y=int(y) #ordonnée de la case           les coordonnées de la case indique les coordonnées du sommet en haut à gauche

    def modifier_etat(self,nv_etat):
        '''modifie l'état de la case'''
        self.etat=nv_etat

    def obtenir_etat(self):
        '''renvoie l'état de la case'''
        return self.etat

    def __str__(self):
        return str(self.etat)


class Carte:
    def __init__(self,x_dim,y_dim):
        ''''dimension de la carte x_dim et y_dim sont des entiers'''
        self.x_dim=x_dim
        self.y_dim=y_dim
        self.mesCases=[[0 for i in range(y_dim)] for j in range(x_dim)]

    def dessin_carte(self):
        '''Créer la carte avec les instances Case'''
        # initialisation des cases avec les bordures et le reste vide
        for i in range(self.x_dim):
            for j in range(self.y_dim):
                if i==0 or i==self.x_dim-1:
                    self.mesCases[i][j] = Case(i, j, 1) #bordure
                elif j == 0 or j== self.y_dim-1 :
                    self.mesCases[i][j] = Case(i, j, 1) #bordure          
                else :
                    self.mesCases[i][j] = Case(i, j, 0) #reste
            
        # création des cellules accès (3 cases à au moins 5 des extrémités)
        listeAcces = [[0 for i in range(2)] for i in range(4)]

        debut = randint(3, self.y_dim-5)
        for j in range(debut,debut+3):
            self.mesCases[0][j].modifier_etat(2)
        listeAcces[0][0] = 0
        listeAcces[0][1] = debut+1

        debut = randint(3, self.y_dim-5)
        for j in range(debut,debut+3):
            self.mesCases[self.x_dim-1][j].modifier_etat(2)
        listeAcces[1][0] = self.x_dim-1
        listeAcces[1][1] = debut+1

        debut = randint(3, self.x_dim-5)
        for i in range(debut,debut+3):
            self.mesCases[i][0].modifier_etat(2)
        listeAcces[2][0] = debut+1
        listeAcces[2][1] = 0

        debut = randint(3, self.x_dim-5)
        for i in range(debut,debut+3):
            self.mesCases[i][self.y_dim-1].modifier_etat(2)
        listeAcces[3][0] = debut+1
        listeAcces[3][1] = self.y_dim-1

        # création des cases obstacle
        nbObstacles = randint(5, 10)
        for nb in range(nbObstacles) :
            ligne = randint(3, self.x_dim-3)
            colonne = randint(3,self.y_dim-3)
            self.mesCases[ligne][colonne].modifier_etat(1)

        return listeAcces
    

    def meilleure_case_libre(self,x_deplacement, y_deplacement,x_courant,y_courant):
        '''x et y prennent les valeurs 0, 1 ou -1 selon la meilleure direction
        et la méthode renvoie la meilleure case libre selon cette direction'''
        x=x_courant+x_deplacement
        y=y_courant+y_deplacement
        #coordonnées de la case qui respecte la meilleure direction

        while self.mesCases[x][y].obtenir_etat() in [1,3]:
            x+=x_deplacement
            y+=y_deplacement
        # tant que la case obtenue n'est pas vide, on calcule de même les coordonnées de la case dans la meilleure direction

        #if self.mesCases[x][y].obtenir_etat()==2:
        #question : quid du voyageur qui arrive et sort ???            
            
        self.mesCases[x][y]=3
        #pour changer la meilleure case vide en case avec voyageur
        
        self.mesCases[x_courant][y_courant]=0
        #pour changer la case avec voyageur en case vide

        return x,y
        

#############################
########## FONCTION ########
############################

def main():
    x_dim=16 ; y_dim=10 #initialisation des dimensions de la carte
    c=Carte(x_dim, y_dim) #nouvel objet carte

    liste_acces=c.dessin_carte()
    
    for i in range(x_dim): # lignes
        for j in range(y_dim): # colonnes
            print(c.mesCases[i][j], end=" ")
        print()
    print("fin")
    
    '''On mélange la liste pour répartir les accès pour les voyageurs '''
    shuffle(liste_acces)
    
    liste_voyageurs=[]
    nb_voyageurs=5
    ''' On vérifie le nombre de voyageurs est inférieur ou égal au nombre d'accès -1'''
    if nb_voyageurs >= len(liste_acces) :
        nb_voyageurs=len(liste_acces)-1

    '''Création des voyageurs'''
    for i in range(nb_voyageurs) :
        '''Ajout des voyageurs'''
        '''Un voyageur par entrée'''
        x_entree = liste_acces[i][0]
        y_entree = liste_acces[i][1]
        x_sortie = liste_acces[i+1][0]
        y_sortie = liste_acces[i+1][1]
        liste_voyageurs.append(Voyageur(x_entree,y_entree,x_sortie,y_sortie,i))
        
    for voyageur in liste_voyageurs :
        x_deplacement, y_deplacement=voyageur.meilleure_direction()
        nv_x,nv_y=c.meilleure_case_libre(x_deplacement, y_deplacement,voyageur.x_courant,voyageur.y_courant)
        voyageur.change_coordonnees_voyageur(nv_x,nv_y)

    for i in range(x_dim): # lignes
        for j in range(y_dim): # colonnes
            print(c.mesCases[i][j], end=" ")
        print()


main()
    
        


    
