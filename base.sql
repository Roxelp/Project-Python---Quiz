-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 27, 2017 at 01:45 PM
-- Server version: 5.5.50-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `test`
--

-- --------------------------------------------------------

--
-- Table structure for table `pytania`
--

CREATE TABLE IF NOT EXISTS `pytania` (
  `id_pytania` int(11) NOT NULL AUTO_INCREMENT,
  `id_testu` int(11) NOT NULL,
  `pytanie` tinytext NOT NULL,
  `odp1` tinytext NOT NULL,
  `odp2` tinytext NOT NULL,
  `odp3` tinytext NOT NULL,
  `odp4` tinytext NOT NULL,
  `prawidlowa` int(11) NOT NULL,
  PRIMARY KEY (`id_pytania`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `pytania`
--

INSERT INTO `pytania` (`id_pytania`, `id_testu`, `pytanie`, `odp1`, `odp2`, `odp3`, `odp4`, `prawidlowa`) VALUES
(2, 1, 'Ile Adam ma lat?', '1', '2', '3', '2', 2),
(3, 1, 'gf', 'fgf', 'gf', 'gfg', 'fg', 1),
(4, 1, 'gf', 'fgf', 'gf', 'gfg', 'fg', 1),
(5, 1, 'gf', 'fgf', 'gf', 'gfg', 'fg', 1),
(6, 1, 'hgh', 'gg', 'g', 'hg', 'ghgh', 1);

-- --------------------------------------------------------

--
-- Table structure for table `testy`
--

CREATE TABLE IF NOT EXISTS `testy` (
  `id_testu` int(11) NOT NULL AUTO_INCREMENT,
  `nazwa` tinytext NOT NULL,
  `kategoria` tinytext NOT NULL,
  `trudnosc` tinytext NOT NULL,
  PRIMARY KEY (`id_testu`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `testy`
--

INSERT INTO `testy` (`id_testu`, `nazwa`, `kategoria`, `trudnosc`) VALUES
(2, 'fd', 'fdf', 'dfd'),
(3, '143', '2323', '43'),
(4, 'Test wiedzy o mejzurze', 'Mejzur', 'Over9000');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
