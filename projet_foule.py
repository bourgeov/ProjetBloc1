#-*- coding: utf-8 -*-

class Voyageur:
    def __init__(self,x_entree,y_entree,x_sortie,y_sortie,identifiant):
        '''coordonnées d'entrée (chercher dans la liste des accès) et coordonnées de sortie du voyageur'''
        self.identifiant=identifiant
        self.x_courant=x_entree 
        self.y_courant=y_entree
        '''position courante du voyageur'''
        self.x_sortie=x_sortie
        self.y_sortie=y_sortie
        '''position de la sortie'''
        self.est_arrive=False '''statut du voyageur : arrivé ou non'''
        
    def meilleure_direction(self):
        '''Calcul de la meilleure direction à prendre'''
        if self.x_courant!=self.x_sortie:
            ''''on calcule le coefficient directeur de la droite liant la position actuelle et la sortie'''
            self.y_courant=round((self.y_sortie-self.y_courant)/(self.x_sortie-self.x_courant))
            if self.y_courant>1:
                self.y_courant=1
            elif self.y_courant<-1:
                self.y_courant=-1
            if self.x_courant>self.x_sortie
                self.x_courant-=1
            elif self.x_courant<self.x_sortie:
                self.x_courant+=1

    def change_coordonnees_voyageur(self,nv_x,nv_y):
        '''deplace le voyageur dans la meilleure_case_libre'''
        self.x_courant=nv_x
        self.y_courant=nv_y

    def supprimer_voyageur(self):
        '''enlever le voyageur de l'interface graphique'''
        pass

class Case:
    '''classe créant les cases et gérant leur représentation graphique'''
    def __init__(self,etat,x,y):
        self.etat=etat '''etat : libre=0, obstacle fixe=1, accès=2, voyageur=3'''
        self.x=x '''abscisse de la case'''
        self.y=y '''ordonnée de la case'''

    def modifier_etat(self,nv_etat):
        '''modifie l'état de la case'''
        self.etat=nv_etat

    def obtenir_etat(self):
        '''renvoie l'état de la case'''
        return self.etat

class Carte:
    def __init__(self,x_dim,y_dim):
        ''''dimension de la carte x_dim et y_dim sont des entiers'''
        self.x_dim=x_dim
        self.y_dim=y_dim

    def dessin_carte(self):
        '''Créer la carte avec les instances Case'''
        mesCases = [[0 for i in range(x_dim)] for j in range(y_dim)]
        for i in range(x_dim):
            for j in range(y_dim):
                mesCases[i][j] = Case(randint(0,2),i, j)
  

    def meilleure_case_libre(self):
        ''''propose la meilleure case libre selon la meilleure_direction obtenue'''
        pass

    


    

def main():
    x_dim=500 ; y_dim=300 '''initialisation des dimensions de la carte'''
    nb_acces=4
    nb_voyageurs=nb_acces
    c=Carte(x_dim, y_dim) '''nouvel objet carte'''
    c.dessin_carte()
    liste_voyageurs=[i for i in range(1,nb_voyageurs+1)]
    
    
    
    
    
        

    
    
    
        
        
        
