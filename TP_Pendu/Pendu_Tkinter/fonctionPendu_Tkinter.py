#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 18:20:41 2020

@author: clement
"""

from random import choice


############################################### FONCTIONS #######################################################


#Va chercher dans le fichier texte les mots et les entres dans une liste puis la retourne
def listeCreate():
    listeWord = []
    fichier_text = open("motsPendu.txt" , "r")#ouvre le fichier .txt
    for line in fichier_text:#il le parcourt
        word = line[:-1] #récupère chaque mot sur les lignes
        listeWord.append(word)#les ajoutes
    fichier_text.close #ferme le fichier
    return(listeWord)


def readBestscore():
    file = open("score.txt" , 'r') 
    bestScore = file.read()
    file.close
    return(bestScore)
    
        
def modifBestscore(oldScore , newScore):
    if newScore > oldScore:
        bestScore = str(newScore)
        file = open("score.txt" , "w")
        file.writelines(bestScore)
        file.close

           
#permet de choisir aléatoirement un mot dans une liste de mots puis le retoune sous forme d'une liste de lettre
def wordChoice (wordListe):
    word=[]
    wordChosenstr= choice(wordListe) #choisie aléatoirement
    for i in wordChosenstr:
        word.append(i)#créé le mot sous forme de liste
    return(word)


#Créé le mot "caché" : 1ere lettre visible le reste sous forme de tiret espacé 
def StartWordPrint(pWord):
    numberLetter = len (pWord) -1 #pensé à enlever la première lettre qui sera visible
    displayedWord = pWord[0] +(' '+ '_' + ' ' )* numberLetter # creation du mot "caché"
    return (displayedWord)
    

#Récupère la position des lettre et les retournes et si il y a pas la lettre elle retourne une 
#liste vide
def letterPosition (pletter , punknowWord):
    position = [] #liste des position de la lettre en param
    positionActuelle = 0
    for letter in punknowWord: #cherche la lettre
        if letter == pletter: #si elle la trouve
            position.append(positionActuelle) #ajoute ca position a la liste
        positionActuelle += 1 # tu avance de un et recommence
    return (position)


#Fonction permet d'ajouter une lettre au mot "caché" à la bonne position et retourne le nouveau 
#mot caché
def appendLetters(positionParam, letterParam, searchedWordParam):
    
    Word_no_space = searchedWordParam.replace(" ","") #afin de créer une liste sans terme "espace" on créé le mot caché sans espace : 1lettre______
     
    searchedWordList = list(Word_no_space) # créé le mot sous forme de liste      

    for position in positionParam : #Récupère les positions des lettre à ajouté
        
        searchedWordList[position] = letterParam #Remplace chaque '_' par la lettre entrée par l'utilisateur
            
    searchedWordParam = ' '.join(searchedWordList) #Remet le mot "caché" en str avec les lettres en plus et les espaces
    
    return searchedWordParam


    
    
