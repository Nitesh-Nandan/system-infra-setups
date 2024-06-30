
CREATE DATABASE IF NOT EXISTS airlines;

DROP TABLE IF EXISTS airlines.`users`;

Use airlines;

CREATE TABLE airlines.`users` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `firstName` varchar(30) NOT NULL,
  `lastName` varchar(30) NOT NULL,
  `age` int(3) NOT NULL,
  `city` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
