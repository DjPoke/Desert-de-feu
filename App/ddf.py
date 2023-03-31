#!/usr/bin/python
# -*- coding: UTF-8 -*-

# =======================================================
# Nom du programme : "Désert de feu"
# Type de jeu : "Jeu d'aventure textuel"
# Par : "Bruno Vignoli"
# Site : "http://retro.bruno.pagesperso-orange.fr/"
# Commencé le : "25/10/2013 à 20h05"
# Nécessite : "Python 2.7.4 minimum et le module Pygame"
# =======================================================

import pygame
from pygame import *
import time
import math

# Définition des couleurs de base
green = (56 , 68 , 20)
greentxt = (192 , 255 , 128)
black = (0 , 0 , 0)
white = (255 , 255 , 255)
grey = (128 , 128 , 128)
red = (255 , 0, 0)

# Constantes du jeu
screen_width = 1024
screen_height = 768
screen_txt_y = 463
screen_txt_height = 252
screen_image_x = 256
screen_image_y = 26
intro_image_x = 256
intro_image_y = 0
font_size = 22
mini = ""

# Initialiser pygame
pygame.init()

# Charger les quelques sons
intro_sound = pygame.mixer.Sound("sons/intro.ogg")
sound_0 = pygame.mixer.Sound("sons/insecte.ogg")
sound_1 = pygame.mixer.Sound("sons/mecanisme.ogg")
end_sound = pygame.mixer.Sound("sons/end.ogg")
sound = []
sound.append(False) # flag son d'intro joué
sound.append(False) # flag son de fin joué

# Variables et constantes de base
lieu_descr = []
lieu_descr.append("") # 0, non exploité
lieu_descr.append("Vous êtes dans un endroit désertique et inquiétant. \
Il y a un arbre près de vous qui est mystérieusement débordant de verdure. \
On peut d'ailleurs se demander ce qu'il fait là...") # 1
lieu_descr.append("Vous êtes dans un recoin du néant. C'est un endroit \
désertique et rocailleux. La chaleur y est par moments intenable.") # 2
lieu_descr.append("Vous êtes dans un endroit inquiétant. Par ici, la chaleur \
est suffocante.") # 3
lieu_descr.append("Vous êtes dans un désert où la chaleur est oppressante. Un \
très vieux puits en pierre bouché et inutilisable se trouve devant vous.") # 4
lieu_descr.append("Vous êtes dans un désert hostile. Il fait très chaud par ici, \
et vous commencez à avoir soif. Un barbare est là, à peine à quelques mètres \
devant vous.") # 5
lieu_descr.append("Vous êtes devant un château entouré de brume. Un étrange \
brouillard grisâtre couvre le ciel plongeant ce désert dans une ambiance plus \
froide. Un soldat attend devant l'entrée d'un château, entre deux tours.") # 6
lieu_descr.append("Vous êtes devant un lac. Étrangement, l'endroit devient plus \
rocailleux, et vous vous trouvez maintenant proche d'un lac.") # 7
lieu_descr.append("Vous êtes dans un endroit perdu dans le désert. Il n'y a ici \
que des dunes, du sable et un ciel brûlant qui vous accable de douleur.") # 8
lieu_descr.append("Vous êtes dans un désert, près d'un squelette. Étrangement, \
le ciel commence à se griser. Quant à ce tas d'os devant vous, il est vieux, usé \
par l'oxydation dûe à l'acidité de l'air.") # 9
lieu_descr.append("Vous êtes dans un château étrange. Ce château est, semble-t'il, \
bien gardé par plusieurs soldats. Et ce brouillard qui enveloppe le ciel vous \
intrigue.") # 10
lieu_descr.append("Vous êtes dans l'angle Nord-Est du château. Les bâtisses sont anciennes, et l'une d'entre elles est recouverte de lière.") # 11
lieu_descr.append("Vous êtes dans un château inquiétant. Un homme semblant faire partie de la noblesse vous tourne le dos, pensif. Il doit s'agir du Prince de Gmell") # 12
lieu_descr.append("Vous êtes dans le château de Gmell. Une femme vous fait face. Elle porte sur elle un étrange accoutrement.") # 13
lieu_descr.append("Vous êtes dans l'angle Sud-Ouest du château.") # 14
lieu_descr.append("Vous êtes dans l'angle Sud-Est du château.") # 15
lieu_descr.append("Vous êtes dans le désert, face à un insecte géant.") # 16
lieu_descr.append("Vous êtes dans le désert. Il y a une ruine juste en face de vous.") # 17
lieu_descr.append("Vous êtes dans un endroit chaud du désert. Il y a un guerrier devant vous.") # 18
lieu_descr.append("Vous êtes dans le désert, face à un dragon.") # 19
lieu_descr.append("Vous êtes dans le désert, devant l'entrée d'une crypte.") # 20
lieu_descr.append("Vous êtes dans une crypte lugubre.") # 21
lieu_descr.append("Vous êtes dans une crypte dont l'extrémité Est mène à une porte.") # 22
lieu_descr.append("Vous êtes dans une crypte inquiétante. Une araignée géante se trouve en face de vous.") # 23
lieu_descr.append("Vous êtes dans une crypte sombre.") # 24
lieu_descr.append("Vous êtes dans une crypte lugubre, face à un gros coffre.") # 25
lieu_descr.append("Vous êtes dans la nature, libre.") # 26

lieu_dir = []
lieu_dir.append([0 , 0 , 0 , 0 , 0 , 0]) # 0, non exploité
lieu_dir.append([0 , 5 , 2 , 3 , 0 , 0]) # 1
lieu_dir.append([0 , 6 , 0 , 1 , 0 , 0]) # 2
lieu_dir.append([0 , 4 , 1 , 0 , 0 , 0]) # 3
lieu_dir.append([3 , 7 , 5 , 0 , 0 , 0]) # 4
lieu_dir.append([1 , 8 , 6 , 4 , 0 , 0]) # 5
lieu_dir.append([2 , 9 , -10 , 5 , 0 , 0]) # 6
lieu_dir.append([4 , 16 , 8 , 0 , 0 , 0]) # 7
lieu_dir.append([5 , 0 , 9 , 7 , 0 , 0]) # 8
lieu_dir.append([6 , 0 , 0 , 8 , 0 , 0]) # 9
lieu_dir.append([0 , 12 , 11 , 6 , 0 , 0]) # 10
lieu_dir.append([0 , 13 , 0 , 10 , 0 , 0]) # 11
lieu_dir.append([10 , 14 , 13 , 0 , 0 , 0]) # 12
lieu_dir.append([11 , 15 , 0 , 12 , 0 , 0]) # 13
lieu_dir.append([12 , 0 , 15 , 0 , 0 , 0]) # 14
lieu_dir.append([13 , 0 , 0 , 14 , 0 , 0]) # 15
lieu_dir.append([7 , 0 , 0 , 0 , 0 , 0]) # 16
lieu_dir.append([16 , 19 , 18 , 0 , 0 , 0]) # 17
lieu_dir.append([0 , 20 , 0 , 17 , 0 , 0]) # 18
lieu_dir.append([17 , 0 , 20 , 0 , 0 , 0]) # 19
lieu_dir.append([18 , 0 , 0 , 19 , 0 , 0]) # 20
lieu_dir.append([0 , 23 , 22 , 0 , 20 , 0]) # 21
lieu_dir.append([0 , 24 , 0 , 21 , 0 , 0]) # 22
lieu_dir.append([21 , 0 , 24 , 0 , 0 , 0]) # 23
lieu_dir.append([22 , 25 , 0 , 23 , 0 , 0]) # 24
lieu_dir.append([24 , 0 , 0 , 0 , 0 , 0]) # 25
lieu_dir.append([0 , 0 , 0 , 0 , 0 , 22]) # 26

max_lieux = 26

lieu_bis = []
i = 0
while i < 27:
	lieu_bis.append("")
	i += 1

verb = []
verb.append("") # 0, non exploité
verb.append(" N NORD AVANCE AVANCER ") # 1
verb.append(" S SUD RECULE RECULER ") # 2
verb.append(" E EST DROITE ") # 3
verb.append(" O OUEST GAUCHE ") # 4
verb.append(" H HAUT MONTE MONTER ") # 5
verb.append(" B BAS DESCENDS DESCENDRE ") # 6
verb.append(" PRENDS PRENDRE RECUPERE RECUPERER RAMASSE RAMASSER") # 7
verb.append(" JETTE JETER POSE POSER ") # 8
verb.append(" I INVENTAIRE ") # 9
verb.append(" Q QUITTE QUITTER FIN ARRET ARRETE ARRETER ") # 10
verb.append(" VOIS VOIR VUE ") # 11
verb.append(" EXAMINE EXAMINER REGARDE REGARDER OBSERVE OBSERVER ") # 12
verb.append(" FOUILLE FOUILLER ") # 13
verb.append(" PARLE PARLER ") # 14
verb.append(" DIS DIRE ") # 15
verb.append(" INTERROGE INTERROGER ") # 16
verb.append(" DONNE DONNER OFFRE OFFRIR ") # 17
verb.append(" TAILLE TAILLER SCULPTE SCULPTER ") # 18
verb.append(" SONDE SONDER ") # 19
verb.append(" PAYE PAYER SOUDOIE SOUDOYER ") # 20
verb.append(" ACHETTE ACHETER ") # 21
verb.append(" ECHANGE ECHANGER ") # 22
verb.append(" TIRE TIRER ") # 23
verb.append(" OUVRE OUVRIR REOUVRE REOUVRIR ROUVRIR ") # 24
verb.append(" FERME FERMER REFERME REFERMER ") # 25
verb.append(" BOIS BOIRE ") # 26
verb.append(" MANGE MANGER ") # 27
verb.append(" CREUSE CREUSER ") # 28
verb.append(" POUSSE POUSSER ") # 29
verb.append(" FRAPPE FRAPPER ") # 30
verb.append(" TUE TUER ") # 31
verb.append(" ASSOCIE ASSOCIER ATTACHE ATTACHER LIE LIER ASSEMBLE ASSEMBLER ") # 32
verb.append(" AIDE AIDER HELP ") # 33

verb_count = 33

verb_list = "NORD, SUD, EST, OUEST, HAUT, BAS, PRENDRE, JETER, INVENTAIRE, QUITTER, VOIR, EXAMINER, FOUILLER, PARLER, DIRE...A, INTERROGER...SUR, DONNER...A, \
TAILLER...AVEC, SONDER, PAYER, ACHETER, ECHANGER...CONTRE, TIRER, POUSSER, OUVRIR, FERMER, BOIRE, MANGER, CREUSER, FRAPPER, TUER, ASSEMBLER/LIER...AVEC. <Flêche haut et bas>"

