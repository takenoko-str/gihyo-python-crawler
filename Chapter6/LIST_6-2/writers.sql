CREATE TABLE `writers` (
  `id` int(11) unsigned NOT NULL,
  `name` varchar(128) NOT NULL DEFAULT '',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `writers` (`id`, `name`)
VALUES
	(879, '芥川 竜之介');
