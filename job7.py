import mysql.connector

class EmployeManager:
    def __init__(self, host='localhost', user='root', password='root', database='job7'):
        self.conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.conn.cursor()
    
    def ajouter_employe(self, nom, prenom, salaire, id_service):
        sql = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (nom, prenom, salaire, id_service))
        self.conn.commit()
    
    def supprimer_employe(self, employe_id):
        sql = "DELETE FROM employe WHERE id = %s"
        self.cursor.execute(sql, (employe_id,))
        self.conn.commit()
    
    def modifier_employe(self, employe_id, nom=None, prenom=None, salaire=None, id_service=None):
        updates = []
        params = []
        if nom:
            updates.append("nom = %s")
            params.append(nom)
        if prenom:
            updates.append("prenom = %s")
            params.append(prenom)
        if salaire:
            updates.append("salaire = %s")
            params.append(salaire)
        if id_service:
            updates.append("id_service = %s")
            params.append(id_service)
        params.append(employe_id)
        sql = f"UPDATE employe SET {', '.join(updates)} WHERE id = %s"
        self.cursor.execute(sql, params)
        self.conn.commit()
    
    def afficher_employes(self):
        self.cursor.execute("SELECT employe.id, employe.nom, employe.prenom, employe.salaire, service.nom FROM employe JOIN service ON employe.id_service = service.id")
        for row in self.cursor.fetchall():
            print(row)
    
    def fermer_connexion(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    manager = EmployeManager()
    manager.afficher_employes()
    manager.fermer_connexion()
