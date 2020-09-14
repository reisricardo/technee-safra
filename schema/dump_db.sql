CREATE DATABASE  IF NOT EXISTS `open` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `open`;
-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: open
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `aux_banks`
--

DROP TABLE IF EXISTS `aux_banks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aux_banks` (
  `code` varchar(16) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `image_path` varchar(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aux_banks`
--

LOCK TABLES `aux_banks` WRITE;
/*!40000 ALTER TABLE `aux_banks` DISABLE KEYS */;
INSERT INTO `aux_banks` VALUES ('BancoPlayerI','Banco Player I','https://raw.githubusercontent.com/reisricardo/static/master/player_i.svg'),('BancoPlayerS','Branco Player S','https://raw.githubusercontent.com/reisricardo/static/master/player_s.svg'),('BancoSafra','Banco Safra','https://raw.githubusercontent.com/reisricardo/static/master/logo-safra-no-text.svg');
/*!40000 ALTER TABLE `aux_banks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `aux_transactions`
--

DROP TABLE IF EXISTS `aux_transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aux_transactions` (
  `account_id` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `transaction_id` int NOT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `currency` char(3) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `operation` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `booking_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `value_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `information` varchar(128) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `aux_banks_code` varchar(16) COLLATE utf8mb4_unicode_ci NOT NULL,
  `users_identification` varchar(14) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`account_id`,`transaction_id`,`users_identification`,`aux_banks_code`),
  KEY `fk_aux_transactions_aux_banks_idx` (`aux_banks_code`),
  KEY `fk_aux_transactions_users1_idx` (`users_identification`),
  CONSTRAINT `fk_aux_transactions_aux_banks` FOREIGN KEY (`aux_banks_code`) REFERENCES `aux_banks` (`code`),
  CONSTRAINT `fk_aux_transactions_users1` FOREIGN KEY (`users_identification`) REFERENCES `users` (`identification`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aux_transactions`
--

LOCK TABLES `aux_transactions` WRITE;
/*!40000 ALTER TABLE `aux_transactions` DISABLE KEYS */;
INSERT INTO `aux_transactions` VALUES ('00335789333',959911,1256.24,'BRL','Debit','2020-08-07 13:43:07','2020-08-07 13:45:22','Pagamento de boleto','BancoPlayerS','12345678901233'),('00335789333',997921,75.60,'BRL','Credit','2020-07-10 14:43:07','2020-07-10 14:45:22','TED 10923 232','BancoPlayerS','12345678901233'),('0034145633',45689,10456.23,'BRL','Invest','2020-08-05 13:43:07','2020-08-05 13:45:22','Aplic Poupança','BancoPlayerI','12345678901233'),('0034145633',45690,1256.78,'BRL','Invest','2020-07-02 13:43:07','2020-07-02 13:45:22','Aplic Poupança','BancoPlayerI','12345678901233'),('0034145633',45693,1058.78,'BRL','Invest','2020-06-16 13:43:07','2020-06-16 13:45:22','CDB 120% CDI','BancoPlayerI','12345678901233'),('0034145633',999911,450.00,'BRL','Debit','2020-08-05 13:43:07','2020-08-05 13:45:22','Compra no mercado','BancoPlayerI','12345678901233'),('0034145633',999921,150.00,'BRL','Credit','2020-05-10 14:43:07','2020-05-10 14:45:22','Depósito em espécie','BancoPlayerI','12345678901233'),('00711234533',999911,250.00,'BRL','Debit','2020-04-05 13:43:07','2020-04-05 13:45:22','Mensalidade Academia','BancoSafra','12345678901233'),('00711234533',999921,8000.00,'BRL','Credit','2020-05-09 14:43:07','2020-05-09 14:45:22','Entrada Compra Carro','BancoSafra','12345678901233');
/*!40000 ALTER TABLE `aux_transactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `uid` char(64) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `identification` varchar(14) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `creation_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `failed_attempts` char(1) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '0',
  `blocked_account` tinyint(1) NOT NULL DEFAULT '0',
  `syncronize_status` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`identification`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (NULL,'12345678901233','Mark Zuckerberg da Silva','2020-09-13 00:46:44','0',0,0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-13 22:27:38
