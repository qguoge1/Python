# Python
## Premier test juste avec des initialisations:
```python
import math
from math import *
class cVilles:
    def __init__ (self, name , x , y ):
        self.name = name
        self.x = x
        self.y = y
    def Afficher_infos(self):
        print("Nom :",self.name)
        print("Longitude :",self.x)
        print("Latitude :",self.y)

def Calculer_distance(Ville1,Ville2):
    distance = round(sqrt( (Ville1.x-Ville2.x)**2 - (Ville1.y-Ville2.y)**2),1)
    print("La distance qui sépare les deux villes est de :", distance)
    
Ville1 = cVilles("Bordeaux",1,5)
Ville2 = cVilles("Alsace",10,5)
Ville3 = cVilles("Paris",5,2)

Ville1.Afficher_infos()
Ville2.Afficher_infos()
Ville3.Afficher_infos()

Calculer_distance(Paris,Bordeaux)   
```
## Deuxième test avec des calculs de villes :

```python
import math
from math import *
from copy import *

class cVilles:
    def __init__ (self):
        self.name = str(input("Entrez le nom de la ville :"))
        self.x = int(input("Entrez la coordonnée en x :"))
        self.y = int(input("Entrez la coordonnée en y :"))
    def Afficher_infos(self):
        print("Nom :",self.name)
        print("Longitude :",self.x)
        print("Latitude :",self.y)

def Calculer_distance(Ville1,Ville2,Liste):
    distance = round(sqrt( abs((Ville1.x-Ville2.x)**2 + (Ville1.y-Ville2.y)**2)),1)
    print("La distance qui sépare ",Ville1.name, Ville2.name, "est de :", distance)
    Liste.append(distance)
    
    
Liste = []
count= 0
Nb_villes = int(input("Entrez le nombre de villes à parcourir"))
print("Remplissez les données pour la ville de départ")
Ville1 = cVilles()




while ( count < Nb_villes):
    count+= 1
    print("Remplissez les données pour la ville suivante")
    Ville2 = cVilles()
    Ville1.Afficher_infos()
    Ville2.Afficher_infos()
    Calculer_distance(Ville1,Ville2,Liste)
    Ville1 = deepcopy(Ville2)
    

distanceTot = sum(Liste)
print("La distance totale est de :" ,distanceTot)
```
## 3eme test avec beaucoup d'itérations :
```python
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

def Calculer_distance(Ville1,Ville2,Liste):
    distance = round(sqrt( abs((Ville1.x-Ville2.x)**2 + (Ville1.y-Ville2.y)**2)),1)
    print("La distance qui sépare ",Ville1.name, Ville2.name, "est de :", distance)
    Liste.append(distance)
    
Liste = []    
NvListe = [999999999]


count= 0
Nb_Villes = 5
count1 = 0
Ville1 = cVilles("Paris",5,8)
Ville2 = cVilles("Bordeaux",2,2)
Ville3 = cVilles("Alsace",9,5)
Ville4 = cVilles("Marseille",5,2)
Ville5 = cVilles("Bretagne",0,9)
ListeVille = [Ville1,Ville2,Ville3,Ville4,Ville5]



while count1< 100:
    random.shuffle(ListeVille)
    while(count< Nb_Villes-1):
        Calculer_distance(ListeVille[count],ListeVille[count+1],Liste) 
        count += 1
    if(sum(Liste)< sum(NvListe)):
        NvListe = deepcopy(Liste)
    Liste = []
    count1 = count1 + 1
    count=0
    
distance_finale = sum(NvListe)
print(distance_finale)

    
```
## 4e test avec plusieurs villes :