# obj_param :  n° de lieu = 0 pour inexistant, 255 pour 'en inventaire', 256 pour 'utilisé', Saisie = 0 pour insaisissable, 1 pour saisissable, 2 pour personnage, Gendre = 1 masculin, 0 féminin, 2 pluriel
obj = []
obj_param = []
obj.append(["" , ""]) # 0, non exploité
obj_param.append([0 , 0 , 0]) # 0, non exploité
obj.append(["ARBRE" , "un arbre"]) # 1
obj_param.append([1 , 0 , 1])
obj.append(["BRANCHE" , "une branche"]) # 2
obj_param.append([0 , 1 , 0])
obj.append(["BATON" , "un bâton"]) # 3
obj_param.append([0 , 1 , 1])
obj.append(["CORDELETTE" , "une cordelette"]) # 4
obj_param.append([3 , 0 , 0])
obj.append(["COFFRET" , "un coffret"]) # 5
obj_param.append([0 , 0 , 1])
obj.append(["CLE DE BRONZE" , "une clé de bronze"]) # 6
obj_param.append([0 , 1 , 0])
obj.append(["PUITS" , "un puits"]) # 7
obj_param.append([4 , 0 , 1])
obj.append(["PIECE D'OR" , "une pièce d'or"]) # 8
obj_param.append([0 , 1 , 0])
obj.append(["BARBARE" , "un barbare"]) # 9
obj_param.append([5 , 2 , 1])
obj.append(["SOLDAT" , "un soldat"]) # 10
obj_param.append([6 , 2 , 1])
obj.append(["LAC" , "un lac"]) # 11
obj_param.append([7 , 0 , 1])
obj.append(["SQUELETTE" , "un squelette"]) # 12
obj_param.append([9 , 0 , 1])
obj.append(["RUBIS" , "un rubis"]) # 13
obj_param.append([0 , 1 , 1])
obj.append(["CORDON" , "un cordon"]) # 14
obj_param.append([0 , 1 , 1])
obj.append(["DAGUE" , "une dague"]) # 15
obj_param.append([0 , 1 , 0])
obj.append(["LANCE" , "une lance"]) # 16
obj_param.append([0 , 1 , 0])
obj.append(["CLE D'ARGENT" , "une clé d'argent"]) # 17
obj_param.append([0 , 1 , 0])
obj.append(["EAU" , "de l'eau"]) # 18
obj_param.append([7 , 0 , 0])
obj.append(["SOLDATS" , "des soldats"]) # 19
obj_param.append([10 , 2 , 2])
obj.append(["LIERE" , "du lière"]) # 20
obj_param.append([11 , 0 , 1])
obj.append(["PRINCE" , "le Prince"]) # 21
obj_param.append([12 , 2 , 1])
obj.append(["FEMME" , "une femme"]) # 22
obj_param.append([13 , 2 , 0])
obj.append(["INSECTE" , "un insecte"]) # 23
obj_param.append([16 , 2 , 1])
obj.append(["CLE D'OR" , "une clé d'or"]) # 24
obj_param.append([0 , 1 , 0])
obj.append(["GUERRIER" , "un guerrier"]) # 25
obj_param.append([18 , 2 , 1])
obj.append(["ACIDE" , "de l'acide"]) # 26
obj_param.append([0 , 1 , 1])
obj.append(["DRAGON" , "un dragon"]) # 27
obj_param.append([19 , 2 , 1])
obj.append(["BARREAU" , "un barreau"]) # 28
obj_param.append([0 , 1 , 1])
obj.append(["PORTE" , "une porte"]) # 29
obj_param.append([20 , 0 , 0])
obj.append(["MURET" , "un muret"]) # 30
obj_param.append([17 , 0 , 1])
obj.append(["ROUAGE" , "un rouage"]) # 31
obj_param.append([21 , 0 , 1])
obj.append(["LEVIER" , "un levier"]) # 32
obj_param.append([0 , 0 , 1])
obj.append(["PORTE DE BRONZE" , "une porte de bronze"]) # 33
obj_param.append([22 , 0 , 0])
obj.append(["ARAIGNEE" , "une araignée"]) # 34
obj_param.append([23 , 2 , 0])
obj.append(["EPEE" , "une épée"]) # 35
obj_param.append([24 , 1 , 0])
obj.append(["COFFRE" , "un coffre"]) # 36
obj_param.append([25 , 2 , 1])
obj.append(["BOURSE" , "une bourse"]) # 37
obj_param.append([0 , 1 , 0])

obj_count = 37

coffret_ouvert = False
epee_retiree = False
coffre_ouvert = False

# Initialiser les fonts et la fenêtre
try:
    screen = pygame.display.set_mode([screen_width,screen_height]) # , pygame.FULLSCREEN)
except:
    screen_width = 640
    screen_height = 480
    screen_txt_y = 290
    screen_txt_height = 156
    screen_image_x = 160
    screen_image_y = 16
    intro_image_x = 160
    intro_image_y = 0
    font_size = 14
    mini = "mini"
    screen = pygame.display.set_mode([screen_width,screen_height] , pygame.FULLSCREEN)

pygame.display.set_caption("Désert de feu")
police = pygame.font.Font(pygame.font.get_default_font() , font_size)
police_height = pygame.font.Font.get_linesize(police)
lines_count = math.floor(screen_txt_height / police_height)
buffer = []
lc = lines_count
while lc > 0:
    buffer.append(" ")
    lc -= 1

# Charger le fond d'écran et l'image d'introduction
screen_img = pygame.image.load("images/" + mini + "ecran.png").convert()
intro_img = pygame.image.load("images/" + mini + "intro.jpg").convert()

# Introduction active
intro = True
fin = False
sound_queue = 0

# Autoriser à charger un écran de jeu ?
load_scn = False

# Boucler tant que 'done = False'
done = False

clock = pygame.time.Clock()

# Fonction d'affichage des graphismes
def UpdateGraphics(img1 , img2):
    screen.blit(img1 , (0 , 0))
    screen.blit(img2 , (screen_image_x , screen_image_y))

# Fonction d'affichage du buffer texte
def Afficher_Buffer(buf , ph , lc , ln):
    i = 0
    while (i < lc):
        c = buf[i]
        try:
            if isinstance(c, unicode) == False:
                c = unicode(c , 'utf-8')
        except:
            c = c # Vérifier sur python 2.7.4 le prends
        txt = police.render(c , True , greentxt , green)
        screen.blit(txt , (2 , ln))
        ln += ph
        i +=1

# Fonction de décalage du buffer texte
def ScrollBuffer(n , buf , lc):
    while n > 0:
        i = 0
        while i < lc - 1:
            buf[i] = buf[i + 1]
            i +=1
        buf[i] = ""
        n -= 1

# Retourne la position Y en pixels d'une ligne numéro i
def YPos(i , ph , ln):
    i = ln + (i * ph)
    return(i)

# Fonction de distribution d'un texte dans le buffer
def Ajouter_Texte(buf , phr1 , ln , lc):
    phr2 = ""
    i = ln
    while len(phr1) > 0:
        if i == lc:
            ScrollBuffer(1 , buf , lc)
            i -= 1
        w , h = police.size(phr1)
        if w > screen_width - 4:
            while w > screen_width - 4:
                l = len(phr1) - 1
                phr2 = phr1[l:] + phr2
                phr1 = phr1[:l]
                w , h = police.size(phr1)
            l = len(phr1) - 1
            ch = phr1[l:]
            while ch != " ":
                phr2 = phr1[l:] + phr2
                phr1 = phr1[:l]
                l = len(phr1) - 1
                ch = phr1[l:]                
        buf[i] = phr1
        i += 1
        phr1 = phr2
        phr2 = ""
    return(i)

# Afficher la commande tapée en cours
def Affiche_Commande(c , y):
    txt = police.render(c , True , greentxt , green)
    screen.blit(txt , (2 , y))

# Décomposer une phrase et retourner le verbe et les objets
def Decompose(phr):
    phr = " ".join(phr.split())
    phr = phr.strip()
    cc = ""
    if phr == "":
        return("" , "" , "" , cc)
    vbs = ""
    ob1s = ""
    ob2s = ""
    while phr != "" and phr[:1] != " ":
        vbs += phr[:1]
        phr = phr[1:]
    phr = phr.strip()
    if phr == "":
        return(vbs , "" , "" , cc)
    while phr != "" and phr[:1] != " ":
        ob1s += phr[:1]
        phr = phr[1:]
    phr = phr.strip()
    if ob1s == "L'" or ob1s == "LE" or ob1s == "LA" or ob1s == "LES" or ob1s == "A" or ob1s == "AU" or ob1s == "AUX" or ob1s == "AVEC" \
        or ob1s == "CE" or ob1s == "CET" or ob1s == "CETTE" or ob1s == "CES" \
        or ob1s == "UN" or ob1s == "UNE" or ob1s == "DES" \
        or ob1s == "MON" or ob1s == "MA" or ob1s == "MES" \
        or ob1s == "TON" or ob1s == "TA" or ob1s == "TES" \
        or ob1s == "SON" or ob1s == "SA" or ob1s == "SES" \
        or ob1s == "DU":
            if ob1s != "L'":
                ob1s += " "
    else:
        ob1s += " "
    phr = phr.strip()
    if phr == "":
        return(vbs , ob1s.strip() , "" , cc)
    while phr != "" and phr[:3] != "ET " and phr[:5] != "AVEC " and phr[:2] != "A " and phr[:3] != "AU " and phr[:4] != "AUX " and phr[:4] != "SUR " and phr[:7] != "CONTRE ":
        ob1s += phr[:1]
        phr = phr[1:]
    phr = phr.strip()

    if phr == "":
        return(vbs , ob1s.strip() , "" , cc)
    else:
        if phr[:3] == "ET ":
            phr = phr[3:]
            cc = "ET"
        elif phr[:5] == "AVEC ":
            phr = phr[5:]
            cc = "AVEC"
        elif phr[:2] == "A ":
            phr = phr[2:]
            cc = "A"
        elif phr[:3] == "AU ":
            phr = phr[3:]
            cc = "AU"
        elif phr[:4] == "AUX ":
            phr = phr[4:]
            cc = "AUX"
        elif phr[:4] == "SUR ":
            phr = phr[4:]
            cc = "SUR"
        elif phr[:7] == "CONTRE ":
            phr = phr[7:]
            cc = "CONTRE"
    phr = phr.strip()
    ob1s = ob1s.strip()
    if phr == "":
        return(vbs , ob1s , "" , cc)
    ob2s = phr
    return(vbs , ob1s , ob2s , cc)

# Trouver un verbe dans une table de verbes
def TrouveVerbe(v , tv , count):
    i = 1
    while i <= count:
        if " " + v + " " in tv[i]:
            return(i)
        i += 1
    return(0)

