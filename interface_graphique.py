################################### lancement de l'interface
#création module + fenetre
import tkinter
from tkinter import *
import time
from classe_Individu import *
from classe_Evolution import *
from classe_monde import *
root = tkinter.Tk()
root.geometry("1300x900") 
root.title("Simulation épidémie ")
root.configure(bg = '#836bf3')
root.resizable(width = False, height = False)
taille_grille = 0

###### Pour lancer la simulation de l'épidemie il suffit de lancer le programme et c'est parti !

################################# lancement de la grille

def dessiner(jour_confinement, confinement, canv, monde, compteur, fen):
    """
    fonction permettant d'affciher l'evolution de l'épidemie 
    """
    for i in range(1, taille_grille + 1):
        intervalle_verti = 1200 / taille_grille
        intervalle_hori = 800 / taille_grille
        canv.create_line((i - 1) * intervalle_verti , 0, (i -1)  * intervalle_verti, 800, width = 1, fill = "black")
        canv.create_line(0, (i-1) * intervalle_hori, 1200, (i-1) * intervalle_hori, width = 1, fill = "black")
    for y in range(taille_grille):
        for x in range(taille_grille):
            if monde.monde1.grille[y][x] != 0:
                for elem in monde.monde1.liste_personnages:
                    if elem.position == (y,x):
                        if elem.etat_contamination >0:
                            canv.create_rectangle(x * intervalle_verti,y * intervalle_hori,(x+1) * intervalle_verti,(y+1) * intervalle_hori, outline  = "black", fill = "#e32323")
                        elif elem.immunite == True:
                            canv.create_rectangle(x * intervalle_verti,y * intervalle_hori,(x+1) * intervalle_verti,(y+1) * intervalle_hori, outline  = "black", fill = "#18dc83")
                        else:                            canv.create_rectangle(x * intervalle_verti,y * intervalle_hori,(x+1) * intervalle_verti,(y+1) * intervalle_hori, outline  = "black", fill = "#836bf3")
            else:
                canv.create_rectangle(x * intervalle_verti,y * intervalle_hori,(x+1) * intervalle_verti,(y+1) * intervalle_hori, outline  = "black", fill = "white")
    if monde.cycle == jour_confinement:
        monde.changer_etat(confinement)
    monde.deplacement_individu()
    monde.evolution_phy()
    monde.evolution_conta()
    monde.contagiosite()
    monde.evolution_derogation()
    monde.personne_morte()
    monde.vaccination()
    monde.jour_suivant()
    if compteur <= 30:
        compteur += 1
        canv.after(500, dessiner, jour_confinement, confinement, canv, monde, compteur, fen)
    else:
        fen.destroy()


##########################################     création interface
######création bouton confinement
matieres = ["Liberté", "Confinement Léger", "Confinement Strict"]

boutons = {} 
v = tkinter.IntVar()
for i in range(len(matieres)):
    c = tkinter.Radiobutton(root, variable = v, value = i,  text = matieres[i], font = (10), bg = '#836bf3')
    c.place(x = 10, y = 10 + i * 30)
    c.configure(bg = 'white')
    c.place(x = 100,y =400 +  i*50)
    boutons[matieres[i]] = c

titre_confinement = Label(root, text = 'Type de confinement', font=('Bold', '25'))
titre_confinement.place(x = 50, y = 300)
########création bande de jour auquel instauration confinement
def presser():
    global taille_grille
    global compteur
    global fen
    sel = echelle1.get()
    I.configure(text = sel)
    confinement = v.get()
    jour_confinement = sel
    taille_grille = int(Lb.selection_get())
    compteur = 0
    monde = Evolution(0, 0, taille_grille, taille_grille, 0.20)
    root.destroy()
    fen = Tk()
    fen.geometry('1300x900')
    fen.title('Projet_pandemie')
    fen.resizable(width = False, height = False)
    canv = Canvas(fen, width = 1200, height = 800, bg = "white")
    canv.place(x=30, y=30)
    dessiner(jour_confinement, confinement , canv, monde, compteur, fen)


####### création d'une échelle verticale (par défaut), graduée de 20 en 20
echelle1 = tkinter.Scale(root, from_ = 0, to = 300,resolution = 25, tickinterval = 100, orient='horizontal')
echelle1.place(x = 1100, y = 400)

# mis een place d'un bouton qui déclenche l'affichage de la valeur choisie sur echelle1
b = tkinter.Button(root, text = "Lancer la simulation", command = presser, height  = 5, width = 20,font = ('Arial', 20), bg  = 'red') 
b.place(x = 500, rely = 0.75)

I = tkinter.Label(root, text = "Jour De début du Confinement", font = ('Bold', 15))
I.place(x = 1000, y  = 350)

######## Création du titre en haut de la fenêtre
titre = Label(root, text = 'Simulation d\'une épidémie', font  = ('Arial Black', 20), bg = '#836bf3')
titre.place(x = 500, rely = 0)
######## insertion photo
photo = PhotoImage(file="coronax.png")
canvas = Canvas(root, width=500, height=550)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.place(x = 400, y = 100)

####### taille de la grille
A = []
def selection(evt):
    selec = Lb.selection_get()
    liste = [Lb.get(i) for i in Lb.curselection()]

Lb = tkinter.Listbox(root, width = 15, height = 7, selectmode = 'unique')
nb_grille = [5, 15, 20, 30, 50, 75, 100]
for i in range(len(nb_grille)):
    Lb.insert(i, nb_grille[i])

Lb.bind('<<ListboxSelect>>', selection)
Lb.place(x = 1100, y = 190)

L = tkinter.Label(root, text = "Taille de la grille", font  = ('Bold', 20))
L.place(x = 1050, y = 150)

#lancement de l'interface
root.mainloop()








