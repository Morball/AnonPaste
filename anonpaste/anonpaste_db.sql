-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 22, 2022 at 02:04 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `anonpaste_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `pastes`
--

CREATE TABLE `pastes` (
  `paste_number` int(11) NOT NULL,
  `paste_title` text NOT NULL,
  `paste_id` varchar(255) NOT NULL,
  `paste_content` text NOT NULL,
  `time_of_paste` varchar(255) NOT NULL,
  `ip_address` varchar(255) NOT NULL,
  `is_private` tinyint(1) NOT NULL,
  `visit_no` int(11) NOT NULL,
  `is_otv` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pastes`
--

INSERT INTO `pastes` (`paste_number`, `paste_title`, `paste_id`, `paste_content`, `time_of_paste`, `ip_address`, `is_private`, `visit_no`, `is_otv`) VALUES
(17, 'muie dinamo', 'SxenYfZDWteT', 'hai salut coaie ce fa ma\r\n', '05/19/22 09:57:17', '127.0.0.1', 0, 2, 0),
(18, 'muie steaua', 'DwNlUFhSOdGO', 'ce fa coi\r\n', '05/19/22 09:58:56', '127.0.0.1', 1, 5, 0),
(19, 'muie steaua', 'TYEHFQDnBcwd', 'inca o data coaie', '05/19/22 10:00:23', '127.0.0.1', 0, 2, 1),
(20, 'da koi', 'rCcODpAdtAmx', 'hai salut ma axel', '05/19/22 10:05:00', '127.0.0.1', 0, 3, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pastes`
--
ALTER TABLE `pastes`
  ADD PRIMARY KEY (`paste_number`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pastes`
--
ALTER TABLE `pastes`
  MODIFY `paste_number` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
