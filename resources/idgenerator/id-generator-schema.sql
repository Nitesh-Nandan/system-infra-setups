CREATE DATABASE IF NOT EXISTS idgenerator;

DROP TABLE IF EXISTS idgenerator.`id_generator`;

CREATE TABLE idgenerator.`id_generator` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `stub` char(1) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;