# Trouver un objet dans une liste d'objets
def TrouveObjet(o , to , count):
    i = 1
    while i <= count:
        a = to[i][0]
        art = ""
        if a in o:
            if o[:2] == "L'":
                art = o[:2]
            if o[:3] == "LE ":
                art = o[:3]
            if o[:3] == "LA ":
                art = o[:3]
            if o[:4] == "LES ":
                art = o[:4]
            if o[:2] == "A ":
                art = o[:2]
            if o[:3] == "AU ":
                art = o[:3]
            if o[:4] == "AUX ":
                art = o[:4]
            if o[:5] == "AVEC ":
                art = o[:5]
            if o[:3] == "CE ":
                art = o[:3]
            if o[:4] == "CET ":
                art = o[:4]
            if o[:6] == "CETTE ":
                art = o[:6]
            if o[:4] == "CES ":
                art = o[:4]
            if o[:3] == "UN ":
                art = o[:3]
            if o[:4] == "UNE ":
                art = o[:4]
            if o[:4] == "DES ":
                art = o[:4]
            if o[:4] == "MON ":
                art = o[:4]
            if o[:3] == "MA ":
                art = o[:3]
            if o[:4] == "MES ":
                art = o[:4]
            if o[:4] == "TON ":
                art = o[:4]
            if o[:3] == "TA ":
                art = o[:3]
            if o[:4] == "TES ":
                art = o[:4]
            if o[:4] == "SON ":
                art = o[:4]
            if o[:3] == "SA ":
                art = o[:3]
            if o[:4] == "SES ":
                art = o[:4]
            if o[:3] == "DU ":
                art = o[:3]
            if o[:6] == "DE LA ":
                art = o[:6]
            if o[:5] == "DE L'":
                art = o[:5]
            l = len(art)
            if a == o or o == art + a:
                return(i)
        i += 1
    return(0)

# Cacher le pointeur de la souris
pygame.mouse.set_visible(False)

# Memoriser le dernier événement keyboard frappé
evk = pygame.K_RETURN

# Delay de touche désactivé
dl = 10000