```python

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

def Calculer_distance(Ville1,Ville2,Liste):
    distance = round(sqrt( abs((Ville1.x-Ville2.x)**2 + (Ville1.y-Ville2.y)**2)),1)     #Formule de maths...
    #print("La distance qui sépare ",Ville1.name, Ville2.name, "est de :", distance)     # print pour les tests 
    Liste.append(distance)                      # On rajoute la distance calculée dans une "liste"
        
Liste = []                      # Liste pour stocker les distances  (On utilisera une fonction "sum()"
NvListe = [999999999]           # Liste pour stocker la distance la plus petite ( on initialise une valeur très grande pour la                                           # comparaison)


count= 0            #Compteur pour compter les trajets effectués
Nb_Villes = 9           # Variables pour les nombres de villes
count1 = 0              # Pour compter le nombre d'itérations que l'on teste
Ville1 = cVilles("Paris",5,8)       # Déclarations des villes pour tester 
Ville2 = cVilles("Bordeaux",2,2)
Ville3 = cVilles("Alsace",9,5)
Ville4 = cVilles("Marseille",5,2)
Ville5 = cVilles("Bretagne",0,9)
Ville6 = cVilles("Normandie",5,9)
Ville7 = cVilles("Bourgogne",5,6)
Ville8 = cVilles("Champagne",5,7)
Ville9 = cVilles("Toulouse",2,3)

ListeVille = [Ville1,Ville2,Ville3,Ville4,Ville5,Ville6,Ville7,Ville8,Ville9]       # Liste qui stocke les villes, il permet de                                                                         # "mélanger"(shuffle()) l'ordre des villes



while count1< 2:            # Boucle qui permet de générer des trajets différents
    random.shuffle(ListeVille)          #Le mélangeur de liste
    while(count< Nb_Villes-1):                  # Boucle qui calcule la distance totale pour le trajet
        Calculer_distance(ListeVille[count],ListeVille[count+1],Liste)      # Calcule la distance entre villes stockées dans ListeVille
        count += 1                     
    if(sum(Liste)< sum(NvListe)):               # Comparaison, NvListe prend la valeur de Liste si sa distance est plus petite
        NvListe = deepcopy(Liste)                   #deepcopy pour éviter des problèmes
    Liste = []              # On vide la liste avant de refaire le calcul des distances
    count1 = count1 + 1         # On incrémente le compteur de la grande boucle 
    count=0                         # On réinitialise le compteur de la petite boucle (Sinon il calcule qu'un trajet)
    
distance_finale = sum(NvListe)      # La distance_finale est la somme des distances calculée
print(distance_finale)                  # affichage du résultat

    

```
- Hypothèses (Intégration Classe + Génération des trajets aléatoires)
```python
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
    def __init__ (self,name,distance=[],trajet= {},coordonnee={}):
        self.name = name
        self.distance = distance
        self.trajet = trajet
        self.coordonnee = coordonnee

    def Definir_trajet(self, Nb_villes):
        count = 0
        liste_trajet = []
        self.trajet = {}
        while(count< Nb_Villes):                  
            self.trajet["Ville" + str(count+1)] = cVilles(str(input("Nom de la ville " + str(count+1) + "\n")),int(input("Entrez x : \n")),int(input("Entrez y : \n")))
            liste_trajet.append(self.trajet["Ville"+str(count+1)].name)
            count += 1
        print(liste_trajet)
    def Calculer_distance(self):
        distance_totale = []
        count = 0
        while(count< Nb_Villes-1):                  
            distance = round(sqrt( abs((self.trajet["Ville"+str(count+1)].x-self.trajet["Ville"+str(count+2)].x)**2 + (self.trajet["Ville"+str(count+1)].y-self.trajet["Ville"+str(count+2)].y)**2)),1)     #Formule de maths...
            #print("La distance qui sépare ",Ville1.name, Ville2.name, "est de :", distance)     # print pour les tests 
            distance_totale.append(distance)
            count += 1
        print("La distance totale est de : ", sum(distance_totale))


def Génération_trajet :
    Nb_trajet = int(input("Entrez le nombre de trajets aléatoire à générer (Moins de 5 pour l'instant svp)"))
    count = 0
    Nb_Villes = int(input("Entrez le nombre de villes : "))
    Trajet = {}
    while(count< Nb_trajet):
        Trajet["Trajet"+str(count+1)] = cTrajet("Trajet"+str(count+1))
        
        Trajet["Trajet"+str(count+1)].Definir_trajet(Nb_Villes)
        count += 1





Trajet1.Calculer_distance()
```
- Marche mais il faut optimiser la déclaration des villes :
```Python
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
    def __init__ (self,name,distance=0,trajet= {},coordonnee={}):
        self.name = name
        self.distance = distance
        self.trajet = trajet
        self.coordonnee = coordonnee

    def Definir_trajet(self, Nb_Villes):
        count = 0
        
        liste_trajet = []
        self.trajet = {}
        while(count< Nb_Villes):                  
            self.trajet["Ville" + str(count+1)] = cVilles(str(input("Nom de la ville " + str(count+1) + "\n")),int(input("Entrez x : \n")),int(input("Entrez y : \n")))
            liste_trajet.append(self.trajet["Ville"+str(count+1)].name)
            count += 1
        print(liste_trajet)
        
    def Calculer_distance(self,Nb_Villes):
        distance_totale = []
        count = 0
        while(count< Nb_Villes-1):                  
            distance = round(sqrt( abs((self.trajet["Ville"+str(count+1)].x-self.trajet["Ville"+str(count+2)].x)**2 + (self.trajet["Ville"+str(count+1)].y-self.trajet["Ville"+str(count+2)].y)**2)),1)     #Formule de maths...
            #print("La distance qui sépare ",Ville1.name, Ville2.name, "est de :", distance)     # print pour les tests 
            distance_totale.append(distance)
            self.distance = sum(distance_totale)
            count += 1
        print("La distance totale est de : ", self.distance)


def Generation_trajet () :
    Nb_trajet = int(input("Entrez le nombre de trajets aléatoire à générer (Moins de 5 pour l'instant svp)"))
    count = 0
    Nb_Villes = int(input("Entrez le nombre de villes : "))
    Trajet = {}
    while(count< Nb_trajet):
        Trajet["Trajet"+str(count+1)] = cTrajet("Trajet"+str(count+1))
        
        Trajet["Trajet"+str(count+1)].Definir_trajet(Nb_Villes)
        Trajet["Trajet"+str(count+1)].Calculer_distance(Nb_Villes)
        count += 1



Generation_trajet()



```
- Code shuffle intégré avec calcul distance

