use aozora_bunko;
CREATE TABLE `works` (
 `id` int(11) unsigned NOT NULL,
 `writer_id` int(11) NOT NULL,
 `title` varchar(255) NOT NULL DEFAULT '',
 `mojidukai_type_id` int(11) NOT NULL,
 `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
 `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
INSERT INTO `works` (`id`, `writer_id`, `title`, `mojidukai_type_id`)
VALUES
 (127, 879, '羅生門', 1),
 (128, 879, '羅生門', 2),
 (3757, 879, '世の中と女', 1);
