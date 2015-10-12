CREATE DATABASE `FamishedBuffs` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;

USE `FamishedBuffs`;

CREATE TABLE IF NOT EXISTS `DiningHalls` (
  `ID` varchar(4) DEFAULT NULL,
  `Hall` varchar(64) DEFAULT NULL,
  `Station` varchar(64) DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS `Hours` (
  `ID` varchar(4) DEFAULT NULL,
  `Open` varchar(6) DEFAULT NULL,
  `Close` varchar(6) DEFAULT NULL,
  `Description` varchar(10) DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS `Breakfast` (
  `ID` varchar(4) DEFAULT NULL,
  `Item` varchar(64) DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS `Lunch` (
  `ID` varchar(4) DEFAULT NULL,
  `Item` varchar(64) DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS `Dinner` (
  `ID` varchar(4) DEFAULT NULL,
  `Item` varchar(64) DEFAULT NULL
);
