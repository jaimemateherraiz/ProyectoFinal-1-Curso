CREATE TABLE `swap_and_grow`.`articulos_blog` (`identificador` INT(255) NOT NULL AUTO_INCREMENT , `titulo` VARCHAR(255) NOT NULL , `contenido` TEXT NOT NULL , `fecha_publicacion` TIMESTAMP NOT NULL , `autor_id` INT(255) NOT NULL , PRIMARY KEY (`identificador`)) ENGINE = InnoDB;

-- Creamos clave foránea
ALTER TABLE articulos_blog
ADD CONSTRAINT fk_autor_id
FOREIGN KEY (autor_id) REFERENCES usuarios(identificador);
