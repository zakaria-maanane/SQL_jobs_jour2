''' TOUT LES JOBS 1-6 SONT COMPRIS DANS CE FICHIER et LAPLATEFORME_JOUR2.SQL'''

import mysql.connector

try:
    # Connexion à la base de données
    conn = mysql.connector.connect(
        host="localhost",      
        user="root",           
        password="root",       
        database="laplateforme_jour2"  #Nom de la base de données
    )

    cursor = conn.cursor()


#===== JOB 2 et 3 => SQL =====

#=========== JOB 4 Fonction pour afficher le contenu d'une table ========
    def afficher_table(nom_table):
        print(f"\n🔹 Contenu de la table `{nom_table}` :")
        query = f"SELECT * FROM {nom_table};"
        cursor.execute(query)
        resultats = cursor.fetchall()

        if resultats:
            for row in resultats:
                print(row)
        else:
            print("⚠️ Aucun résultat trouvé.")

    # Afficher les trois tables
    afficher_table("etudiant")
    afficher_table("etage")
    afficher_table("salle")
#==================================================================

# ===========--- JOB 5 requête pour calculer la superficie totale ---==========
    query = "SELECT SUM(superficie) AS superficie_totale FROM etage;"
    cursor.execute(query)
    resultats = cursor.fetchone()  # Récupère le résultat sous forme de tuple

    if resultats and resultats[0] is not None:
        superficie_totale = resultats[0]
        print(f"La superficie de La Plateforme est de {superficie_totale} m².")
    else:
        print("⚠️ Aucune superficie disponible dans la base de données.")
#=====================================================================================

# ========--- JOB 6 Ajoute ici la requête pour calculer la capacité totale des salles ---======
    query = "SELECT SUM(capacite) AS capacite_totale FROM salle;"
    cursor.execute(query)
    resultats = cursor.fetchone()  # Récupère le résultat sous forme de tuple

    if resultats and resultats[0] is not None:
        capacite_totale = resultats[0]
        print(f"La capacité totale des salles est de {capacite_totale} personnes.")
    else:
        print("⚠️ Aucune capacité disponible dans la base de données.")
#========================================================================================



    # Fermer la connexion
    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(f"❌ Erreur : {err}")
