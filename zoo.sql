

CREATE DATABASE zoo;
USE zoo;

-- Table des cages
CREATE TABLE cage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    superficie FLOAT NOT NULL,
    capacite_max INT NOT NULL
);

-- Table des animaux
CREATE TABLE animal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    race VARCHAR(100) NOT NULL,
    cage_id INT,
    date_naissance DATE NOT NULL,
    pays_origine VARCHAR(100) NOT NULL,
    FOREIGN KEY (cage_id) REFERENCES cage(id) ON DELETE SET NULL
);
