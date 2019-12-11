from math import *
from copy import *
import random

class cVilles:
    def __init__ (self,name,x,y):
        self.name = name
        self.x = x
        self.y = y
        
    def Afficher_infos(self):
        print("Nom :",self.name)
        print("Longitude :",self.x)
        print("Latitude :",self.y)



class cTrajet:
    def __init__ (self,name,distance=0,trajet= [], villes = {}):
        self.name = name
        self.distance = distance
        self.trajet = trajet
        self.villes = villes
    def Definir_Villes(self,Nb_Villes):
        count = 0
        while(count< Nb_Villes):
            self.villes["Ville" + str(count+1)] = cVilles(str(input("Nom de la ville " + str(count+1) + "\n")),int(input("Entrez x : \n")),int(input("Entrez y : \n")))
            count += 1  
    def Definir_trajet(self, Nb_Villes):
        count = 0
        liste_trajet = []
        while(count< Nb_Villes):                  
            self.trajet.append(self.villes["Ville"+str(count+1)])
            count += 1
        random.shuffle(self.trajet)
        print("Le trajet effectué sera : \n")
        count = 0
        while(count< Nb_Villes):                  
            print(self.trajet[count].name)
            count += 1
        
    def Calculer_distance(self,Nb_Villes):
        distance_totale = []
        count = 0
        while(count< Nb_Villes-1):                  
            distance = (sqrt( abs((self.villes["Ville"+str(count+1)].x-self.villes["Ville"+str(count+2)].x)**2 + (self.villes["Ville"+str(count+1)].y-self.villes["Ville"+str(count+2)].y)**2)),1)     #Formule de maths...
          #  print("La distance qui sépare ",self.villes["Ville"+str(count+1)].name, self.villes["Ville"+str(count+2)].name, "est de :", distance)     
            distance_totale.append(distance)
            self.distance = sum(distance_totale)
            count += 1
        print("La distance totale est de : ", self.distance)


def Generation_trajet () :
    Nb_trajet = int(input("Entrez le nombre de trajets aléatoire à générer (Moins de 5 pour l'instant svp)"))
    count = 0
    Nb_Villes = int(input("Entrez le nombre de villes : "))
    Trajet = {}
    while(count< Nb_trajet):            # Crée les variables trajets dans un dictionnaire   Ils seront notés Trajet["Trajet1"], Trajet["Trajet2"]
        Trajet["Trajet"+str(count+1)] = cTrajet("Trajet"+str(count+1))
        count += 1
    Trajet["Trajet1"].Definir_Villes(Nb_Villes) #On défini les villes pour le premier trajet pour pouvoir directement les mélanger ensuite sans les redéclarer

    count = 0  
    while(count< Nb_trajet):            # Crée les variables trajets dans un dictionnaire   Ils seront notés Trajet["Trajet1"], Trajet["Trajet2"]
        Trajet["Trajet"+str(count+1)].villes = deepcopy(Trajet["Trajet1"].villes)          # On évite de redéclarer les villes à chaque fois
        Trajet["Trajet"+str(count+1)].Definir_trajet(Nb_Villes)
        Trajet["Trajet"+str(count+1)].Calculer_distance(Nb_Villes)
        count += 1

        
        



Generation_trajet()




        
