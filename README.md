# Python

```
from math import *

class villes():

    def __init__(self, nom, x, y):
        self.nom_ville=nom
        self.ab=x
        self.ord=y
        
    def resume(self):
        print("la ville est:",self.nom_ville)
        print("coordonné en x", self.ab)
        print("coordonné en y", self.ord)

def distance(Ville1,Ville2):
    dist= round(sqrt((Ville1.ab-Ville2.ab)**2 + (Ville1.ord-Ville2.ord)**2),1)
    print("distance ente ces 2 villes vaut:",dist)

def totalDistance(Ville1,Ville2,Ville3):
    dist1= round(sqrt((Ville1.ab-Ville2.ab)**2 + (Ville1.ord-Ville2.ord)**2),1)
    dist2= round(sqrt((Ville2.ab-Ville3.ab)**2 + (Ville2.ord-Ville3.ord)**2),1)
    dist3= round(sqrt((Ville3.ab-Ville1.ab)**2 + (Ville3.ord-Ville1.ord)**2),1)
    total= dist1 + dist2 + dist3
    print("total de la distance est:",total)
    return total

Ville1 = villes("paris",2,3)
Ville1.resume()

Ville2= villes("rome",5,7)
Ville2.resume()

Ville3 = villes("new york",7,4)
Ville3.resume()


Ville4 = villes("dubaï",1,1)
Ville4.resume()

totalDistance(Ville2,Ville3,Ville4) 
##distance(Ville3,Ville4)
##distance(Ville1,Ville2)

```
