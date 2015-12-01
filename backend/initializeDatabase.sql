CREATE DATABASE `FamishedBuffs` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;

USE `FamishedBuffs`;

CREATE TABLE IF NOT EXISTS `DiningHalls` (
  `ID` int(1) NOT NULL,
  `Hall` varchar(64) NOT NULL,
  `Station` varchar(64) DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS `Hours` (
  `HallID` int(1) NOT NULL,
  `Open` varchar(6) DEFAULT NULL,
  `Close` varchar(6) DEFAULT NULL,
  `Day` varchar(10) DEFAULT NULL,
  `Meal` varchar(10) DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS `Meal` (
  `HallID` int(1) NOT NULL,
  `Day` varchar(10) DEFAULT NULL,
  `Item` varchar(64) NOT NULL,
  `MealType` varchar(32) DEFAULT NULL 
);
