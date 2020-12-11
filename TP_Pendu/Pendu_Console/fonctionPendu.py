#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 07:49:57 2020

@author: clement
"""

############################################### HEADER #########################################################

# Ce programme regroupe toutes les fonctions utilisées dans le jeu pendu
# Réalisé le 27/11/2020 
# Réalisé par Poirié Clément 
# il reste à faire :
# améliorer le fichier texte qu'il se trie automatiquement

############################################### Module importé ##################################################

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

  
#La fonction game est la fonction qui correspond à un tour de jeu    
def game ():
        score = 8 #chaque tour on a nos 8 chances
        listeLetter = [] # Liste des lettre utilisé lors du tour de jeu
        word = wordChoice(listeCreate()) #Récupère un mot du fichier texte
        
        
        searchedWord = StartWordPrint(word) #Créé le mot "caché" : la première lettre du mot et les tirets
              
        game = True #Création d'un flag (d'une condition du tour de jeu)
        
        while game == True :
                        
            print(searchedWord) #affihe à l'utilisateur le mot caché

            flag1= False #création d'un flag pour le choix de la lettre (redemande la lettre)
            
            while flag1== False:
                user_letter = input (" choisissez une lettre : ")
                if user_letter.isalpha() == True: # verifie si c'est bien un str qui est rentré
                        if len(user_letter) == 1: # verifie qu'il y a bien une lettre de rentré
                            if user_letter not in listeLetter: #verifie si la lettre a pas déja été utilié 
                                flag1=True #condition de sortie de la boucle 
                       
                    
                  
                
            listeLetter.append(user_letter) #on ajoute la lettre entré par l'utilisateur dans la liste des lettre utilisé
            
            position = letterPosition(user_letter , word) #retourne position si lettre dans le mot            
                   
            if position == []: #Si lettre pas dans le mot : perte d'une chance 
                score -= 1
                print("il vous restes : " , score , "chance(s)")
                if score <= 0: #si score est à 0 fin de partie
                    print ("vous perdez")
                    game = False #condition de sortie du tour de jeu

            else: #si lettre dans le mot on ajoute la ou les lettre(s) suivant les positions dans le mot "caché"
                searchedWord = appendLetters(position, user_letter, searchedWord)
         
            
            if  searchedWord == " ".join(word): #si le mot caché est le même que le mot choisie dans le fichier texte : il a trouvé toutes les lettre il gagne
                
                print("vous avez gagnez")
                game = False #condition de sortie du tour de jeu
                
        flag2 = False #flag pour redemander à l'utilisateur si il saisie une valeur incorecte       
        while flag2 == False:
            condition = input("voulez vous rejouer ? ")  
            if condition == "oui":
                flag2 = True 
                return(True) # permet de rejouer une partie (boucle while du Main)
                
            if condition == "non": #permet arreter la partie (condition de sortie de la boucle while du Main)
                flag2 = True
                return(False)
        
       
     




       

   
    


 
        
    



