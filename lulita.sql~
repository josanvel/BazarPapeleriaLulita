SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';


-- -----------------------------------------------------
-- Schema BazarPapeleriaLulita
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `BazarPapeleriaLulita` DEFAULT CHARACTER SET latin1 ;
USE `BazarPapeleriaLulita` ;

-- -----------------------------------------------------
-- Table `BazarPapeleriaLulita`.`PRODUCTO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `PRODUCTO`;
CREATE TABLE `PRODUCTO` (
	idProducto int not null primary key auto_increment,
	descripcionProducto varchar(100),
	precioUnitarioReal float,
	precioUnitarioIva float,
	stock int
);

-- -----------------------------------------------------
-- Table `BazarPapeleriaLulita`.`CLIENTE`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `CLIENTE`;
CREATE TABLE `CLIENTE` (
	idCliente int not null primary key auto_increment,
	nombre varchar(50),
	apellido varchar(50),	
	direccion varchar(50),
	fechaDeNacimiento date,
	rucCedula int,
	telefono int
);

-- -----------------------------------------------------
-- Table `BazarPapeleriaLulita`.`FACTURA`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FACTURA`;
CREATE TABLE `FACTURA` (
	idFactura int not null primary key auto_increment,
	idCliente int not null,
	fecha date,
	foreign key(idCliente) references CLIENTE (idCliente)
);

-- -----------------------------------------------------
-- Table `BazarPapeleriaLulita`.`DETALLE`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `DETALLE`;
CREATE TABLE `DETALLE` (
	idDetalle int not null primary key auto_increment,
	cantidadProducto int,
	subTotal decimal,
	total float,
	idProducto int not null,
	foreign key(idProducto) references PRODUCTO(idProducto),
	idFactura int not null,
	foreign key(idFactura) references FACTURA(idFactura)
);
