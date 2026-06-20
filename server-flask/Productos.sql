-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 18-06-2026 a las 21:04:42
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `Cafeteria`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Productos`
--

use cafeteria



CREATE TABLE `Productos` (
  `id_producto` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `categoria` varchar(50) DEFAULT NULL,
  `precio` decimal(10,2) NOT NULL,
  `stock` int(11) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

ALTER TABLE `Productos` 

ADD COLUMN `ingredientes` varchar(255) DEFAULT NULL,
ADD COLUMN `disponibles` tinyint(1) DEFAULT 1,
ADD COLUMN `OPCIONES_PARA_ARMAR_TU_ALIMENTO` varchar(255) DEFAULT NULL



--
-- Volcado de datos para la tabla `Productos`
--

INSERT INTO `Productos` (`id_producto`, `nombre`, `categoria`, `precio`, `stock`, `ingredientes`, `disponibles`, `OPCIONES_PARA_ARMAR_TU_ALIMENTO`) VALUES
(15, 'Margarita', 'Cócteles', 100.00, 20, 'Bacardi Blanco\r\nMenta\r\nLimon', 1, NULL),
(16, 'Malibu Bay Breeze', 'Cócteles', 150.00, 20, 'Malibu\r\nJugo De Piña\r\nJugo De Arandanos', 1, NULL),
(17, 'Mimosa de Cereza', 'Cócteles', 150.00, 20, 'Vino Espumoso\r\nCereza\r\nJugo De Naranja', 1, NULL),
(18, 'Carajillo', 'Cócteles', 200.00, 20, 'Licor 43\r\nCafe', 1, NULL),
(19, 'Alfonso 13', 'Cócteles', 180.00, 20, 'Kahalua\r\nClavel\r\nCereza', 1, NULL),
(20, 'Paloma', 'Cócteles', 150.00, 20, 'Tequila\r\nSoda De Toronja\r\nLimon\r\nSal', 1, NULL),
(21, 'Cuba Libre', 'Cócteles', 100.00, 20, 'Ron\r\nCoca Cola\r\nLimon', 1, NULL),
(22, 'Piña Colada', 'Cócteles', 150.00, 20, 'Ron\r\nJugo De Piña\r\nCrema De Coco', 1, NULL),
(23, 'Rol Lotus', 'Roles de Canela', 100.00, 15, NULL, 1, NULL),
(24, 'Rol Oreo', 'Roles de Canela', 100.00, 15, NULL, 1, NULL),
(25, 'Rol Frutos Rojos', 'Roles de Canela', 100.00, 15, NULL, 1, NULL),
(26, 'Cupcake Lotus', 'Cupcakes', 50.00, 15, NULL, 1, NULL),
(27, 'Cupcake Oreo', 'Cupcakes', 50.00, 15, NULL, 1, NULL),
(28, 'Cupcake Fresa', 'Cupcakes', 50.00, 15, NULL, 1, NULL),
(29, 'Brownie Nuez', 'Brownies', 65.00, 10, NULL, 1, NULL),
(30, 'Brownie Oreo', 'Brownies', 65.00, 10, NULL, 1, NULL),
(31, 'Brownie Kinder Delice', 'Brownies', 65.00, 10, NULL, 1, NULL),
(32, 'NutriSushi', 'Entrada', 150.00, 20, 'Arroz integral para sushi\r\nPepino\r\nZanahoria\r\nAguacate\r\nAtún\r\nPollo\r\nSalmón\r\nAlga nori\r\nAjonjoli', 1, 'Pepino\r\nZanahoria\r\nAtún\r\nPollo\r\nAjonjolí'),
(33, 'Bruschettas', 'Snack', 120.00, 20, 'Pan integral\r\nHuevo\r\nAguacate\r\nQueso fresco\r\nJitomate\r\nLimon\r\nAceite de oliva', 1, 'Queso fresco\r\nJitomate\r\nLimon\r\nAceite de oliva'),
(34, 'Mini Sandwich', 'Platillo Fuerte', 180.00, 20, 'Pan integral\r\nPechuga de pollo\r\nJamon de pavo\r\nEspinaca\r\nLechuga\r\nJitomate\r\nAguacate\r\nLimon\r\nSal\r\nYogur', 1, 'Pollo o Jamon de pavo\r\nEspinaca\r\nLechuga\r\nAguacate\r\nAderezo de yogur o aguacate\r\n');



UPDATE `Productos` 
SET `OPCIONES_PARA_ARMAR_TU_ALIMENTO` = REPLACE(`OPCIONES_PARA_ARMAR_TU_ALIMENTO`, '\r\n', ', ')
WHERE `OPCIONES_PARA_ARMAR_TU_ALIMENTO` LIKE '%\r\n%';

UPDATE `Productos` 
SET `ingredientes` = REPLACE(`ingredientes`, '\r\n', ', ')
WHERE `ingredientes` LIKE '%\r\n%';


ALTER TABLE `Productos` 
DROP COLUMN `OPCIONES_PARA_ARMAR_TU_ALIMENTO`,
DROP COLUMN `ingredientes`;


UPDATE `productos` SET `id_producto` = '6' WHERE `productos`.`id_producto` = 15; 


UPDATE `productos` SET `id_producto` = '7' WHERE `productos`.`id_producto` = 16;
UPDATE `productos` SET `id_producto` = '8' WHERE `productos`.`id_producto` = 17;
UPDATE `productos` SET `id_producto` = '9' WHERE `productos`.`id_producto` = 18;
UPDATE `productos` SET `id_producto` = '10' WHERE `productos`.`id_producto` = 19;
UPDATE `productos` SET `id_producto` = '11' WHERE `productos`.`id_producto` = 20;
UPDATE `productos` SET `id_producto` = '12' WHERE `productos`.`id_producto` = 21;
UPDATE `productos` SET `id_producto` = '13' WHERE `productos`.`id_producto` = 22;
UPDATE `productos` SET `id_producto` = '14' WHERE `productos`.`id_producto` = 23;
UPDATE `productos` SET `id_producto` = '15' WHERE `productos`.`id_producto` = 24;
UPDATE `productos` SET `id_producto` = '16' WHERE `productos`.`id_producto` = 25;
UPDATE `productos` SET `id_producto` = '17' WHERE `productos`.`id_producto` = 26;
UPDATE `productos` SET `id_producto` = '18' WHERE `productos`.`id_producto` = 27;
UPDATE `productos` SET `id_producto` = '19' WHERE `productos`.`id_producto` = 28;
UPDATE `productos` SET `id_producto` = '20' WHERE `productos`.`id_producto` = 29;
UPDATE `productos` SET `id_producto` = '21' WHERE `productos`.`id_producto` = 30;
UPDATE `productos` SET `id_producto` = '22' WHERE `productos`.`id_producto` = 31;
UPDATE `productos` SET `id_producto` = '23' WHERE `productos`.`id_producto` = 32;
UPDATE `productos` SET `id_producto` = '24' WHERE `productos`.`id_producto` = 33;
UPDATE `productos` SET `id_producto` = '25' WHERE `productos`.`id_producto` = 34; 







--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Productos`
--
ALTER TABLE `Productos`
  ADD PRIMARY KEY (`id_producto`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `Productos`
--
ALTER TABLE `Productos`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
