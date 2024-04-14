-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 16, 2022 at 04:55 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `PrototypeDB`
--

-- --------------------------------------------------------

--
-- Table structure for table `Entries`
--

CREATE TABLE `Entries` (
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `firstname` varchar(255) DEFAULT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  `entryID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Entries`
--

INSERT INTO `Entries` (`username`, `password`, `firstname`, `lastname`, `entryID`) VALUES
('psyxp1', 'admin', 'Xavier', 'Parnell', 1),
('psycc4', 'admin', 'Conor', 'Cowley', 2),
('psylm11', 'admin', 'Louis', 'Maurice', 3),
('psyhs11', 'admin', 'Hitarth', 'Shah', 4),
('efyre1', 'admin', 'Ronnan', 'El-Hames', 5),
('psyja10', 'admin', 'James', 'Ashenden', 6),
('psyts15', 'admin', 'Trijit', 'Saha', 10),
('pszik', 'admin', 'Ian', 'Knight', 11),
('admin', 'admin', 'NA', 'NA', 12);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Entries`
--
ALTER TABLE `Entries`
  ADD PRIMARY KEY (`entryID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Entries`
--
ALTER TABLE `Entries`
  MODIFY `entryID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
