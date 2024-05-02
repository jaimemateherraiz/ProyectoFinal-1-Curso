CREATE TABLE articulos_categorias (
    articulo_id INT(255),
    categoria_id INT(255),
    FOREIGN KEY (articulo_id) REFERENCES articulos_blog(identificador),
    FOREIGN KEY (categoria_id) REFERENCES categorias_articulos(identificador)
);
