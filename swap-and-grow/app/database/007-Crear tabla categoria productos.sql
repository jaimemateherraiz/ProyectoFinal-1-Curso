CREATE TABLE categorias_productos (
    identificador INT(255) AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    productos_id INT(255),
    FOREIGN KEY (productos_id) REFERENCES productos(identificador)
);
