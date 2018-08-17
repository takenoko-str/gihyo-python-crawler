CREATE DATABASE quotes DEFAULT CHARACTER SET utf8;
use quotes;

CREATE TABLE `quotes` (
 `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
 `author` varchar(255) DEFAULT NULL,
 `text` text,
 `text_hash` char(64) DEFAULT NULL,
 `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
 `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 PRIMARY KEY (`id`),
 UNIQUE KEY `text_hash` (`text_hash`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tags` (
 `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
 `name` varchar(255) NOT NULL DEFAULT '',
 `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
 `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 PRIMARY KEY (`id`),
 UNIQUE KEY `tag` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

CREATE TABLE `quotes_tags` (
 `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
 `quote_id` int(11) NOT NULL,
 `tag_id` int(11) NOT NULL,
 `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
 `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 PRIMARY KEY (`id`),
 UNIQUE KEY `quote_tag` (`quote_id`,`tag_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
