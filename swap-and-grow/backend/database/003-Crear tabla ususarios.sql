CREATE TABLE `swap_and_grow`.`usuarios` 
(`identificador` INT(255) NOT NULL AUTO_INCREMENT ,
 `nombre` VARCHAR(255) NOT NULL ,
    `apellidos` VARCHAR(255) NOT NULL ,
    `correo_electronico` VARCHAR(255) NOT NULL ,
    `contraseña` VARCHAR(255) NOT NULL ,
    `fecha_registro` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
     `telefono` VARCHAR(20) NOT NULL ,
    PRIMARY KEY (`identificador`)) 
ENGINE = InnoDB;