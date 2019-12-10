# Python
Premier test :
````python
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
