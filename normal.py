# coding: utf-8
from tkinter import *  #pour importer l'ensemble du tkinter
import requests
import mysql.connector   #pour importer la base de données
import tkinter.ttk
from tkinter.messagebox import *
from PIL import ImageTk, Image
#from client1 import * : On importe un fichier lorsqu'il est créé
from tkcalendar import *  # pour importer la calendrier

fenetre = Tk()
fenetre.geometry("1200x500")
fenetre.title("Interface de communication unifiée")

#label = Label(fenetre, text= "Bienvenue dans l'interface de communication", bg="green")
#label.pack()


##fonction appel simple
def call():
    appelle=appelle1.get()
    appelant=appelant1.get()
    para="PJSIP/"+appelant
    params=(('endpoint', para),('extension', appelle),('context','Telecom'),('priority', '1'), ('callerId',appelant),)
    response = requests.post('http://192.168.1.2:8088/ari/channels', params=params,auth=('asterisk','passer'))
    showinfo("Information de l'appel", "Appel en cours de "+appelle+"...")




bouton=Button(fenetre, text="Appel Simple", bg="#00FFFF", fg="black")
bouton.place(x=0,y=6, width="200", height="40")

bouton1=Button(fenetre, text="Appel Vidéo", bg="#00FFFF", fg="black")
bouton1.place(x=0,y=50, width="200", height="40")

bouton2=Button(fenetre, text="Conférence", bg="#00FFFF", fg="black")
bouton2.place(x=0,y=100, width="200", height="40")

bouton3=Button(fenetre, text="Messagerie vocale", bg="#00FFFF", fg="black")
bouton3.place(x=0,y=150, width="200", height="40")

bouton4=Button(fenetre, text="Transfert d'appel", bg="#00FFFF", fg="black")
bouton4.place(x=0,y=200, width="200", height="40")

bouton5=Button(fenetre, text="Parking", bg="#00FFFF", fg="black")
bouton5.place(x=0,y=250, width="200", height="40")

bouton6=Button(fenetre, text="SMS ou Chat", bg="#00FFFF", fg="black")
bouton6.place(x=0,y=300, width="200", height="40" )

bouton7=Button(fenetre, text="Mise en écoute", bg="#00FFFF", fg="black")
bouton7.place(x=0,y=350, width="200", height="40")

bouton8=Button(fenetre, text="Partage de fichiers", bg="#00FFFF", fg="black")
bouton8.place(x=0,y=400, width="200", height="40")

bouton9=Button(fenetre, text="Centre d'appel", bg="#00FFFF", fg="black")
bouton9.place(x=0,y=450, width="200", height="40")

bouton10=Button(fenetre, text="Appel asterisk google", bg="#00FFFF", fg="black")
bouton10.place(x=0,y=500, width="200", height="40")

#appel simple
labelappelant=Label(fenetre,text="Appelant",bg="black",fg="white")
labelappelle=Label(fenetre,text="Appelé",bg="black",fg="white")
appelant1=StringVar()
appelle1=StringVar()
entreeappelant=Entry(fenetre,textvariable=appelant1)
entreeappelle=Entry(fenetre, textvariable=appelle1)
labelappelant.place(x=810,y=6,width="80",height=40)
entreeappelant.place(x=900,y=6, width="115", height=40)
labelappelle.place(x=810,y=56,width="80",height=40)
entreeappelle.place(x=900,y=56, width="115", height="40")


##Le bouton permettant d'appeler
appel=Button(fenetre, text="Appeler",width="10",height=0,bd=0,bg="#0080ff",activebackground="#00bfff",foreground='#ffffff',font=("Arial", 12), command=call)
appel.place(x=1020,y=56, height="40")



fenetre.mainloop()

