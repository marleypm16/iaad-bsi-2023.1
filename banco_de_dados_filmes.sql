CREATE DATABASE estante_de_filmes
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_general_ci;

USE estante_de_filmes;

CREATE TABLE IF NOT EXISTS work_diretores (
    Coddiretores INT AUTO_INCREMENT,
    Nomediretores VARCHAR(255),
    tipo_show VARCHAR(7) NOT NULL,
    PRIMARY KEY (Coddiretores)
) DEFAULT CHARSET = utf8mb4;

INSERT INTO work_diretores
(Coddiretores, Nomediretores, tipo_show)
VALUES
(1, 'Kyle Newacheck', 'Movie'),
(2, 'Brian Volk-Weiss', 'Movie'),
(3, 'Arsenio Hall', 'Movie'),
(4, 'Reece Pockney, Scott Langley, Alex Babic, Gemma Harvey, Jessica Hann, Emma Tate', 'TV Show'),
(5, NULL, 'TV Show'),
(6, NULL, 'TV Show'),
(7, NULL, 'TV Show'),
(8, NULL, 'TV Show'),
(9, 'Monica Floyd', 'Movie'),
(10, 'Duncan Jones', 'Movie'),
(11, 'Mike Secher', 'TV Show'),
(12, 'Christian Gudegast', 'Movie')
;

CREATE TABLE IF NOT EXISTS filmes (
    show_id INT AUTO_INCREMENT,
    title VARCHAR(40) NOT NULL,
    duration VARCHAR(25),
    listen_in VARCHAR(400),
    Coddiretores INT,
    PRIMARY KEY (show_id),
    UNIQUE (title),
    FOREIGN KEY (Coddiretores)
    REFERENCES work_diretores(Coddiretores)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) DEFAULT CHARSET = utf8mb4;


INSERT INTO filmes
(title, duration, listen_in, Coddiretores)
VALUES
('Game Over, Man!', '102 min', 'Action & Adventure, Comedies', 1),
('Arsenio Hall: Smart & Classy', '63 min', 'Stand-Up Comedy', 2),
('Kazoops!', NULL, 'Kids'' TV', 3),
('We Are the Champions', '1 Season', 'Docuseries, Reality TV', 4),
('Pablo Escobar, el patrón del mal', '1 Season', 'Crime TV Shows, International TV Shows, Spanish-Language TV Shows', 5),
('Saint Seiya: The Lost Canvas', '1 Season', 'Anime Series, International TV Shows', 6),
('Fauda', '3 Seasons', 'Crime TV Shows, International TV Shows, TV Action & Adventure', 7),
('The Cook of Castamar', '1 Season', 'International TV Shows, Romantic TV Shows, Spanish-Language TV Shows', 8),
('The App That Stole Christmas', '64 min', 'Children & Family Movies, Comedies', 9),
('Mute', '127 min', 'Sci-Fi & Fantasy, Thrillers', 10),
('Drugs, Inc.', '1 Season', 'Crime TV Shows, Docuseries', 11),
('Den of Thieves', '140 min', 'Action & Adventure', 12)
;
create table if not exists pais_filme(
	pais_id INT AUTO_INCREMENT,
    show_id int,
    nome_pais varchar(100),
    primary key(pais_id),
	FOREIGN KEY (show_id)
	REFERENCES filmes(show_id)
	ON DELETE CASCADE
);

insert into pais_filme (pais_id,show_id,nome_pais) values(
	1,3,'USA'),(2,4,'Brasil');
select * from filmes;
DELIMITER $$
CREATE TRIGGER verifica_duration
BEFORE INSERT ON filmes
FOR EACH ROW
BEGIN
    IF NEW.duration NOT LIKE '%min%' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'não esqueça de adicionar a medida de tempo em "%min%"';
    END IF;
END$$
DELIMITER ;