# ******************** Boucle principale ********************
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Quitte l'app par fermeture
            done = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN: # Valider
                if intro == True:
                    intro = False
                    lieu = 1
                    load_scn = True
                    reset_descr = True
                    exCMD = ""
                    CMD = ""
                    CMD_to_execute = ""
                    Ready = True
                elif fin == True:
                    done = True
                elif Ready == True:
                    Ready = False
                    CMD_to_execute = CMD
                    buffer[ligne] = CMD
                    exCMD = CMD
                    CMD = ""
                    ligne += 1
            elif event.key == pygame.K_UP: # Rappeler la dernière commande
                if intro ==False and Ready == True:
                    CMD = exCMD
            elif event.key == pygame.K_DOWN: # Effacer la commande en cours
                if intro ==False and Ready == True:
                    CMD = ""
            elif event.key == pygame.K_BACKSPACE:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_4:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_SPACE:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_QUOTE:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_a:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_b:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_c:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_d:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_e:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_f:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_g:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_h:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_i:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_j:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_k:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_l:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_m:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_SEMICOLON:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_n:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_o:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_p:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_q:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_r:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_s:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_t:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_u:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_v:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_w:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_x:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_y:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
            elif event.key == pygame.K_z:
                evk = pygame.K_RETURN
                dl = 10000
                memchar = ""
        if event.type == pygame.KEYDOWN: # Quitte l'app par 'ESC'
            if event.key == pygame.K_ESCAPE:
                done = True
            if intro == False and Ready == True:
                if event.key == pygame.K_BACKSPACE and evk != pygame.K_BACKSPACE:
                    if len(CMD) > 0:
                        l = len(CMD) - 1
                        CMD = CMD[:l]
                    evk = pygame.K_BACKSPACE
                    dl = 250
                    char = ""
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_SPACE and evk != pygame.K_SPACE:
                    char = event.dict['unicode']
                    evk = pygame.K_SPACE
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_4 and evk != pygame.K_4:
                    char = event.dict['unicode']
                    evk = pygame.K_4
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_QUOTE and evk != pygame.K_QUOTE:
                    char = event.dict['unicode']
                    evk = pygame.K_QUOTE
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_a and evk != pygame.K_a:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_a
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_b and evk != pygame.K_b:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_b
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_c and evk != pygame.K_c:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_c
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_d and evk != pygame.K_d:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_d
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_e and evk != pygame.K_e:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_e
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_f and evk != pygame.K_f:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_f
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_g and evk != pygame.K_g:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_g
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_h and evk != pygame.K_h:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_h
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_i and evk != pygame.K_i:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_i
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_j and evk != pygame.K_j:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_j
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_k and evk != pygame.K_k:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_k
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_l and evk != pygame.K_l:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_l
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_m and evk != pygame.K_m:
                    char = "M"
                    evk = pygame.K_m
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_SEMICOLON and evk != pygame.K_SEMICOLON:
                    char = "M"
                    evk = pygame.K_SEMICOLON
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_n and evk != pygame.K_n:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_n
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_o and evk != pygame.K_o:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_o
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_p and evk != pygame.K_p:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_p
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_q and evk != pygame.K_q:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_q
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_r and evk != pygame.K_r:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_r
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_s and evk != pygame.K_s:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_s
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_t and evk != pygame.K_t:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_t
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_u and evk != pygame.K_u:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_u
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_v and evk != pygame.K_v:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_v
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_w and evk != pygame.K_w:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_w
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_x and evk != pygame.K_x:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_x
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_y and evk != pygame.K_y:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_y
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                elif event.key == pygame.K_z and evk != pygame.K_z:
                    char = event.dict['unicode'].upper()
                    evk = pygame.K_z
                    dl = 250
                    millisecs = int(round(time.time() * 1000))
                memchar = char

    # *** Répéter les touches appuyées ***
    if intro == False and Ready == True and dl != 10000:
        dl = dl - (int(round(time.time() * 1000)) - millisecs)
        if dl <= 0:
            char = ""
            if evk == pygame.K_BACKSPACE:
                if len(CMD) > 0:
                    l = len(CMD) - 1
                    CMD = CMD[:l]
                char = memchar
            elif evk == pygame.K_SPACE:
                char = memchar
            elif evk == pygame.K_4:
                char = memchar
            elif evk == pygame.K_QUOTE:
                char = memchar
            elif evk == pygame.K_a:
                char = memchar
            elif evk == pygame.K_b:
                char = memchar
            elif evk == pygame.K_c:
                char = memchar
            elif evk == pygame.K_d:
                char = memchar
            elif evk == pygame.K_e:
                char = memchar
            elif evk == pygame.K_f:
                char = memchar
            elif evk == pygame.K_g:
                char = memchar
            elif evk == pygame.K_h:
                char = memchar
            elif evk == pygame.K_i:
                char = memchar
            elif evk == pygame.K_j:
                char = memchar
            elif evk == pygame.K_k:
                char = memchar
            elif evk == pygame.K_l:
                char = memchar
            elif evk == pygame.K_m:
                char = memchar
            elif evk == pygame.K_SEMICOLON:
                char = memchar
            elif evk == pygame.K_n:
                char = memchar
            elif evk == pygame.K_o:
                char = memchar
            elif evk == pygame.K_p:
                char = memchar
            elif evk == pygame.K_q:
                char = memchar
            elif evk == pygame.K_r:
                char = memchar
            elif evk == pygame.K_s:
                char = memchar
            elif evk == pygame.K_t:
                char = memchar
            elif evk == pygame.K_u:
                char = memchar
            elif evk == pygame.K_v:
                char = memchar
            elif evk == pygame.K_w:
                char = memchar
            elif evk == pygame.K_x:
                char = memchar
            elif evk == pygame.K_y:
                char = memchar
            elif evk == pygame.K_z:
                char = memchar
            millisecs = int(round(time.time() * 1000))
            dl = 120
        
    # *** Tracer des graphismes ***
    if intro == True:
        screen.fill(black) # Dessiner l'écran d'introduction
        screen.blit(intro_img , (intro_image_x , intro_image_y))
    else:
        if load_scn == True:
            filename = "images/" + mini + str(lieu) + lieu_bis[lieu] + ".jpg"
            temp_scn = pygame.image.load(filename).convert() # Charger le décors le plus récent si nécessaire
            if lieu == 16 and sound[0] == False: # Jouer les sons de début de lieu
                sound[0] = True
                sound_0.play()
            load_scn = False
        if reset_descr == True:
            i = 0
            while i < lines_count:
                buffer[i] = ""
                i +=1
            ligne = 0
            ligne = Ajouter_Texte(buffer , lieu_descr[lieu] , ligne , lines_count)
            directions = ""
            if lieu_dir[lieu][0] > 0:
                directions += "au Nord, "
            if lieu_dir[lieu][1] > 0:
                directions += "au Sud, "
            if lieu_dir[lieu][2] > 0:
                directions += "à l'Est, "
            if lieu_dir[lieu][3] > 0:
                directions += "à l'Ouest, "
            if lieu_dir[lieu][4] > 0:
                directions += "en Haut, "
            if lieu_dir[lieu][5] > 0:
                directions += "en Bas, "
            if directions == "":
                directions == "Nulle part"
            else:
                directions = directions[:len(directions) - 2]
            ligne = Ajouter_Texte(buffer , "Vous pouvez aller " + directions , ligne , lines_count)
            ligne = Ajouter_Texte(buffer , "Vous voyez :" , ligne , lines_count)
            liste_objets = ""
            i = 1
            while i <= obj_count:
                if obj_param[i][0] == lieu:
                    liste_objets += obj[i][1] + ", "
                i += 1
            l = len(liste_objets)
            cr = liste_objets[:1].upper()
            liste_objets = cr + liste_objets[1:l - 2]
            if liste_objets == "":
                liste_objets = "Rien de spécial."
            ligne = Ajouter_Texte(buffer , liste_objets , ligne , lines_count)
            if fin == False:
                ligne = Ajouter_Texte(buffer , "Que voulez-vous faire ?" , ligne , lines_count)
            else:
                ligne = Ajouter_Texte(buffer , "Vous avez triomphé, vous vous êtes enfui du désert !" , ligne , lines_count)
            reset_descr = False
            char = ""
        UpdateGraphics(screen_img , temp_scn)
        Afficher_Buffer(buffer , police_height , lines_count , screen_txt_y)
        if Ready == True and fin == False:
            w , h = police.size(CMD + char + "_")
            if w <= screen_width - 4:
                CMD += char
                char = ""
                Affiche_Commande(CMD + "_" , YPos(ligne , police_height , screen_txt_y))
        elif fin == True:
            fin = True
        else:
            # Exécuter une commande interprétée
            vbs , ob1s , ob2s , cc  = Decompose(CMD_to_execute)
            vb = TrouveVerbe(vbs , verb , verb_count)
            ob1 = TrouveObjet(ob1s , obj , obj_count)
            ob2 = TrouveObjet(ob2s , obj , obj_count)
            CMD = ""
            CMD_to_execute = ""
            MSG = ""
            if vb == 0: # Pas de verbe trouvé
                if vbs != "":
                        MSG = "Je ne comprends pas."
            elif vb == 1: # Nord
                if ob1 == 0 and ob2 == 0:
                    if lieu_dir[lieu][0] > 0:
                        lieu = lieu_dir[lieu][0]
                        load_scn = True
                        reset_descr = True
                    else:
                        MSG = "Je ne peux pas aller par là."
                else:
                    MSG = "Je ne comprends pas."
            elif vb == 2: # Sud
                if ob1 == 0 and ob2 == 0:
                    if lieu_dir[lieu][1] > 0:
                        lieu = lieu_dir[lieu][1]
                        load_scn = True
                        reset_descr = True
                    else:
                        MSG = "Je ne peux pas aller par là."
                else:
                    MSG = "Je ne comprends pas."
            elif vb == 3: # Est
                if ob1 == 0 and ob2 == 0:
                    if lieu_dir[lieu][2] > 0:
                        lieu = lieu_dir[lieu][2]
                        load_scn = True
                        reset_descr = True
                    else:
                        MSG = "Je ne peux pas aller par là."
                else:
                    MSG = "Je ne comprends pas."
            elif vb == 4: # Ouest
                if ob1 == 0 and ob2 == 0:
                    if lieu_dir[lieu][3] > 0:
                        lieu = lieu_dir[lieu][3]
                        load_scn = True
                        reset_descr = True
                    else:
                        MSG = "Je ne peux pas aller par là."
                else:
                    MSG = "Je ne comprends pas."
            elif vb == 5: # Haut
                if ob1 == 0 and ob2 == 0:
                    if lieu_dir[lieu][4] > 0:
                        lieu = lieu_dir[lieu][4]
                        load_scn = True
                        reset_descr = True
                        if lieu == 26 and sound[1] == False:
                            sound[1] = True
                            end_sound.play()
                            fin = True
                    else:
                        MSG = "Je ne peux pas aller par là."
                else:
                    MSG = "Je ne comprends pas."
            elif vb == 6: # Bas
                if ob1 == 0 and ob2 == 0:
                    if lieu_dir[lieu][5] > 0:
                        lieu = lieu_dir[lieu][5]
                        load_scn = True
                        reset_descr = True
                    else:
                        MSG = "Je ne peux pas aller par là."
                else:
                    MSG = "Je ne comprends pas."
            elif vb == 7: # Prendre
                if ob1 > 0 and ob2s == "":
                    if obj_param[ob1][2] == 0:
                        article = "la"
                    elif obj_param[ob1][2] == 1:
                        article = "le"
                    else:
                        article = "les"
                    if obj_param[ob1][0] == lieu and obj_param[ob1][1] == 1:
                        if ob1 == 35 and epee_retiree == False:
                            epee_retiree = True
                            lieu_bis[24] = "bis"
                            load_scn = True
                            obj_param[ob1][0] = 255
                            MSG = "Au moment où vous prenez l'épée, vous entendez un sourd grondement mécanique."
                            sound_1.play()
                        else:
                            obj_param[ob1][0] = 255
                            MSG = "Vous " + article + " prenez."
                    elif obj_param[ob1][0] != lieu:
                        MSG = "Cet objet n'est pas ici."
                    else:
                        MSG = "Vous ne pouvez pas " + article +" prendre."
                elif ob1 == 0 and ob2 == 0 and ob1s != "":
                    MSG = "Il n'y a pas de ça ici."
                elif ob1 == 0 and ob2 == 0 and ob1s == "":
                    MSG = "Que voulez-vous prendre ?"
                else:
                    MSG = "Je ne comprends pas."
            elif vb == 8: # Jeter
                if ob1 > 0 and ob2s == "":
                    if obj_param[ob1][2] == 0:
                        article = "la"
                    elif obj_param[ob1][2] == 1:
                        article = "le"
                    else:
                        article = "les"
                    if obj_param[ob1][0] == 255 and obj_param[ob1][1] == 1:
                        obj_param[ob1][0] = lieu
                        MSG = "Vous " + article + " jetez."
                    elif obj_param[ob1][0] != 255:
                        MSG = "Vous ne possédez pas cet objet."
                    else:
                        MSG = "Vous ne pouvez pas " + article +" jeter."
                elif ob1 == 0 and ob2 == 0 and ob1s != "":
                    MSG = "Vous ne possédez pas cet objet."
                elif ob1 == 0 and ob2 == 0 and ob1s == "":
                    MSG = "Que voulez-vous jeter ?"
                else:
                    MSG = "Je ne comprends pas."
            elif vb == 9: # Inventaire
                if ob1 ==0 and ob2 == 0:
                    inventaire = ""
                    i = 1
                    while i <= obj_count:
                        if obj_param[i][0] == 255:
                            inventaire += obj[i][1] + ", "
                        i += 1
                    l = len(inventaire)
                    cr = inventaire[:1].upper()
                    inventaire = cr + inventaire[1:l - 2]
                    if inventaire == "":
                        inventaire = "Rien du tout."
                    ligne = Ajouter_Texte(buffer , "Vous possédez :" , ligne , lines_count)
                    ligne = Ajouter_Texte(buffer , inventaire , ligne , lines_count)
            elif vb == 10: # Quitter
                if ob1 == 0 and ob2 == 0:
                    done = True
                else:
                    MSG = "Je ne comprends pas."
            elif vb == 11: # Voir
                if ob1 == 0 and ob2 == 0:
                    load_scn = True
                    reset_descr = True
                else:
                    MSG = "Je ne comprends pas."
            elif vb == 12: # Examiner
                if ob1 == 1 and ob2s == "":
                    if obj_param[1][0] == lieu:
                        if obj_param[2][0] == 0:
                            obj_param[2][0] = 1
                            MSG = "Ses branches sont assez robustes. L'une d'entre elles est à votre portée."
                        else:
                            MSG = "Ses branches sont assez robustes, et étonnamment touffues."                            
                    else:
                        MSG = "Cet objet n'est pas ici."
                elif ob1 == 2 and ob2s == "":
                    if obj_param[2][0] == 255:
                        MSG = "Cette branche, une fois taillée, pourrait vous servir d'arme pour vous défendre dans ces contrées hostiles."
                    elif obj_param[2][0] == lieu:
                        MSG = "C'est une branche d'arbre, assez solide."
                    else:
                        MSG = "Cet objet n'est pas ici."
                elif ob1 == 4 and ob2s == "":
                    if obj_param[4][0] == lieu:
                        MSG = "Cette cordelette sort de sous la terre."
                    else:
                        MSG = "Cet objet n'est pas ici."
                elif ob1 == 5 and ob2s == "":
                    if obj_param[5][0] == lieu:
                        MSG = "Ce coffret est en bois et en métal, et il est orné d'une pierre bleue."
                    else:
                        MSG = "Cet objet n'est pas ici."
                elif ob1 == 6 and ob2s == "":
                    if obj_param[6][0] == 255 or obj_param[6][0] == lieu:
                        MSG = "Cette clé est faite de bronze. Quelle serrure peut-elle bien ouvrir ?"
                    else:
                        MSG = "Cet objet n'est pas ici."
                elif ob1 == 7 and ob2s == "":
                    if obj_param[7][0] == lieu:
                        if obj_param[8][0] == 0:
                            obj_param[8][0] = 255
                            MSG = "En tâtonnant un peu les pierres qui le constituent, vous sentez que \
l'une d'entre elles bouge partiellement. Vous en retirez avec patience la partie mobile, et derrière ce \
fragment de roche se trouve une pièce d'or, que vous vous empressez d'empocher."
                        else:
                            MSG = "Vous ne découvrez rien de plus."
                    else:
                        MSG = "Il n'est pas ici."
                elif ob1 == 9 and ob2s == "":
                    if obj_param[9][0] == lieu:
                        MSG = "Malgré son aspect effrayant dû à son accoutrement et à sa musculature imposante, ce barbare vous semble amical."
                    else:
                        MSG = "Il n'est pas ici."
                elif ob1 == 10 and ob2s == "":
                    if obj_param[10][0] == lieu:
                        MSG = "Ce soldat garde l'entrée au château."
                    else:
                        MSG = "Il n'est pas ici."
                elif ob1 == 11 and ob2s == "":
                    if obj_param[11][0] == lieu:
                        MSG = "Ce lac semble trop profond pour s'y baigner, mais vous-y avez pied tout au long de sa bordure."
                    else:
                        MSG = "Il n'est pas ici."
                elif ob1 == 20 and ob2s == "":
                    if obj_param[20][0] == lieu:
                        if obj_param[14][0] == 0:
                            obj_param[14][0] = 255
                            MSG = "Dans le lière, vous trouvez un cordon que quelqu'un avait sûrement caché là. Vous le prenez."
                        else:
                            MSG = "Vous ne trouvez rien de plus."
                    else:
                        MSG = "Il n'est pas ici."
                elif ob1 == 22 and ob2s == "":
                    if obj_param[22][0] == lieu:
                        MSG = "Cette femme est étrangement habillée. Elle cache à demi son visage à l'aide d'une capuche."
                    else:
                        MSG = "Elle n'est pas ici."
                elif ob1 == 31 and ob2s == "":
                    if obj_param[31][0] == lieu:
                        MSG = "Ce mécanisme est équipé d'un trou qui sert d'emplacement pour quelque chose comme un levier."
                    else:
                        MSG = "Il n'est pas ici."
                elif ob1 ==0 and ob2 ==0 and ob1s != "":
                    MSG = "Je ne vois pas de ça ici."
                elif ob1 ==0 and ob2 ==0 and ob1s == "":
                    MSG = "Que voulez-vous examiner ?"
                elif ob2s != "" or cc != "":
                    MSG = "Je ne comprends pas."
                else:
                    MSG = "Il n'y a rien de spécial."
            elif vb == 13: # Fouiller
                if ob1 == 12 and ob2s == "":
                    if obj_param[12][0] == lieu:
                        if obj_param[13][0] == 0:
                            MSG = "Vous fouillez tant bien que mal le squelette en vous bouchant le nez d'une main, et tandis \
que vous en soulevez le crâne de l'autre, vous y trouvez dessous un rubis que vous récupérez."
                            obj_param[13][0] = 255
                        else:
                            MSG = "Vous ne trouvez plus rien."
                    else:
                        MSG = "Il n'est pas ici."
                elif ob1 == 0 and ob2 == 0 and ob1s != "":
                    MSG = "Je ne vois pas de ça ici."
                elif ob1 == 0 and ob2 == 0 and ob1s == "":
                    MSG = "Que voulez-vous fouiller ?"
                elif ob2 > 0:
                    MSG = "Je ne comprends pas."
                else:
                    MSG = "Vous ne pouvez pas."
            elif vb == 14: # Parler
                if ob1 == 9 and ob2s == "":
                    if obj_param[9][0] == lieu:
                        MSG = "Bonjour l'inconnu."
                    else:
                        MSG = "Il n'est pas ici."
                elif ob1 == 10 and ob2s == "":
                    if obj_param[10][0] == lieu:
                        if obj_param[8][0] != 256:
                            MSG = "Bonjour, jeune homme. Il faut payer pour entrer ici."
                        else:
                            MSG = "Bienvenue au château de Gmell."
                    else:
                        MSG = "Il n'est pas ici."
                elif ob1 == 19 and ob2s == "":
                    if obj_param[19][0] == lieu:
                        MSG = "Bienvenue au château de Gmell."
                    else:
                        MSG = "Ils ne sont pas ici."
                elif ob1 == 11 and ob2s == "":
                    if obj_param[11][0] == lieu:
                        MSG = "Le lac parle ?! Il vous dit : Sondes-moi... Sondes-moi..."
                    else:
                        MSG = "Il n'est pas ici."
                elif ob1 == 22 and ob2s == "":
                    if obj_param[22][0] == lieu:
                        if obj_param[13] != 256:
                            MSG = "Bonjour, étranger. M'échangerais-tu un objet précieux contre une dague de bonne facture ?"
                        else:
                            MSG = "Merci, étranger, pour cette transaction. Elle te sera sûrement utile."
                    else:
                        MSG = "Elle n'est pas ici."
                elif ob1 == 21 and ob2s == "":
                    if obj_param[21][0] == lieu:
                        if lieu_bis[19] == "":
                            MSG = "Bonjour étranger. Vous vous demandez peut-être ce qui me tracasse ? Il y a un dragon qui à fait \
beaucoup de dégâts par ici. J'offrirai une belle récompense à celui qui m'en débarassera."
                        elif lieu_bis[19] == "bis" and obj_param[24][0] == 0:
                            MSG = "Bravo mon cher, voici votre récompense pour avoir tué cet horrible dragon : Une clé faite d'or qui vous sera sûrement très utile."
                            obj_param[24][0] = 255
                        else:
                            MSG = "Merci étranger pour ce que vous avez fait pour le royaume perdu de Gmell."
                    else:
                        MSG = "Il n'est pas ici."
                elif ob1 == 25 and ob2s == "":
                    if obj_param[25][0] == lieu:
                        if obj_param[16][0] < 255:
                            MSG = "Bonjour, étranger !"
                        elif obj_param[16][0] == 255:
                            MSG = "Bonjour, étranger. Me donnerais-tu ta lance contre de l'acide ?"
                        elif obj_param[26][0] < 256:
                            MSG = "Merci, étranger ! J'éspère que tu verras l'utilité de cet acide."
                        else:
                            MSG = "Bravo pour tes exploits, étranger !"
                    else:
                        MSG = "Il n'est pas ici."
                elif ob1 == 0 and ob2 == 0 and ob1s != "":
                    MSG = "Je ne le/la/les vois pas ici."
                elif ob1 == 0 and ob2 == 0 and ob1s == "":
                    MSG = "Avec qui voulez-vous parler ?"
                elif ob1 > 0 and ob2 == 0:
                    MSG = "Aucune réponse."
                elif ob2 > 0:
                    MSG = "Je ne comprends pas."
                else:
                    MSG = "Vous ne pouvez pas."
            elif vb == 15: # Dire ... à, au, aux
                if ob1s > "" and ob2s == "" and cc == "":
                    MSG = "Dire quoi à qui ?"
                elif ob1s != "" and ob2s != "" and (cc == "A" or cc == "AU"):
                    if ob2s == "BARBARE" and lieu == 5:
                        if ob1s == "BONJOUR":
                            MSG = "Bonjour, l'inconnu. Vous êtes sûrement un rebelle du Nord de Forgam, vous !"
                        else:
                            MSG = "Il ne réponds pas."
                    elif ob2s == "BARBARE" and lieu != 5:
                        MSG = "Il n'est pas ici."
                    else:
                        MSG = "Vous ne pouvez pas faire cela."
                elif ob1s != "" and ob2s != "" and (cc == "AUX"):
                    if ob2s == "SOLDATS" and lieu == 10:
                        if ob1s == "BONJOUR":
                            MSG = "Bonjour, jeune homme, et bienvenue."
                        else:
                            MSG = "Ils ne répondent pas."
                    elif ob2s == "SOLDATS" and lieu != 10:
                        MSG = "Ils ne sont pas ici."
                    else:
                        MSG = "Vous ne pouvez pas faire cela."
                elif ob1 == 0 and ob2 == 0 and ob1s == "":
                    MSG = "Que voulez-vous dire et à qui ?"
                else:
                    MSG = "Je ne comprends pas."
            elif vb == 16: # Interroger ... sur
                if ob1 > 0 and ob2 > 0 and cc == "SUR":
                    if ob1 == 9 and ob2 == ob1 and obj_param[ob1][0] == lieu:
                        MSG = "Je suis né ici, j'habite par ici et j'ai appris à survivre à la force de mes muscles."
                    elif ob1 == 9 and ob2 == ob1 and obj_param[ob1][0] != lieu:
                        MSG = "Il n'est pas ici."
                    elif ob1 == 9 and ob2 == 10 and obj_param[ob1][0] == lieu:
                        MSG = "Si vous désirez rentrer dans les terres de l'Est, il vous faudra payer le soldat avec de l'or."
                    elif ob1 == 9 and ob2 == 10 and obj_param[ob1][0] != lieu:
                        MSG = "Il n'est pas ici."
                    elif ob1 == 19 and ob2 == ob1 and obj_param[ob1][0] == lieu:
                        MSG = "Nous sommes les derniers soldats du Prince Uther de Gmell."
                    elif ob1 == 19 and ob2 == ob1 and obj_param[ob1][0] != lieu:
                        MSG = "Ils ne sont pas ici."
                    else:
                        MSG = "Vous ne pouvez pas faire cela."
                elif ob1 > 0 and ob2 == 0 and cc == "":
                    MSG = "L'interroger sur quoi ?"
                elif ob1 > 0 and ob2 == 0 and cc == "SUR":
                    if ob1 == 9 and obj_param[ob1][0] == lieu:
                        if ob2s == "LE DESERT" or ob2s == "DESERT" or ob2s == "FORGAM" or ob2s == "ICI" or ob2s == "LES REBELLES" or ob2s == "REBELLE" or ob2s == "REBELLES":
                            MSG = "Ici, nous sommes dans le désert perdu de Forgam. C'est un lieu où l'on envoie ceux qui se sont rebellés contre les terres du Nord. Le \
seul échapatoire, c'est de trouver la mystérieuse porte Sud de Geofront."
                        elif ob2s == "VOUS" or ob2s == "MOI" or ob2s == "IDENTITE" or ob2s == "QUI SUIS JE" or ob2s == "QUI JE SUIS":
                            MSG = "Ha ! Vous ne savez pas qui vous êtes ? Vous êtes sûrement un rebelle, alors !"
                        elif ob2s == "GEOFRONT":
                            MSG = "Tout ce que je sais sur Geofront, c'est que cette porte est peut-être un mythe. On dit que ceux qui l'ont trouvé ne sont jamais revenus."
                        else:
                            MSG = "il ne réponds pas."
                    elif ob1 == 9 and obj_param[ob1][0] != lieu:
                        MSG = "Il n'est pas ici."
                    else:
                        MSG = "Vous ne pouvez pas faire cela."
                elif ob1 == 0 and ob2 == 0 and ob1s == "":
                    MSG = "Qui voulez-vous interroger, et avec quoi ?"
                elif ob1 == 0 and ob2 == 0 and ob1s != "":
                    MSG = "Vous ne pouvez pas l'interroger."
                else:
                    MSG = "Je ne comprends pas."
            elif vb == 17: # Donner ... à, au
                if ob1 > 0 and ob2 > 0 and (cc == "A" or cc == "AU"):
                    if ob2 == 10 and obj_param[ob2][0] == lieu:
                        if ob1 == 8 and obj_param[ob1][0] == 255:
                            obj_param[ob1][0] = 256
                            lieu_dir[lieu][2] = 10
                            MSG = "Merci d'avoir payé pour votre passage. Vous pouvez entrer au château de Gmell."
                        elif ob1 == 8 and obj_param[ob1][0] < 255:
                            MSG = "Vous n'avez pas de pièce d'or."
                        elif ob1 == 8 and obj_param[ob1][0] == 256:
                            MSG = "Vous avez déjà payé pour votre passage."
                        elif obj_param[ob1][0] != 255:
                            MSG = "Vous n'avez pas cet objet."
                        else:
                            MSG = "Il ne veut pas."
                    elif ob2 == 10 and obj_param[ob2][0] != lieu:
                        MSG = "Il n'est pas ici."
                    elif ob2 == 22 and obj_param[ob2][0] == lieu:
                        if ob1 == 13 and obj_param[ob1][0] == 255:
                            obj_param[ob1][0] = 256
                            obj_param[15][0] = 255
                            MSG = "Voici une dague. Merci pour cet échange, il vous sera certainement favorable."
                        elif ob1 == 13 and obj_param[ob1][0] < 255:
                            MSG = "Vous n'avez pas de rubis."
                        elif ob1 == 13 and obj_param[ob1][0] == 256:
                            MSG = "Vous m'avez déjà échangé le rubis contre la dague."
                        elif obj_param[ob1][0] != 255:
                            MSG = "Vous n'avez pas cet objet."
                        else:
                            MSG = "Elle ne veut pas."
                    elif ob2 == 25 and obj_param[ob2][0] == lieu:
                        if ob1 == 16 and obj_param[ob1][0] == 255:
                            obj_param[ob1][0] = 256
                            obj_param[26][0] = 255
                            MSG = "Voici de l'acide. Merci pour cet échange, qu'il vous soit favorable !"
                        elif ob1 == 16 and obj_param[ob1][0] < 255:
                            MSG = "Vous n'avez pas de lance."
                        elif ob1 == 16 and obj_param[ob1][0] == 256:
                            MSG = "Vous m'avez déjà échangé lla lance contre l'acide."
                        elif obj_param[ob1][0] != 255:
                            MSG = "Vous n'avez pas cet objet."
                        else:
                            MSG = "Il ne veut pas."
                    else:
                        MSG = "Vous ne pouvez pas faire cela."
                elif ob1 > 0 and ob2 == 0:
                    MSG = "Que voulez-vous donner et à qui ?"
                elif ob1 == 0 and ob2 == 0 and ob1s == "":
                    MSG = "Que voulez-vous donner et à qui ?"
                else:
                    MSG = "Je ne comprends pas."
            elif vb == 18: # Tailler
                if ob1 > 0 and ob2 >0 and cc == "AVEC":
                    if obj_param[ob1][2] == 0:
                        article = "la"
                    elif obj_param[ob1][2] == 1:
                        article = "le"
                    else:
                        article = "les"
                    if ob1 == 2 and ob2 == 15 and obj_param[ob1][0] == 255 and obj_param[ob2][0] == 255:
                        obj_param[ob1][0] = 256
                        obj_param[3][0] = 255
                        MSG = "Vous " + article + " sculptez jusqu'à obtenir un bâton de bonne facture."
                    elif ob1 == 2 and ob2 == 15 and (obj_param[ob1][0] != 255 or obj_param[ob2][0] != 255):
                        MSG = "Vous ne possédez pas ces deux objets."
                    else:
                        MSG = "Vous ne pouvez pas faire cela."
                elif ob1 > 0 and ob2 == 0 and cc == "":
                    MSG = "Avec quoi ?"
                elif ob1 > 0 and ob2 == 0 and cc == "AVEC":
                    MSG = "Vous ne pouvez pas faire cela."
                elif ob1 == 0 and ob2 == 0 and ob1s == "":
                    MSG = "Que voulez-vous sculpter, et avec quoi ?"
                elif ob1 == 0 and ob2 == 0 and ob1s != "":
                    MSG = "Vous ne pouvez pas sculpter cela."
                else:
                    MSG = "Je ne comprends pas."
            elif vb == 19: # Sonder
                if ob1 == 11 and ob2s == "":
                    if obj_param[11][0] == lieu:
                        if obj_param[17][0] == 0:
                            MSG = "En sondant le bord des eaux du lac, vous trouvez une clé en argent. Vous la mettez dans l'une de vos poches."
                            obj_param[17][0] = 255
                        else:
                            MSG = "Vous n'y trouvez plus rien."
                    else:
                        MSG = "Cet objet n'est pas ici."
                elif ob1 == 0 and ob2 == 0 and ob1s != "":
                    MSG = "Je ne vois pas de ça ici."
                elif ob1 == 0 and ob2 == 0 and ob1s == "":
                    MSG = "Que voulez-vous sonder ?"
                elif ob2 > 0:
                    MSG = "Je ne comprends pas."
                else:
                    MSG = "Vous ne pouvez pas."
            elif vb == 20: # Payer
                if ob1 == 10 and ob2s == "":
                    if obj_param[10][0] == lieu and obj_param[8][0] == 255:
                        obj_param[8][0] = 256
                        lieu_dir[lieu][2] = 10
                        MSG = "Merci d'avoir payé pour votre passage. Vous pouvez entrer au château de Gmell."
                    elif obj_param[10][0] == lieu and obj_param[8][0] < 255:
                        MSG = "Vous n'avez pas de pièce d'or."
                    elif obj_param[10][0] == lieu and obj_param[8][0] == 256:
                        MSG = "Vous avez déjà payé pour votre passage."
                    else:
                        MSG = "Il n'est pas ici."
                elif ob1 == 0 and ob2 == 0 and ob1s != "":
                    MSG = "Je ne vois pas de ça ici."
                elif ob1 == 0 and ob2 == 0 and ob1s == "":
                    MSG = "Qui voulez-vous payer ?"
                elif ob2 > 0:
                    MSG = "Je ne comprends pas."
                else:
                    MSG = "Vous ne pouvez pas."
            elif vb == 21: # Acheter
                if ob1 == 15 and ob2s == "":
                    if obj_param[22][0] == lieu and obj_param[13][0] == 255:
                        obj_param[13][0] = 256
                        obj_param[15][0] = 255
                        MSG = "Merci pour votre achat. Vous n'en serez pas déçu."
                    elif obj_param[22][0] == lieu and obj_param[13][0] < 255:
                        MSG = "Vous n'avez pas de rubis."
                    elif obj_param[22][0] == lieu and obj_param[13][0] == 256:
                        MSG = "Vous m'avez déjà acheté la dague."
                    else:
                        MSG = "Elle n'est pas ici."
                elif ob1 == 0 and ob2 == 0 and ob1s != "":
                    MSG = "Je ne vois pas de ça ici."
                elif ob1 == 0 and ob2 == 0 and ob1s == "":
                    MSG = "Que voulez-vous acheter ?"
                elif ob2 > 0:
                    MSG = "Je ne comprends pas."
                else:
                    MSG = "Vous ne pouvez pas."
            elif vb == 22: # Echanger
                if ob1 > 0 and ob2 >0 and (cc == "CONTRE" or cc == "AVEC"):
                    if obj_param[ob1][2] == 0:
                        article1 = "la"
                    elif obj_param[ob1][2] == 1:
                        article1 = "le"
                    else:
                        article1 = "les"
                    if obj_param[ob2][2] == 0:
                        article2 = "la"
                    elif obj_param[ob2][2] == 1:
                        article2 = "le"
                    else:
                        article2 = "les"
                    if lieu == 13 and ob1 == 13 and ob2 == 15 and obj_param[ob1][0] == 255:
                        obj_param[ob1][0] = 256
                        obj_param[ob2][0] = 255
                        MSG = "Vous faite l'échange : " + article1 + " " + obj[ob1][0].lower() + " contre " + article2 + " " + obj[ob2][0].lower()
                    elif lieu == 13 and ob1 == 13 and ob2 == 15 and obj_param[ob1][0] < 255:
                        MSG = "Vous ne possédez pas de rubis."
                    elif lieu == 13 and ob1 == 13 and ob2 == 15 and obj_param[ob1][0] == 256:
                        MSG = "L'échange a déjà été fait."
                    elif lieu == 13 and ob1 == 15 and ob2 == 13 and obj_param[ob2][0] == 255:
                        obj_param[ob1][0] = 255
                        obj_param[ob2][0] = 256
                        MSG = "Vous faite l'échange : " + article1 + " " +  obj[ob1][0].lower() + " contre " + article2 + " " + obj[ob2][0].lower()
                    elif lieu == 13 and ob1 == 15 and ob2 == 13 and obj_param[ob2][0] < 255:
                        MSG = "Vous ne possédez pas de rubis."
                    elif lieu == 13 and ob1 == 15 and ob2 == 13 and obj_param[ob2][0] == 256:
                        MSG = "L'échange a déjà été fait."
                    elif lieu == 18 and ob1 == 16 and ob2 == 26 and obj_param[ob1][0] == 255:
                        obj_param[ob1][0] = 256
                        obj_param[ob2][0] = 255
                        MSG = "Vous faite l'échange : " + article1 + " " + obj[ob1][0].lower() + " contre " + "l'" + obj[ob2][0].lower()
                    elif lieu == 18 and ob1 == 16 and ob2 == 26 and obj_param[ob1][0] < 255:
                        MSG = "Vous ne possédez pas de lance."
                    elif lieu == 18 and ob1 == 16 and ob2 == 26 and obj_param[ob1][0] == 256:
                        MSG = "L'échange a déjà été fait."
                    elif lieu == 18 and ob1 == 26 and ob2 == 16 and obj_param[ob2][0] == 255:
                        obj_param[ob1][0] = 255
                        obj_param[ob2][0] = 256
                        MSG = "Vous faite l'échange : " + "l'" +  obj[ob1][0].lower() + " contre " + article2 + " " + obj[ob2][0].lower()
                    elif lieu == 18 and ob1 == 26 and ob2 == 16 and obj_param[ob2][0] < 255:
                        MSG = "Vous ne possédez pas de lance."
                    elif lieu == 18 and ob1 == 26 and ob2 == 16 and obj_param[ob2][0] == 256:
                        MSG = "L'échange a déjà été fait."
                    else:
                        MSG = "Vous ne pouvez pas faire cela."
                elif ob1 > 0 and ob2 == 0 and cc == "":
                    MSG = "Contre quoi ?"
                elif ob1 > 0 and ob2 == 0 and (cc == "CONTRE" or cc == "AVEC"):
                    MSG = "Vous ne pouvez pas faire cela."
                elif ob1 == 0 and ob2 == 0 and ob1s == "":
                    MSG = "Que voulez-vous échanger, et contre quoi ?"
                elif ob1 == 0 and ob2 == 0 and ob1s != "":
                    MSG = "Vous ne pouvez pas échanger cela."
                else:
                    MSG = "Je ne comprends pas."
            elif vb == 23: # Tirer
                if ob1 == 4 and ob2s == "":
                    if obj_param[4][0] == lieu:
                        MSG = "En tirant sur la cordelette, un coffret lui étant lié s'arrache assez facilement de la terre."
                        obj_param[4][0] = 256
                        obj_param[5][0] = lieu
                    else:
                        MSG = "Cet objet n'est pas ici."
                elif ob1 == 32 and ob2s == "":
                    if obj_param[32][0] == lieu:
                        MSG = "Vous tirez sur la barre de fer, et vous entendez tout un mécanisme s'activer. Le levier se met \
à tourner seul jusqu'à ce qu'il arrive en butée et se plie, le rendant inutilisable."
                        obj_param[32][0] = 256
                        sound_1.play()
                    else:
                        MSG = "Cet objet n'est pas ici."
                elif ob1 == 0 and ob2 == 0 and ob1s != "":
                    MSG = "Je ne vois pas de ça ici."
                elif ob1 == 0 and ob2 == 0 and ob1s == "":
                    MSG = "Que voulez-vous tirer ?"
                elif ob2 > 0:
                    MSG = "Je ne comprends pas."
                else:
                    MSG = "Vous ne pouvez pas."
            elif vb == 24: # Ouvrir
                if ob1 == 29 and ob2 == 24 and cc == "AVEC":
                    if obj_param[29][0] == lieu:
                        if obj_param[24][0] == 255:
                            lieu_dir[20][5] = 21
                            obj_param[24][0] = 256
                            MSG = "Vous ouvrez la porte de la crypte, et à l'intérieur, vous y voyez un escalier qui s'enfonce dans les ténêbres."
                        elif obj_param[24][0] == 256:
                            MSG = "La porte est déjà ouverte."
                        else:
                            MSG = "Vous n'avez pas de clé d'or."
                    else:
                        MSG = "La porte n'est pas ici."
                elif ob1 == 29 and ob2 == 0:
                    if obj_param[29][0] == lieu:
                        MSG = "L'ouvrir avec quoi ?"
                    else:
                        MSG = "Cet objet n'est pas ici."
                elif ob1 == 29 and ob2 != 24 and cc == "AVEC":
                    MSG = "Vous ne pouvez pas."
                elif ob1 == 5 and ob2s == "":
                    if obj_param[5][0] == lieu:
                        if coffret_ouvert == False:
                                coffret_ouvert = True
                                if obj_param[6][0] == 0:
                                    obj_param[6][0] = 255
                                    MSG = "En l'ouvrant, vous y trouvez une clé de bronze que vous placez dans votre sac à dos."
                                else:
                                    MSG = "Vous ouvrez le coffret."
                        else:
                            MSG = "Il est déjà ouvert."
                    else:
                        MSG = "Cet objet n'est pas ici."
                elif ob1 == 36 and ob2 == 17 and cc == "AVEC":
                    if obj_param[36][0] == lieu:
                        if obj_param[17][0] >= 255:
                            if coffre_ouvert == False:
                                coffre_ouvert = True
                                if obj_param[37][0] == 0:
                                    obj_param[37][0] = 255
                                    obj_param[17][0] = 256
                                    MSG = "En l'ouvrant, vous y trouvez une bourse remplie de pièces d'or que vous placez dans votre sac à dos."
                                else:
                                    MSG = "Vous ouvrez le coffre."
                            else:
                                MSG = "Il est déjà ouvert."
                        else:
                            MSG = "Vous n'avez pas cette clé."
                    else:
                        MSG = "Cet objet n'est pas ici."
                elif ob1 == 36 and ob2 == 0:
                    if obj_param[36][0] == lieu and obj_param[17][0] == 256:
                        if coffre_ouvert == False:
                            coffre_ouvert = True
                            MSG = "Vous ouvez le coffre."
                        else:
                            MSG = "Il est déjà ouvert."
                    elif obj_param[36][0] == lieu and obj_param[17][0] < 256:
                        MSG = "L'ouvrir avec quoi ?"
                    else:
                        MSG = "Cet objet n'est pas ici."
                elif ob1 == 36 and ob2 != 17 and cc == "AVEC":
                    MSG = "Vous ne pouvez pas."
                elif ob1 == 33 and ob2 == 6 and cc == "AVEC":
                    if obj_param[33][0] == lieu:
                        if obj_param[6][0] == 255:
                                if obj_param[32][0] == 256 and obj_param[35][0] > 0 and epee_retiree == True:
                                    lieu_dir[22][4] = 26
                                    obj_param[6][0] = 256
                                    MSG = "Vous ouvrez la porte de bronze, et vous voyez soudainement une lumière intense et apaisante parvenir jusqu'à vos yeux."
                                else:
                                    MSG = "Vous tournez la clé partiellement mais un méchanisme secondaire semble bloquer la serrure."
                        elif obj_param[6][0] == 256:
                            MSG = "La porte est déjà ouverte."
                        else:
                            MSG = "Vous n'avez pas cette clé sur vous."
                    else:
                        MSG = "La porte n'est pas ici."
                elif ob1 == 33 and ob2 == 0:
                    if obj_param[33][0] == lieu:
                        MSG = "L'ouvrir avec quoi ?"
                    else:
                        MSG = "Cet objet n'est pas ici."
                elif ob1 == 33 and ob2 != 6 and cc == "AVEC":
                    MSG = "Vous ne pouvez pas."
                elif ob1 > 0 and ob2 > 0 and cc == "AVEC":
                    MSG = "Je ne peux pas."
                elif ob1 > 0 and ob2 == 0 and cc == "AVEC":
                    MSG = "Je ne comprends pas."
                elif ob1 == 0 and ob2 == 0 and ob1s != "":
                    MSG = "Je ne vois pas de ça ici."
                elif ob1 == 0 and ob2 == 0 and ob1s == "":
                    MSG = "Que voulez-vous ouvrir ?"
                elif ob2 > 0:
                    MSG = "Je ne comprends pas."
                else:
                    MSG = "Vous ne pouvez pas."
            elif vb == 25: # Fermer
                if ob1 == 5 and ob2s == "":
                    if obj_param[5][0] == lieu:
                        if coffret_ouvert == True:
                            coffret_ouvert = False
                            MSG = "Vous fermez le coffret."
                        else:
                            MSG = "Il est déjà fermé."
                    else:
                        MSG = "Cet objet n'est pas ici."
                elif ob1 == 36 and ob2s == "":
                    if obj_param[36][0] == lieu:
                        if coffre_ouvert == True:
                            coffre_ouvert = False
                            MSG = "Vous fermez le coffre."
                        else:
                            MSG = "Il est déjà fermé."
                    else:
                        MSG = "Cet objet n'est pas ici."
                elif ob1 == 0 and ob2 == 0 and ob1s != "":
                    MSG = "Je ne vois pas de ça ici."
                elif ob1 == 0 and ob2 == 0 and ob1s == "":
                    MSG = "Que voulez-vous fermer ?"
                elif ob2 > 0:
                    MSG = "Je ne comprends pas."
                else:
                    MSG = "Vous ne pouvez pas."
            elif vb == 26: # Boire
                if (ob1 == 11 or ob1 == 18) and ob2s == "":
                    if obj_param[11][0] == lieu:
                        MSG = "L'eau du lac n'a pas un goût terriblement appréciable, mais elle vous rafraîchit un peu."
                    else:
                        MSG = "Cet objet n'est pas ici."
                elif ob1 == 0 and ob2 == 0 and ob1s != "":
                        MSG = "Je ne vois pas de ça ici."
                elif ob1 == 0 and ob2 == 0 and ob1s == "":
                    MSG = "Que voulez-vous boire ?"
                elif ob2 > 0:
                    MSG = "Je ne comprends pas."
                else:
                    MSG = "Vous ne pouvez pas."
            elif vb == 27: # Manger
                if (ob1 == 11 or ob1 == 18) and ob2s == "":
                    if obj_param[11][0] == lieu:
                        MSG = "L'eau ne se mange pas, elle se boit."
                    else:
                        MSG = "Cet objet n'est pas ici."
                elif ob1 == 0 and ob2 == 0 and ob1s != "":
                        MSG = "Je ne vois pas de ça ici."
                elif ob1 == 0 and ob2 == 0 and ob1s == "":
                    MSG = "Que voulez-vous manger ?"
                elif ob2 > 0:
                    MSG = "Je ne comprends pas."
                else:
                    MSG = "Vous ne pouvez pas."
            elif vb == 28: # Creuser
                if ob1 == 7 and ob2s == "":
                    if obj_param[7][0] == lieu:
                        MSG = "Vous creusez au centre du puits dans le sable qui le bouche, mais vous ne trouvez rien."
                    else:
                        MSG = "Cet objet n'est pas ici."
                elif ob1 > 0 and ob2 > 0 and cc == "AVEC":
                    MSG = "Je ne peux pas."
                elif ob1 > 0 and ob2 == 0 and cc == "AVEC":
                    MSG = "Je ne comprends pas."
                elif ob1 == 0 and ob2 == 0 and ob1s != "":
                    MSG = "Je ne vois pas de ça ici."
                elif ob1 == 0 and ob2 == 0 and ob1s == "":
                    MSG = "Que voulez-vous creuser ?"
                elif ob2 > 0:
                    MSG = "Je ne comprends pas."
                else:
                    MSG = "Vous ne pouvez pas."
            elif vb == 29: # Pousser
                if ob1 == 1 and ob2s == "":
                    if obj_param[1][0] == lieu:
                        MSG = "Il est trop lourd pour vous."
                    else:
                        MSG = "Cet objet n'est pas ici."
                elif ob1 == 30 and ob2s == "":
                    if obj_param[30][0] == lieu:
                        if obj_param[28][0] == 0:
                            obj_param[28][0] = 255
                            MSG = "Une petite partie du muret s'effondre, et vous découvrez dedans un petit barreau de fer qui peut vous servir de levier. Vous le prenez."
                        else:
                            MSG = "Vous avez beau pousser le muret, plus rien ne bouge."
                    else:
                        MSG = "Cet objet n'est pas ici."
                elif ob1 == 0 and ob2 == 0 and ob1s != "":
                        MSG = "Je ne vois pas de ça ici."
                elif ob1 == 0 and ob2 == 0 and ob1s == "":
                    MSG = "Que voulez-vous pousser ?"
                elif ob2 > 0:
                    MSG = "Je ne comprends pas."
                else:
                    MSG = "Vous ne pouvez pas."
            elif vb == 30: # Frapper
                if ob1 == 9 and (ob2s == "" or ((ob2 == 3 or ob2 == 15 or ob2 == 16) and cc == "AVEC")):
                    if obj_param[9][0] == lieu:
                        if (ob2 > 0 and obj_param[ob2][0] == 255) or ob2s == "":
                            MSG = "Ha ha ha... Avec ta faible musculature, tu n'as aucune chance de me vaincre !"
                        elif ob2 > 0 and obj_param[ob2][0] != 255:
                            MSG = "Vous n'avez pas cet objet."
                    else:
                        MSG = "Il n'est pas ici."
                elif ob1 == 10 and (ob2s == "" or ((ob2 == 3 or ob2 == 15 or ob2 == 16) and cc == "AVEC")):
                    if obj_param[10][0] == lieu:
                        if (ob2 > 0 and obj_param[ob2][0] == 255) or ob2s == "":
                            MSG = "Le soldat pare votre coup avec facilité."
                        elif ob2 > 0 and obj_param[ob2][0] != 255:
                            MSG = "Vous n'avez pas cet objet."
                    else:
                        MSG = "Il n'est pas ici."
                elif ob1 == 23 and (ob2s == "" or ((ob2 == 3 or ob2 == 15 or ob2 == 16) and cc == "AVEC")):
                    if obj_param[23][0] == lieu:
                        if ((ob2s == "" or ob2 == 16) and obj_param[16][0] == 255):
                            if lieu_bis[16] == "":
                                MSG = "Vous tuez l'insecte géant à coups de lance, tout en restant à une certaine distance de lui."
                                lieu_bis[16] = "bis"
                                lieu_dir[16][1] = 17
                                load_scn = True
                            else:
                                MSG = "L'insecte géant est déjà mort."
                        elif ob2 > 0 and obj_param[ob2][0] != 255:
                            MSG = "Vous n'avez pas cet objet."
                        else:
                            MSG = "Vous ne pouvez pas vous approcher de cet insecte sans une arme à longue portée."
                    else:
                        MSG = "Il n'est pas ici."
                elif ob1 == 27 and (ob2s == "" or ((ob2 == 3 or ob2 == 15 or ob2 == 16 or ob2 == 26) and cc == "AVEC")):
                    if obj_param[27][0] == lieu:
                        if ((ob2s == "" or ob2 == 26) and obj_param[26][0] == 255):
                            if lieu_bis[19] == "":
                                MSG = "Vous tuez le dragon en lui envoyant l'acide au visage."
                                lieu_bis[19] = "bis"
                                obj_param[26][0] = 256
                                load_scn = True
                            else:
                                MSG = "Le dragon est déjà mort."
                        elif ob2 > 0 and obj_param[ob2][0] != 255:
                            MSG = "Vous n'avez pas cet objet."
                        else:
                            MSG = "Vous ne pouvez pas vous approcher du dragon, il vous faut une arme spéciale."
                    else:
                        MSG = "Il n'est pas ici."
                elif ob1 == 34 and (ob2s == "" or (ob2 == 35 and cc == "AVEC")):
                    if obj_param[34][0] == lieu:
                        if ((ob2s == "" or ob2 == 35) and obj_param[35][0] == 255):
                            if lieu_bis[23] == "":
                                MSG = "Vous tuez l'araignée à coups d'épée."
                                lieu_bis[23] = "bis"
                                load_scn = True
                            else:
                                MSG = "L'araignée est déjà morte."
                        elif ob2 > 0 and obj_param[ob2][0] != 255:
                            MSG = "Vous n'avez pas cet objet."
                        else:
                            MSG = "Vous ne pouvez pas tuer l'araignée sans une arme tranchante."
                    else:
                        MSG = "Elle n'est pas ici."
                elif ob1 > 0 and ob2 > 0 and cc == "AVEC":
                    MSG = "Je ne peux pas."
                elif ob1 > 0 and ob2 == 0 and cc == "AVEC":
                    MSG = "Je ne comprends pas."
                elif ob1 == 0 and ob2 == 0 and ob1s != "":
                    MSG = "Je ne le/la vois pas ici."
                elif ob1 == 0 and ob2 == 0 and ob1s == "":
                    MSG = "Qui voulez-vous frapper ?"
                elif ob2 > 0:
                    MSG = "Je ne comprends pas."
                else:
                    MSG = "Vous ne pouvez pas."
            elif vb == 31: # Tuer
                if ob1 == 9 and (ob2s == "" or ((ob2 == 3 or ob2 == 15 or ob2 == 16) and cc == "AVEC")):
                    if obj_param[9][0] == lieu:
                        if (ob2 > 0 and obj_param[ob2][0] == 255) or ob2s == "":
                            MSG = "N'essaye même pas !"
                        elif ob2 > 0 and obj_param[ob2][0] != 255:
                            MSG = "Vous n'avez pas cet objet."
                    else:
                        MSG = "Il n'est pas ici."
                elif ob1 == 10 and (ob2s == "" or ((ob2 == 3 or ob2 == 15 or ob2 == 16) and cc == "AVEC")):
                    if obj_param[10][0] == lieu:
                        if (ob2 > 0 and obj_param[ob2][0] == 255) or ob2s == "":
                            MSG = "Il faut se faire à l'évidence, vous n'avez aucune chance de le vaincre."
                        elif ob2 > 0 and obj_param[ob2][0] != 255:
                            MSG = "Vous n'avez pas cet objet."
                    else:
                        MSG = "Il n'est pas ici."
                elif ob1 == 23 and (ob2s == "" or ((ob2 == 3 or ob2 == 15 or ob2 == 16) and cc == "AVEC")):
                    if obj_param[23][0] == lieu:
                        if ((ob2s == "" or ob2 == 16) and obj_param[16][0] == 255):
                            if lieu_bis[16] == "":
                                MSG = "Vous tuez l'insecte géant à coups de lance, tout en restant à une certaine distance de lui."
                                lieu_bis[16] = "bis"
                                lieu_dir[16][1] = 17
                                load_scn = True
                            else:
                                MSG = "L'insecte géant est déjà mort."
                        elif ob2 > 0 and obj_param[ob2][0] != 255:
                            MSG = "Vous n'avez pas cet objet."
                        else:
                            MSG = "Vous ne pouvez pas vous approcher de cet insecte sans une arme à longue portée."
                    else:
                        MSG = "Il n'est pas ici."
                elif ob1 == 27 and (ob2s == "" or ((ob2 == 3 or ob2 == 15 or ob2 == 16 or ob2 == 26) and cc == "AVEC")):
                    if obj_param[27][0] == lieu:
                        if ((ob2s == "" or ob2 == 26) and obj_param[26][0] == 255):
                            if lieu_bis[19] == "":
                                MSG = "Vous tuez le dragon en lui envoyant l'acide au visage."
                                lieu_bis[19] = "bis"
                                obj_param[26][0] = 256
                                load_scn = True
                            else:
                                MSG = "Le dragon est déjà mort."
                        elif ob2 > 0 and obj_param[ob2][0] != 255:
                            MSG = "Vous n'avez pas cet objet."
                        else:
                            MSG = "Vous ne pouvez pas vous approcher du dragon, il vous faut une arme spéciale."
                    else:
                        MSG = "Il n'est pas ici."
                elif ob1 == 34 and (ob2s == "" or (ob2 == 35 and cc == "AVEC")):
                    if obj_param[34][0] == lieu:
                        if ((ob2s == "" or ob2 == 35) and obj_param[35][0] == 255):
                            if lieu_bis[23] == "":
                                MSG = "Vous tuez l'araignée avec votre épée."
                                lieu_bis[23] = "bis"
                                load_scn = True
                            else:
                                MSG = "L'araignée est déjà morte."
                        elif ob2 > 0 and obj_param[ob2][0] != 255:
                            MSG = "Vous n'avez pas cet objet."
                        else:
                            MSG = "Vous ne pouvez pas vous approcher de cette araignée sans une arme tranchante."
                    else:
                        MSG = "Elle n'est pas ici."
                elif ob1 > 0 and ob2 > 0 and cc == "AVEC":
                    MSG = "Je ne peux pas."
                elif ob1 > 0 and ob2 == 0 and cc == "AVEC":
                    MSG = "Je ne comprends pas."
                elif ob1 == 0 and ob2 == 0 and ob1s != "":
                    MSG = "Je ne le/la vois pas ici."
                elif ob1 == 0 and ob2 == 0 and ob1s == "":
                    MSG = "Qui voulez-vous tuer ?"
                elif ob2 > 0:
                    MSG = "Je ne comprends pas."
                else:
                    MSG = "Vous ne pouvez pas."
            elif vb == 32: # Attacher
                if ob1 > 0 and ob2 >0 and (cc == "AVEC" or cc == "ET" or cc == "A" or cc == "AU" or cc == "SUR"):
                    if ob1 == 3 and ob2 == 15 and obj_param[ob1][0] == 255 and obj_param[ob2][0] == 255:
                        if obj_param[14][0] == 255:
                            obj_param[ob1][0] = 256
                            obj_param[ob2][0] = 256
                            obj_param[14][0] = 256
                            obj_param[16][0] = 255
                            MSG = "Vous les liez solidement avec le cordon et obtenez une magnifique lance pour frapper à distance."
                        else:
                            MSG = "Il vous manque quelque chose pour lier la dague et le bâton."
                    elif ob1 == 3 and ob2 == 15 and (obj_param[ob1][0] != 255 or obj_param[ob2][0] != 255):
                        MSG = "Vous ne possédez pas ces deux objets."
                    elif ob1 == 15 and ob2 == 3 and obj_param[ob1][0] == 255 and obj_param[ob2][0] == 255:
                        if obj_param[14][0] == 255:
                            obj_param[ob1][0] = 256
                            obj_param[ob2][0] = 256
                            obj_param[14][0] = 256
                            obj_param[16][0] = 255
                            MSG = "Vous les liez solidement avec le cordon et obtenez une magnifique lance pour frapper à distance."
                        else:
                            MSG = "Il vous manque quelque chose pour lier la dague et le bâton."
                    elif ob1 == 15 and ob2 == 3 and (obj_param[ob1][0] != 255 or obj_param[ob2][0] != 255):
                        MSG = "Vous ne possédez pas ces deux objets."
                    elif ob1 == 28 and ob2 == 31 and obj_param[ob1][0] == 255 and obj_param[ob2][0] == lieu:
                        obj_param[ob1][0] = 256
                        obj_param[ob2][0] = 256
                        obj_param[32][0] = lieu
                        MSG = "Vous placez le barreau de fer dans un trou prévu à cet effet. Il peut maintenant vous servir de levier."
                    elif ob1 == 28 and ob2 == 31 and obj_param[ob1][0] < 255 and obj_param[ob2][0] == lieu:
                        MSG = "Vous ne possedez pas de barreau de fer."
                    elif ob1 == 28 and ob2 == 31 and obj_param[ob1][0] == 256 and obj_param[ob2][0] == lieu:
                        MSG = "C'est déjà fait."
                    elif ob1 == 31 and ob2 == 28 and obj_param[ob1][0] == lieu and obj_param[ob2][0] == 255:
                        obj_param[ob1][0] = 256
                        obj_param[ob2][0] = 256
                        obj_param[32][0] = lieu
                        MSG = "Vous placez le barreau de fer dans un trou prévu à cet effet. Il peut maintenant vous servir de levier."
                    elif ob1 == 31 and ob2 == 28 and obj_param[ob1][0] == lieu and obj_param[ob2][0] < 255:
                        MSG = "Vous ne possedez pas de barreau de fer."
                    elif ob1 == 31 and ob2 == 28 and obj_param[ob1][0] == lieu and obj_param[ob2][0] == 256:
                        MSG = "C'est déjà fait."
                    else:
                        MSG = "Vous ne pouvez pas faire cela."
                elif ob1 > 0 and ob2 == 0 and cc == "":
                    MSG = "Avec quoi ?"
                elif ob1 > 0 and ob2 == 0 and (cc == "AVEC" or cc == "ET" or cc == "A" or cc == "AU" or cc == "SUR"):
                    MSG = "Vous ne pouvez pas faire cela."
                elif ob1 == 0 and ob2 == 0 and ob1s == "":
                    MSG = "Que voulez-vous attacher, et avec quoi ?"
                elif ob1 == 0 and ob2 == 0 and ob1s != "":
                    MSG = "Vous ne pouvez pas attacher cela."
                else:
                    MSG = "Je ne comprends pas."
            elif vb == 33: # Aide
                MSG = verb_list
            UpdateGraphics(screen_img , temp_scn)
            if ligne == lines_count:
                if MSG == "":
                    ScrollBuffer(1 , buffer , lines_count)
                    ligne -= 1
                else:
                    ScrollBuffer(2 , buffer , lines_count)
                    ligne -= 2
            elif ligne == lines_count - 1 and MSG != "":
                ScrollBuffer(1 , buffer , lines_count)
                ligne -= 1        
            if MSG != "":
                ligne = Ajouter_Texte(buffer , MSG , ligne , lines_count)
                if ligne == lines_count:
                    ScrollBuffer(1 , buffer , lines_count)
                    ligne -= 1
            Afficher_Buffer(buffer , police_height , lines_count , screen_txt_y)
            Affiche_Commande(CMD + "_" , YPos(ligne , police_height , screen_txt_y))
            Ready = True
    # *** Afficher ce qui a été fait
    pygame.display.flip()
    # Limiter à 20 FPS
    clock.tick(20)
    if sound_queue == 0:
        intro_sound.play()
        sound_queue = -1
# ferme la fenêtre et quitte
pygame.quit()

