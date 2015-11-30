CREATE DATABASE `FamishedBuffs` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;

USE `FamishedBuffs`;

CREATE TABLE IF NOT EXISTS `DiningHalls` (
  `ID` int(1) NOT NULL auto_increment,
  `Hall` varchar(64) NOT NULL,
  `Station` varchar(64) DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS `Hours` (
  `ID` int(1) NOT NULL auto_increment,
  `Day` varchar(10) NOT NULL
  `Open` varchar(6) NOT NULL,
  `Close` varchar(6) NOT NULL,
  `HallID` int(1) NOT NULL,
  `Description` varchar(10) DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS `Breakfast` (
  `ID` int(1) NOT NULL auto_increment,
  `Item` varchar(64)NOT NULL,
  `HourID` int(1) NOT NULL
);

CREATE TABLE IF NOT EXISTS `Lunch` (
  `ID` int(1) NOT NULL auto_increment,
  `Item` varchar(64) DEFAULT NULL,
  `HourID` int(1) NOT NULL
);

CREATE TABLE IF NOT EXISTS `Dinner` (
  `ID` int(1) NOT NULL auto_increment,
  `Item` varchar(64) DEFAULT NULL,
  `HourID` int(1) NOT NULL
);
