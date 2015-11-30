CREATE DATABASE `FamishedBuffs` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;

USE `FamishedBuffs`;

CREATE TABLE IF NOT EXISTS `DiningHalls` (
  `ID` int(1) NOT NULL auto_increment,
  `Hall` varchar(64) NOT NULL,
  `Station` varchar(64) DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS `Hours` (
  `ID` int(1) NOT NULL auto_increment,
  `Day` varchar(10) DEFAULT NULL
  `Open` varchar(6) DEFAULT NULL,
  `Close` varchar(6) DEFAULT NULL,
  `HallID` int(1) NOT NULL
);

CREATE TABLE IF NOT EXISTS `Meal` (
  `ID` int(1) NOT NULL auto_increment,
  `MealType` varchar(32) DEFAULT NULL 
  `Item` varchar(64) NOT NULL,
  `HourID` int(1) NOT NULL,
  `HallID` int(1) NOT NULL
);
