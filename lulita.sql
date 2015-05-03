SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema BazarPapeleriaLulita
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `BazarPapeleriaLulita` DEFAULT CHARACTER SET latin1 ;
USE `BazarPapeleriaLulita` ;

-- -----------------------------------------------------
-- Table `BazarPapeleriaLulita`.`CUENTAS`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `CUENTAS`;
CREATE TABLE `CUENTAS`(
			idCuentas INT NOT NULL auto_increment,
			idUsuario VARCHAR(10) NOT NULL,
			idContrasena VARCHAR(10) NOT NULL,
			tipoCuenta INT(1) NOT NULL,
			CONSTRAINT idC PRIMARY KEY(IdCuentas,IdUsuario),
			UNIQUE (IdUsuario)
);

-- -----------------------------------------------------
-- Table `BazarPapeleriaLulita`.`PRODUCTO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `PRODUCTO`;
CREATE TABLE `PRODUCTO` (
	idProducto INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	descripcionProducto VARCHAR(100),
	precioUnitarioReal FLOAT,
	precioUnitarioIva FLOAT,
	stock_Inicial INT,
	stock_Actual INT
);
-- -----------------------------------------------------
-- Table `BazarPapeleriaLulita`.`CLIENTE`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `CLIENTE`;
CREATE TABLE `CLIENTE` (
	idCliente INT NOT NULL AUTO_INCREMENT,
	nombreApellido VARCHAR(100) NOT NULL,	
	direccion VARCHAR(50) NOT NULL,
	fechaDeNacimiento DATE,
	rucCedula VARCHAR(13) NOT NULL,
	telefono VARCHAR(10),
	CONSTRAINT idC PRIMARY KEY(idCliente,rucCedula)
);

-- -----------------------------------------------------
-- Table `BazarPapeleriaLulita`.`FACTURA`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FACTURA`;
CREATE TABLE `FACTURA` (
	idFactura INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	idCliente INT NOT NULL,
	fecha DATETIME NOT NULL,
	idCuentas INT NOT NULL,
	FOREIGN KEY (idCliente) REFERENCES CLIENTE (idCliente),
	FOREIGN KEY (idCuentas) REFERENCES CUENTAS (idCuentas)
);

-- -----------------------------------------------------
-- Table `BazarPapeleriaLulita`.`DETALLE`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `DETALLE`;
CREATE TABLE `DETALLE` (
	idDetalle INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	cantidadProducto INT,
	precioUnitario FLOAT,
	precioTotalProducto FLOAT,
	idProducto INT NOT NULL,
	idFactura INT NOT NULL,
	FOREIGN KEY(idProducto) REFERENCES PRODUCTO(idProducto),
	FOREIGN KEY(idFactura) REFERENCES FACTURA(idFactura)
);