```python
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
```
- Marche jusqu'à la génération des trajets aléatoires :
```python
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
            distance = round(sqrt(abs((self.trajet[count].x-self.trajet[count+1].x)**2 + (self.trajet[count].y-self.trajet[count+1].y)**2)),1)     #Formule de maths...
          #  print("La distance qui sépare ",self.trajet[count].name, self.trajet[count+1].name, "est de :", distance)     
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
        Trajet["Trajet"+str(count+1)].villes =  Trajet["Trajet1"].villes.copy()          # On évite de redéclarer les villes à chaque fois
        Trajet["Trajet"+str(count+1)].Definir_trajet(Nb_Villes)
        Trajet["Trajet"+str(count+1)].Calculer_distance(Nb_Villes)
        count += 1





Generation_trajet()
```
ma keh ( sans génétique):
```python
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

        self.trajet = []
        while(count< Nb_Villes):
            self.trajet.append(self.villes["Ville"+str(count+1)])
            print(self.trajet)
            count += 1

        print("before", self.trajet)    
        random.shuffle(self.trajet)
        print("after", self.trajet)
        print("Le trajet effectué sera : \n")

        count = 0
        while(count< Nb_Villes):                  
            print(self.trajet[count].name)
            count += 1
        
    def Calculer_distance(self,Nb_Villes):
        distance_totale = []
        count = 0
        while(count< Nb_Villes-1):                  
            distance = round(sqrt(abs((self.trajet[count].x-self.trajet[count+1].x)**2 + (self.trajet[count].y-self.trajet[count+1].y)**2)),1)     #Formule de maths...
          #  print("La distance qui sépare ",self.trajet[count].name, self.trajet[count+1].name, "est de :", distance)     
            distance_totale.append(distance)
            self.distance = sum(distance_totale)
            count += 1
        print("La distance totale est de : ", self.distance)
    def meilleur_trajet

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
        Trajet["Trajet"+str(count+1)].villes =  deepcopy(Trajet["Trajet1"].villes)          # On évite de redéclarer les villes à chaque fois

        Trajet["Trajet"+str(count+1)].Definir_trajet(Nb_Villes)
       # print("in gnerqaion_trajt" ,[[Trajet["Trajet"+str(i+1)].trajet[j].name for i in range(Nb_trajet)] for j in range(Nb_trajet)])         Trajet["Trajet"+str(count+1)].Calculer_distance(Nb_Villes)
        count += 1





Generation_trajet()
```
