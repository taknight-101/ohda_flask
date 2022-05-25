-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Sep 22, 2021 at 07:08 AM
-- Server version: 8.0.21
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask_ohda`
--

-- --------------------------------------------------------

--
-- Table structure for table `devs`
--

DROP TABLE IF EXISTS `devs`;
CREATE TABLE IF NOT EXISTS `devs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `status` enum('1','2','3',''),
  `place` text ,
  `type_id` text NOT NULL,
  `sn` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=30 ;

-- --------------------------------------------------------

--
-- Table structure for table `registered_routes`
--

DROP TABLE IF EXISTS `registered_routes`;
CREATE TABLE IF NOT EXISTS `registered_routes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_method` varchar(255) DEFAULT NULL,
  `add_actions` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=42 ;

--
-- Dumping data for table `registered_routes`
--

INSERT INTO `registered_routes` (`id`, `action_method`, `add_actions`) VALUES
(1, 'pcs', 'add_pcs'),
(2, 'laptops', 'add_laptops'),
(3, 'monitors', 'add_monitors'),
(4, 'printers', 'add_printers');

-- --------------------------------------------------------

--
-- Table structure for table `routes_in_code`
--

DROP TABLE IF EXISTS `routes_in_code`;
CREATE TABLE IF NOT EXISTS `routes_in_code` (
  `id` int NOT NULL AUTO_INCREMENT,
  `routeName` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 ;

-- --------------------------------------------------------

--
-- Table structure for table `types`
--

DROP TABLE IF EXISTS `types`;
CREATE TABLE IF NOT EXISTS `types` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type` text NOT NULL,
  `cls` text ,
  `icon` text NOT NULL,
  `action_method` text NOT NULL,
  `add_actions` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=61 ;

--
-- Dumping data for table `types`
--

INSERT INTO `types` (`id`, `type`, `cls`, `icon`, `action_method`, `add_actions`) VALUES
(1, 'pc,كيسة كمبيوتر ', 'small-box bg-info', 'fas fa-keyboard', 'pcs', 'add_pcs'),
(2, 'laptop,لابتوب', 'small-box bg-success', 'fas fa-laptop', 'laptops', 'add_laptops'),
(3, 'monitors,شاشات', 'small-box bg-warning', 'fas fa-chalkboard-teacher', 'monitors', 'add_monitors'),
(4, 'printers,طابعات', 'small-box bg-danger', 'fas fa-print', 'printers', 'add_printers');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
