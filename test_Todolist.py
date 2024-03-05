todo_list = {
    "Titre" : [],
    "Contenu" : [],
    "Status" : []
}

def add_Task(dict,insert_titre,insert_contenu,insert_status):
        dict["Titre"] = insert_titre
        dict["Contenu"] = insert_contenu
        dict["Status"] = insert_status
add_Task(todo_list,"Permis Moto", "Faut passer le code d'abord","Pas finie")

if todo_list["Status"] != "Pas finie":
    def delete_Task(dict,delete_titre,delete_contenu,delete_status):
        dict["Titre"] = delete_titre
        dict["Contenu"] = delete_contenu
        dict["Status"] = delete_status
    delete_Task(todo_list," "," "," ")
    print("Vous n'avez pas de tâche à faire! Super! ")
else :
    print(todo_list)

"""
todo_list["Titre"].append("1. Permis Moto")
todo_list["Titre"].append("2. TEST")

todo_list["Contenu"].append("1. Passer le code d'abord")
todo_list["Contenu"].append("2. TEST_description")

todo_list["Status"].append("1. Pas finie")
todo_list["Status"].append("2. Pas finie")

print(todo_list)
"""