CREATE TABLE `mojidukai_types` (
 `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
 `name` varchar(8) NOT NULL DEFAULT '',
 `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
INSERT INTO `mojidukai_types` (`id`, `name`)
VALUES
 (1, '新字旧仮名'),
 (2, '旧字旧仮名');
