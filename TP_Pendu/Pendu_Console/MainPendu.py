#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 08:25:17 2020

@author: clement
"""

############################################### HEADER #######################################################

# Ce programme permet de jouer au pendu sur une console
# Réalisé par Poirié Clément 
# Réalisé le 27/11/2020

############################################### Module importé #######################################################
from fonctionPendu import game , listeCreate, modifBestscore , readBestscore 


############################################### MAIN #######################################################

listeCreate()  #Créé la liste de mots
condition_partie = True
bestScore_partie = 0


bestScore = readBestscore()
bestScore_int = int(bestScore)

print ("le plus grand nombre de partie consécutif joué au pendu est : ", bestScore , "essayez de plus jouer que cela ") 
print("voici le premier mot : ")

while condition_partie == True:
    condition_partie = game()  
    bestScore_partie += 1
   

modifBestscore(bestScore_int , bestScore_partie)
bestScore = readBestscore()

print ("le plus grand nombre de partie consécutif joué au pendu est : ", bestScore)    
   