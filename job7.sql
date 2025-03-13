

CREATE DATABASE IF NOT EXISTS entreprise;

USE entreprise;

-- Création de la table service
CREATE TABLE service (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL
);

-- Création de la table employe
CREATE TABLE employe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    salaire DECIMAL(10, 2) NOT NULL,
    id_service INT,
    FOREIGN KEY (id_service) REFERENCES service(id)
);

-- Insertion de données dans la table service
INSERT INTO service (nom) VALUES
('Informatique'),
('Ressources Humaines'),
('Comptabilité'),
('Marketing'),
('Direction');

-- Insertion de données dans la table employe
INSERT INTO employe (nom, prenom, salaire, id_service) VALUES
('Dubois', 'Jean', 2800.00, 1),
('Martin', 'Sophie', 3200.00, 2),
('Lefevre', 'Marc', 4500.00, 3),
('Dupont', 'Marie', 3800.00, 4),
('Petit', 'Pierre', 5500.00, 5),
('Durand', 'Julie', 2900.00, 1),
('Moreau', 'Thomas', 3500.00, 2),
('Laurent', 'Camille', 4200.00, 3);