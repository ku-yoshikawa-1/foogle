CREATE DATABASE  IF NOT EXISTS `db`  DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `db`;

DROP TABLE IF EXISTS `product_info`;
CREATE TABLE `product_info` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(45) DEFAULT NULL,
  `product_type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`product_id`),
  UNIQUE KEY `product_id_UNIQUE` (`product_id`),
  UNIQUE KEY `product_name_UNIQUE` (`product_name`)
);

DROP TABLE IF EXISTS `shop_info`;
CREATE TABLE `shop_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `Latitude` float NOT NULL,
  `Longitude` float NOT NULL,
  `Brand` varchar(45) DEFAULT NULL,
  `Shop_descriptioncol` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
);

DROP TABLE IF EXISTS `bargain_info`;
CREATE TABLE `bargain_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) DEFAULT NULL,
  `shop_id` int(11) DEFAULT NULL,
  `price` int(11) unsigned DEFAULT NULL,
  `product_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `product_id_idx` (`product_id`),
  KEY `shop_id_idx` (`shop_id`),
  CONSTRAINT `product_id` FOREIGN KEY (`product_id`) REFERENCES `product_info` (`product_id`),
  CONSTRAINT `shop_id` FOREIGN KEY (`shop_id`) REFERENCES `shop_info` (`id`)
);

--
-- Table structure for table `product_info`
--
