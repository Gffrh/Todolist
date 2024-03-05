import pymongo

myclient = pymongo.MongoClient("mongodb+srv://Root:GTygbCFQMkDZXHSU@todolist.dlhlsgi.mongodb.net/")
TodolistDB = myclient["Todolist_DB"]
TodolistCollection = TodolistDB["Todolist_collection"]

tableau_des_taches=[]

def ajout_elem(tab,x):
    tab.append(x)

def suppr_elem(tab,x):
    tab.remove(x)

def update_elem(x,y):
    tableau_des_taches[x]=y

while True:

    print("1. Afficher les taches à faire")
    print("2. Ajouter une nouvelle tache")
    print("3. Supprimer une tache")
    print("4, Modifier une tache")

    test_choix = input("Que voulez-vous faire ? : ")
    

    if test_choix=="1":
        print(tableau_des_taches)

    if test_choix=="2": 
        ajout_input = input("Nom de la tache : ")
        ajout_elem(tableau_des_taches,ajout_input)
        TodolistCollection.insert_one({"Nom de la tache ": ajout_input})


    if test_choix=="3":
        supp_input = input("Choissisez quelle tache à supprimer : ")
        suppr_elem(tableau_des_taches,supp_input)
        TodolistCollection.delete_one({"Nom de la tache à supprimer " : supp_input})

        """
        if input != input:
            print("Cette tache n'existe pas.")
        else:
            suppr_elem(tableau_des_taches,input("Choissisez quelle tache à supprimer : "))
        """

    if test_choix=="4": 
        update_input = input("Quelle est la nouvelle tache : ")
        update_elem(0,update_input)