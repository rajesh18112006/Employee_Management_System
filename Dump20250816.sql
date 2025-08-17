-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `attendance`
--

DROP TABLE IF EXISTS `attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendance` (
  `employeeid` int NOT NULL,
  `employeename` varchar(100) DEFAULT NULL,
  `jobroll` varchar(50) DEFAULT NULL,
  `present` int DEFAULT NULL,
  `overtime` int DEFAULT NULL,
  `leavedays` int DEFAULT NULL,
  PRIMARY KEY (`employeeid`),
  CONSTRAINT `attendance_ibfk_1` FOREIGN KEY (`employeeid`) REFERENCES `employeedetails` (`employeeid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendance`
--

LOCK TABLES `attendance` WRITE;
/*!40000 ALTER TABLE `attendance` DISABLE KEYS */;
INSERT INTO `attendance` VALUES (101,'RAJESH','MANAGER',28,4,2),(102,'ARUN KUMAR','SOFTWARE DEVELOPER',27,4,3),(103,'KUMARAN','WEB DEVELOPER',25,8,5),(104,'HARINI','MECHANICAL DEVELOPER',25,12,5),(105,'DEEPAK','CIVIL DEVELOPER',23,16,7),(106,'PAVITHRA','DATA ANALYST',26,6,4),(107,'SANJAY','DATABASE ADMINISTRATOR',27,8,3);
/*!40000 ALTER TABLE `attendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employeedetails`
--

DROP TABLE IF EXISTS `employeedetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employeedetails` (
  `employeeid` int NOT NULL,
  `employeename` varchar(100) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `dateofbirth` date DEFAULT NULL,
  `qualification` varchar(100) DEFAULT NULL,
  `jobroll` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`employeeid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employeedetails`
--

LOCK TABLES `employeedetails` WRITE;
/*!40000 ALTER TABLE `employeedetails` DISABLE KEYS */;
INSERT INTO `employeedetails` VALUES (101,'RAJESH','MALE','2004-11-18','B-TECH CSE','MANAGER'),(102,'ARUN KUMAR','MALE','2000-02-10','B-TECH IT','SOFTWARE DEVELOPER'),(103,'KUMARAN','MALE','2000-08-20','B-TECH CSE','WEB DEVELOPER'),(104,'HARINI','FEMALE','2002-11-05','BE MECH','MECHANICAL DEVELOPER'),(105,'DEEPAK','MALE','2000-02-10','BE CIVIL','CIVIL DEVELOPER'),(106,'PAVITHRA','FEMALE','2000-02-10','B-TECH AIDS','DATA ANALYST'),(107,'SANJAY','MALE','2000-02-10','BSC CS','DATABASE ADMINISTRATOR');
/*!40000 ALTER TABLE `employeedetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salary`
--

DROP TABLE IF EXISTS `salary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salary` (
  `employeeid` int NOT NULL,
  `employeename` varchar(100) DEFAULT NULL,
  `basicpay` int DEFAULT NULL,
  `reduction` int DEFAULT NULL,
  `totalsalary` int DEFAULT NULL,
  `issuedate` date DEFAULT NULL,
  PRIMARY KEY (`employeeid`),
  CONSTRAINT `salary_ibfk_1` FOREIGN KEY (`employeeid`) REFERENCES `employeedetails` (`employeeid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salary`
--

LOCK TABLES `salary` WRITE;
/*!40000 ALTER TABLE `salary` DISABLE KEYS */;
INSERT INTO `salary` VALUES (101,'RAJESH',50000,3333,47500,'2024-07-23'),(102,'ARUN KUMAR',40000,4000,36667,'2024-07-23'),(103,'KUMARAN',30000,5000,26000,'2024-07-23'),(104,'HARINI',35000,5833,30917,'2024-07-23'),(105,'DEEPAK',40000,9333,33334,'2024-07-23'),(106,'PAVITHRA',40000,5333,35667,'2024-07-23'),(107,'SANJAY',30000,3000,28000,'2024-11-23');
/*!40000 ALTER TABLE `salary` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-16 15:51:27
