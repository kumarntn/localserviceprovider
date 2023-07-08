-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2023 at 12:20 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nexus`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(5) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`) VALUES
(1, 'administrator', 'admin@123'),
(2, 'adm', '123');

-- --------------------------------------------------------

--
-- Table structure for table `contractors`
--

CREATE TABLE `contractors` (
  `id` int(5) NOT NULL,
  `cnr_id` varchar(15) NOT NULL,
  `cmpny` varchar(50) NOT NULL,
  `name` varchar(30) NOT NULL,
  `contact` bigint(12) NOT NULL,
  `mailid` varchar(50) NOT NULL,
  `city` varchar(25) NOT NULL,
  `type_of_services` varchar(200) NOT NULL,
  `working_day` varchar(25) NOT NULL,
  `profile` varchar(100) NOT NULL,
  `id_proof` varchar(100) NOT NULL,
  `username` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contractors`
--

INSERT INTO `contractors` (`id`, `cnr_id`, `cmpny`, `name`, `contact`, `mailid`, `city`, `type_of_services`, `working_day`, `profile`, `id_proof`, `username`, `password`, `status`) VALUES
(1, 'cnr0001', 'Netcon', 'Karthi Keyan', 9876543210, 'karthi@gmail.com', 'Covai', 'House Keeping', 'All Days', 'img5.jfif', 'idpf.jpg', 'cnr0001', '54321', 'Accept'),
(2, 'cnr0002', 'JJ', 'Tharani', 9876543210, 'thara@gmail.com', 'Covai', 'Plumber, Electrician, House Keeping', 'All Days', 'img3.jfif', 'idpf.jpg', 'cnr0002', '54321', 'Accept'),
(3, 'cnr0003', 'JK', 'Selvam', 7654321890, 'selvam@gmail.com', 'Covai', 'Painter, Carpenter, Plumber, Electrician, House Keeping, Security', 'All Days', 'admin.jpg', 'idpf.jpg', 'cnr0003', '54321', 'Accept');

-- --------------------------------------------------------

--
-- Table structure for table `feedbacks`
--

CREATE TABLE `feedbacks` (
  `id` int(5) NOT NULL,
  `srvc_id` varchar(15) NOT NULL,
  `service` varchar(30) NOT NULL,
  `usr_id` varchar(15) NOT NULL,
  `usr_name` varchar(30) NOT NULL,
  `user_feedback` varchar(100) NOT NULL,
  `wkr_id` varchar(15) NOT NULL,
  `wkr_name` varchar(30) NOT NULL,
  `wkr_feedback` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `feedbacks`
--

INSERT INTO `feedbacks` (`id`, `srvc_id`, `service`, `usr_id`, `usr_name`, `user_feedback`, `wkr_id`, `wkr_name`, `wkr_feedback`) VALUES
(1, 'srvc0001', 'Electrician', 'usr0001', 'Gowsalya', 'Good Service, Thank you!!!', 'wkr0001', 'Tamil Selvan', 'Good'),
(2, 'srvc0002', 'House Keeping', 'usr0001', 'Gowsalya', 'Good service', 'cnr0002', 'Tharani', 'Nice'),
(3, 'srvc0004', 'House Keeping', 'usr0001', 'Gowsalya', '', '', '', ''),
(4, 'srvc0005', 'House Keeping', 'usr0002', 'Harshini', '', 'cnr0001', 'Karthi Keyan', ''),
(5, 'srvc0006', 'Painter', 'usr0001', 'Gowsalya', 'good', 'cnr0002', 'Tharani', '');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `id` int(5) NOT NULL,
  `srvc_id` varchar(15) NOT NULL,
  `amount` int(8) NOT NULL,
  `usr_id` varchar(15) NOT NULL,
  `usr_name` varchar(30) NOT NULL,
  `type` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`id`, `srvc_id`, `amount`, `usr_id`, `usr_name`, `type`) VALUES
(1, 'srvc0001', 2000, 'usr0001', 'Gowsalya', 'Online Payment'),
(2, 'srvc0002', 3000, 'usr0001', 'Gowsalya', 'Cash');

-- --------------------------------------------------------

--
-- Table structure for table `services`
--

CREATE TABLE `services` (
  `id` int(5) NOT NULL,
  `srvc_id` varchar(15) NOT NULL,
  `service` varchar(30) NOT NULL,
  `sdate` varchar(15) NOT NULL,
  `venue` varchar(25) NOT NULL,
  `usr_id` varchar(15) NOT NULL,
  `usr_name` varchar(30) NOT NULL,
  `wkr_id` varchar(15) NOT NULL,
  `wkr_name` varchar(30) NOT NULL,
  `cost` int(8) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `services`
--

INSERT INTO `services` (`id`, `srvc_id`, `service`, `sdate`, `venue`, `usr_id`, `usr_name`, `wkr_id`, `wkr_name`, `cost`, `status`) VALUES
(1, 'srvc0001', 'Electrician', '2023-04-09', 'Covai', 'usr0001', 'Gowsalya', 'wkr0001', 'Tamil Selvan', 2000, 'Finished'),
(3, 'srvc0002', 'House Keeping', '2023-04-09', 'Covai', 'usr0001', 'Gowsalya', 'cnr0002', 'Tharani', 3000, 'Finished'),
(4, 'srvc0004', 'House Keeping', '2023-04-09', 'Covai', 'usr0001', 'Gowsalya', '', '', 0, 'New'),
(5, 'srvc0005', 'House Keeping', '2023-04-17', 'Madurai', 'usr0002', 'Harshini', 'cnr0001', 'Karthi Keyan', 5000, 'Accept'),
(6, 'srvc0006', 'Painter', '2023-03-09', 'Covai', 'usr0001', 'Gowsalya', 'cnr0002', 'Tharani', 50000, 'Finished');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(5) NOT NULL,
  `usr_id` varchar(15) NOT NULL,
  `name` varchar(30) NOT NULL,
  `contact` bigint(12) NOT NULL,
  `mailid` varchar(50) NOT NULL,
  `city` varchar(25) NOT NULL,
  `profile` varchar(100) NOT NULL,
  `id_proof` varchar(100) NOT NULL,
  `username` varchar(15) NOT NULL,
  `password` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `usr_id`, `name`, `contact`, `mailid`, `city`, `profile`, `id_proof`, `username`, `password`) VALUES
(1, 'usr0001', 'Gowsalya', 8765432190, 'gowsalya@gmail.com', 'Covai', 'img4.jfif', 'idpf.jpg', 'usr0001', '54321'),
(2, 'usr0002', 'Harshini', 7654321890, 'harshini@gmail.com', 'Madurai', 'img6.jfif', 'idpf.jpg', 'usr0002', '54321');

-- --------------------------------------------------------

--
-- Table structure for table `workers`
--

CREATE TABLE `workers` (
  `id` int(5) NOT NULL,
  `wkr_id` varchar(15) NOT NULL,
  `name` varchar(30) NOT NULL,
  `contact` bigint(12) NOT NULL,
  `mailid` varchar(40) NOT NULL,
  `city` varchar(25) NOT NULL,
  `experience` varchar(25) NOT NULL,
  `type_of_services` varchar(25) NOT NULL,
  `working_day` varchar(20) NOT NULL,
  `profile` varchar(100) NOT NULL,
  `idproof` varchar(100) NOT NULL,
  `username` varchar(15) NOT NULL,
  `password` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `workers`
--

INSERT INTO `workers` (`id`, `wkr_id`, `name`, `contact`, `mailid`, `city`, `experience`, `type_of_services`, `working_day`, `profile`, `idproof`, `username`, `password`, `status`) VALUES
(1, 'wkr0001', 'Tamil Selvan', 7654321890, 'tamil@gmail.com', 'Covai', 'Above 3 years', 'Electrician', 'All Days', 'img1.jfif', 'idpf.jpg', 'wkr0001', '54321', 'Accept'),
(2, 'wkr0002', 'Malathi', 6789054321, 'malathi@gmail.com', 'Trichy', 'Above 3 years', 'Painter', 'Mon-Sat', 'img2.jfif', 'idpf.jpg', 'wkr0002', '54321', 'Accept'),
(3, 'wkr0003', 'Angel', 8765432190, 'angel@gmail.com', 'Madurai', '3 years', 'House Keeping', 'All Days', 'img4.jfif', 'idpf.jpg', 'wkr0003', '54321', 'Pending');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `contractors`
--
ALTER TABLE `contractors`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `feedbacks`
--
ALTER TABLE `feedbacks`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `services`
--
ALTER TABLE `services`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `workers`
--
ALTER TABLE `workers`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `contractors`
--
ALTER TABLE `contractors`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `feedbacks`
--
ALTER TABLE `feedbacks`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `services`
--
ALTER TABLE `services`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `workers`
--
ALTER TABLE `workers`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
