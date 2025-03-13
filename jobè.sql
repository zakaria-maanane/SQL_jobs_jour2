-- Création de la base de données
CREATE DATABASE entreprise;
USE entreprise;

-- Création de la table employe
CREATE TABLE employe (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    salaire DECIMAL(10,2) NOT NULL,
    id_service INT NOT NULL
);
-- Insertion des employés
INSERT INTO employe (nom, prenom, salaire, id_service) VALUES
('Dupont', 'Jean', 3500.00, 1),
('Martin', 'Sophie', 2800.00, 2),
('Durand', 'Luc', 4000.00, 1),
('Bernard', 'Claire', 3200.00, 3);

-- Requête pour récupérer les employés dont le salaire est supérieur à 3000€
SELECT * FROM employe WHERE salaire > 3000;

-- Création de la table service
CREATE TABLE service (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(50) NOT NULL
);

-- Insertion des services
INSERT INTO service (nom) VALUES
('Informatique'),
('Ressources Humaines'),
('Marketing');

-- Requête pour récupérer tous les employés avec leur service
SELECT employe.nom, employe.prenom, employe.salaire, service.nom AS service 
FROM employe
JOIN service ON employe.id_service = service.id;
