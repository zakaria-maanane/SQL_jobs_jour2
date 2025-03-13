import mysql.connector

def connecter_bd():
    return mysql.connector.connect(
        host="localhost",  
        user="root",  
        password="root",  
        database="zoo"
    )

def ajouter_cage(superficie, capacite_max):
    conn = connecter_bd()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)", (superficie, capacite_max))
    conn.commit()
    conn.close()

def ajouter_animal(nom, race, cage_id, date_naissance, pays_origine):
    conn = connecter_bd()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO animal (nom, race, cage_id, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)",
                   (nom, race, cage_id, date_naissance, pays_origine))
    conn.commit()
    conn.close()

def supprimer_animal(animal_id):
    conn = connecter_bd()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM animal WHERE id = %s", (animal_id,))
    conn.commit()
    conn.close()

def supprimer_cage(cage_id):
    conn = connecter_bd()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cage WHERE id = %s", (cage_id,))
    conn.commit()
    conn.close()

def afficher_animaux():
    conn = connecter_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animal")
    for animal in cursor.fetchall():
        print(animal)
    conn.close()

def afficher_cages():
    conn = connecter_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cage")
    for cage in cursor.fetchall():
        print(cage)
    conn.close()

def superficie_totale():
    conn = connecter_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(superficie) FROM cage")
    total = cursor.fetchone()[0]
    conn.close()
    return total if total else 0

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Ajouter une cage")
        print("2. Ajouter un animal")
        print("3. Supprimer un animal")
        print("4. Supprimer une cage")
        print("5. Afficher les animaux")
        print("6. Afficher les cages")
        print("7. Superficie totale des cages")
        print("8. Quitter")
        
        choix = input("Choisissez une option : ")
        if choix == "1":
            superficie = float(input("Superficie de la cage : "))
            capacite = int(input("Capacité max de la cage : "))
            ajouter_cage(superficie, capacite)
        elif choix == "2":
            nom = input("Nom de l'animal : ")
            race = input("Race de l'animal : ")
            cage_id = int(input("ID de la cage : "))
            date_naissance = input("Date de naissance (YYYY-MM-DD) : ")
            pays_origine = input("Pays d'origine : ")
            ajouter_animal(nom, race, cage_id, date_naissance, pays_origine)
        elif choix == "3":
            animal_id = int(input("ID de l'animal à supprimer : "))
            supprimer_animal(animal_id)
        elif choix == "4":
            cage_id = int(input("ID de la cage à supprimer : "))
            supprimer_cage(cage_id)
        elif choix == "5":
            afficher_animaux()
        elif choix == "6":
            afficher_cages()
        elif choix == "7":
            print("Superficie totale des cages :", superficie_totale())
        elif choix == "8":
            break
        else:
            print("Option invalide.")
