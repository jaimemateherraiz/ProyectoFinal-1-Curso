CREATE TABLE swaps (
    identificador INT(255) AUTO_INCREMENT PRIMARY KEY,
    tipo ENUM('venta', 'donacion', 'intercambio'),
    producto_id INT(255),
    comprador_id INT(255) NULL,
    vendedor_id INT(255) NULL,
    donante_id INT(255) NULL,
    receptor_id INT(255) NULL,
    precio DECIMAL(10, 2) NULL, 
    cantidad INT(255),
    fecha_swap TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (producto_id) REFERENCES productos(identificador),
    FOREIGN KEY (comprador_id) REFERENCES usuarios(identificador),
    FOREIGN KEY (vendedor_id) REFERENCES usuarios(identificador),
    FOREIGN KEY (donante_id) REFERENCES usuarios(identificador),
    FOREIGN KEY (receptor_id) REFERENCES usuarios(identificador)
);
