#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 15:59:49 2020

@author: clement
"""

##############################################################################################################################
#                                                                HEADER
##############################################################################################################################


# Ce programme permet de jouer au pendu sur une console
# Réalisé par Poirié Clément 
# Réalisé le 11/12/2020
# Reste à faire : 
#amélioration des fonctions : enlever les "global"

##############################################################################################################################
#                                                           MODULES IMPORTES
##############################################################################################################################




from fonctionPendu_Tkinter import listeCreate , wordChoice ,StartWordPrint ,letterPosition 
from fonctionPendu_Tkinter import  appendLetters , readBestscore, modifBestscore

from tkinter import Tk , Label , Entry , Canvas , PhotoImage , Button




##############################################################################################################################
#                                                           FONCTIONS TKINTER
##############################################################################################################################

# analyse si la lettre entrée par l'utilisateur est dans le mot et fais toutes les modifs necessaires
def game ():
    
    global mot_cherche , listeLetter , motCache , chance , affich_image , canvas , Condition_victoire , bestScore_int, score_partie
    liste_prescrite = ['1','2','3','4','5','6','7','8','9']
    
    lettre_choisie = commande_joueur.get() #récupère la lettre entré par l'utilisateur
        
    liste_position = letterPosition(lettre_choisie , mot_cherche ) #ajout de cette lettre dans la liste
    
    commande_joueur.delete(0 , 'end')
    
    # verifie que c'est une lettre qui est rentrée
    if len(lettre_choisie) == 1:
        if lettre_choisie[0] not in liste_prescrite:
            
            #verifie que la lettre a pas déja été rentrée
            if lettre_choisie in listeLetter:
                
                Label_princ['text'] = "vous avez déjà proposé cette lettre"
                
                
            else:
                
                listeLetter.append(lettre_choisie)
                lettre_utilise['text'] = "lettres utilisées " + str(listeLetter)
                
                #lettre pas dans le mot
                if liste_position == []:
                    chance = chance - 1
                    vie_restante['text'] = "il vous reste " + str(chance) + " vie"
                    Label_princ['text'] = "Cette lettre n'est pas dans le mot"
                    
                    affich_image = canvas.create_image(0,0,anchor = 'nw' , image = image_pendu[chance-1] ) #Change l'image (descend dans la liste)
                    if chance == 0:
                        Label_princ['text'] = "Vous avez perdu \n Voulez vous rejouer ?"
                        bouton_valider['text'] = "Nouvelle partie"
                        if bestScore_int < score_partie:
                            modifBestscore(bestScore_int , score_partie)
                #lettre dans le mot    
                else:
                    Label_princ['text'] = "Cette lettre est dans le mot"
                    motCache = appendLetters(liste_position, lettre_choisie, motCache)
                    affichage_mot['text'] = motCache
                    if motCache == " ".join(mot_cherche):
                        Label_princ['text'] = "Vous avez gagnez \n Voulez vous rejouer ?"
                        bouton_valider['text'] = "Nouvelle partie"
                        if bestScore_int < score_partie:
                            modifBestscore(bestScore_int , score_partie)
            
        else:
            Label_princ['text'] = "on accepte pas les chiffres"
        
    else:
        Label_princ['text'] = "une seule lettre je vous pris"
        
            
# renitialise toute les valeurs et remet la fenetre de base        
def Initialisation ():
    global chance , mot_cherche , listeLetter , liste_mots , motCache , affichage_mot , affich_image , score_partie , bestScore_int
    chance = 8
    mot_cherche = wordChoice(liste_mots)
    listeLetter = []
    motCache = StartWordPrint(mot_cherche)    
    bestScore = readBestscore()
    bestScore_int = int(bestScore)
    score_partie = score_partie + 1
    Meilleur_Score['text'] ="Plus grand nombre de partie succesive joué :" + bestScore    
    bouton_valider['text'] = "valider la lettre"
    affichage_mot['text'] = motCache
    Label_princ['text'] = "" 
    vie_restante['text'] = "il vous reste " + str(chance) + " vie"
    affich_image = canvas.create_image(0,0,anchor = 'nw' , image = image_pendu[7] )
    lettre_utilise['text'] = "lettres utilisées " + str(listeLetter)

#action du bouton principal         
def Bouton_Princ ():
    global bouton_valider
    
    if bouton_valider['text'] == "Nouvelle partie":
        Initialisation()
        
    elif bouton_valider['text'] == "valider la lettre":
        game()

#permet de valider une lettre en appuyant sur la touche entrée du clavier  
def clavier (event):
    touche = event.keysym
    if touche == 'Return':
        game()
#        
     
##############################################################################################################################
#                                                       MAIN
##############################################################################################################################


###########################
#     Variables Globales
###########################

                  
liste_mots = listeCreate()
listeLetter = []

chance = 8
score_partie = 1 

mot_cherche = wordChoice(liste_mots)
motCache = StartWordPrint(mot_cherche)

bestScore = readBestscore()
bestScore_int = int(bestScore)


########################
#     FENETRE TKINTER
########################

#création de la fenetre
fenetre = Tk()
fenetre.title("Le pendu")
fenetre.geometry("1000x500")
fenetre.configure(bg = "#3c3e43")

                  
#création des wigets              

#création des Labels et positionnement                   
affichage_mot = Label(fenetre , text = StartWordPrint(mot_cherche) , bg = '#3c3e43' , fg ='white', font =("Helvetica", 30  )   )
affichage_mot.grid(row = 1, column = 2)

Label_princ = Label(fenetre , text = "", bg = '#3c3e43' , fg ='white' )
Label_princ.grid (row = 2 , column = 2 )

indications = Label( fenetre , text = "entrer une lettre : ", bg = '#3c3e43' , fg ='white' )
indications.grid (row = 3 , padx = 10 , sticky = 'E')

lettre_utilise = Label( fenetre , text = "lettres utilisées " + str(listeLetter) , bg = '#3c3e43' , fg ='white' )
lettre_utilise.grid(row =5 , column = 0 , columnspan = 3 , sticky = 'E')

Meilleur_Score = Label( fenetre , text = "Plus grand nombre de partie succesive joué : " + bestScore , bg = '#3c3e43' , fg ='white' )
Meilleur_Score.grid(row = 0, column = 0 , columnspan = 3)

vie_restante = Label( fenetre , text = "il vous reste " + str(chance) + " vie", bg = '#3c3e43' , fg ='white' )
vie_restante.grid(row = 4 , column = 0)   

                
#création de l'entée et positionnement                    
commande_joueur = Entry (fenetre , width = 30) 
commande_joueur.bind('<Return>' , clavier) #"écoute" le clavier du joueur et execute la fonction clavier
commande_joueur.grid (row = 3 , column = 2 , padx = 10)              

#création de du bouton et positionnement
bouton_valider = Button (fenetre , text = "valider la lettre" , bg = "white" , fg = "black" , command = Bouton_Princ )
bouton_valider.grid(row = 4 , column = 1 , columnspan = 2 )   

#création du canvas et de la liste d'image positionné dedans et positionnement dans la fenetre           
canvas = Canvas ( fenetre , width = 300 , height = 300 , bg = "#3c3e43")
image_pendu = []
for i in range (1,9):
    image_pendu.append(PhotoImage(file = "Image_pendu/bonhomme" + str(i) + ".gif")) #créé une liste d'image 
image_pendu.reverse() #on l'inverse 
affich_image = canvas.create_image(0,0,anchor = 'nw' , image = image_pendu[7] ) #on créé la premiere image
canvas.grid ( row = 1 , column = 3 ,rowspan = 5, padx = 100 , pady = 50 , sticky = 'nesw') #on affiche premiere image et canvas                 







                




























            
                  
                 
fenetre.mainloop()