import customtkinter as ctk
from tkinter import ttk
import mysql.connector

def mostrar_supercontrolador(frame_admin, ventana_principal):
    # Variables globales para almacenar información sobre la tabla y el registro seleccionado
    listacampos = []
    tablaactual = 0
    identificador_seleccionado = 0

    # Variables de conexión a la base de datos
    varservidor = "localhost"
    varbasededatos = "swap_and_grow"
    varusuario = "root"
    varcontraseña = ""
    primeratabla = ""

    # Función para eliminar un registro seleccionado
    def eliminaRegistro():
        nonlocal identificador_seleccionado, tablaactual
        print("Voy a eliminar el registro que está seleccionado")
        print("La tabla seleccionada es: " + tablaactual)
        print("El identificador seleccionado es: " + str(identificador_seleccionado))
        peticion = f"DELETE FROM {tablaactual} WHERE Identificador = {identificador_seleccionado};"
        print(peticion)
        cursor.execute(peticion)
        conexion.commit()
        seleccionaTabla(tablaactual)

    # Función para manejar clics en el árbol (Treeview)
    def clickEnArbol(event):
        nonlocal identificador_seleccionado
        print("Has hecho click en el arbol")
        elemento = arbol.identify('item', event.x, event.y)
        arbol.selection_set(elemento)
        print(elemento)
        valores = arbol.item(elemento, 'values')
        print(valores)
        identificador_seleccionado = valores[0]

    # Función para insertar registros en la base de datos
    def insertaBaseDatos():
        nonlocal tablaactual
        print("Insertamos en la base de datos")
        print(listacampos)
        peticion = "INSERT INTO " + tablaactual + " VALUES (NULL,"
        
        for campo in range(0, len(listacampos)):
            if campo != 0:
                peticion += "'" + listacampos[campo].get() + "',"
        peticion = peticion[:-1]
        peticion += ")"
        print(peticion)
        cursor.execute(peticion)
        conexion.commit()
        seleccionaTabla(tablaactual)

    # Función para mostrar los campos de una tabla seleccionada y los registros en el Treeview
    def seleccionaTabla(mitabla):
        nonlocal listacampos, tablaactual
        tablaactual = mitabla
        print("Has pulsado la tabla de: " + mitabla)
        for widget in contieneformulario.winfo_children():
            widget.destroy()
        cursor.execute("SHOW COLUMNS IN " + mitabla)
        columnas = cursor.fetchall()
        listacampos = []
        for columna in columnas:  
            ctk.CTkLabel(contieneformulario, text=columna[0]).pack(padx=5, pady=5)
            listacampos.append(ctk.CTkEntry(contieneformulario))
            listacampos[-1].pack(padx=5, pady=5)
        ctk.CTkButton(contieneformulario, text="Insertar", command=insertaBaseDatos).pack(padx=5, pady=5)
        # Vacío el arbol
        for elemento in arbol.get_children():
            arbol.delete(elemento)
        for columna in arbol['columns']:
            arbol.column(columna, width=0)
            arbol.heading(columna, text='')
        # ahora relleno el arbol con los datos que tocan
        cursor.execute("SHOW COLUMNS IN " + mitabla)
        columnas = cursor.fetchall()
        listadocolumnas = []
        for columna in columnas:
            listadocolumnas.append(columna[0])
        listadocolumnas = tuple(listadocolumnas)
        print(listadocolumnas)
        arbol['columns'] = listadocolumnas
        print("---------------------")
        print(arbol['columns'][0])
        for unacolumna in listadocolumnas:
            arbol.heading(unacolumna, text=unacolumna)
            arbol.column(unacolumna, width=50)
        cursor.execute("SELECT * FROM " + mitabla)
        registros = cursor.fetchall()
        for registro in registros:
            arbol.insert('', 'end', values=registro)

    # Conexión a la base de datos MySQL    
    conexion = mysql.connector.connect(
        host=varservidor,
        user=varusuario,
        password=varcontraseña,
        database=varbasededatos
    )
    cursor = conexion.cursor()

    # Creación de los contenedores y widgets necesarios
    contienetablas = ctk.CTkFrame(frame_admin)
    contienetablas.pack(side="left", fill="both", expand=True, padx=5, pady=5)
    ctk.CTkLabel(contienetablas, text="Tablas en la BBDD", font=("Arial", 16)).pack(pady=10)

    # Obtener las tablas de la base de datos y crear botones para seleccionarlas
    cursor.execute("SHOW TABLES IN " + varbasededatos)
    tablas = cursor.fetchall()
    contador = 0
    for tabla in tablas:
        if contador == 0:
            primeratabla = tabla[0]
            contador += 1
        ctk.CTkButton(contienetablas, text=tabla[0], width=10, command=lambda tabla=tabla[0]: seleccionaTabla(tabla)).pack(padx=10, pady=10)

    # Creación del contenedor para el formulario de inserción
    contieneformulario = ctk.CTkFrame(frame_admin)
    contieneformulario.pack(side="left", fill="both", expand=True, padx=5, pady=5)
    ctk.CTkLabel(contieneformulario, text="Formulario de inserción", font=("Arial", 16)).pack(pady=10)

    # Mostrar los campos del formulario según la tabla seleccionada
    cursor.execute("SHOW COLUMNS IN " + primeratabla)
    columnas = cursor.fetchall()
    for columna in columnas:  
        ctk.CTkLabel(contieneformulario, text=columna[0]).pack(padx=5, pady=5)
        ctk.CTkEntry(contieneformulario).pack(padx=5, pady=5)

    # Creación del contenedor para los datos mostrados en Treeview
    contienedatos = ctk.CTkFrame(frame_admin)
    contienedatos.pack(side="left", fill="both", expand=True, padx=5, pady=5)
    ctk.CTkLabel(contienedatos, text="Datos en mi sistema", font=("Arial", 16)).pack(pady=10)

    #Configuración del Treeview para mostrar los datos
    arbol = ttk.Treeview(contienedatos)
    arbol['columns'] = ("nombre", "apellidos",)
    arbol.pack(padx=5, pady=5, fill="both", expand=True)
    arbol.heading("#0", text="Columna 0")
    arbol.heading("nombre", text="Nombre")
    arbol.heading("apellidos", text="Apellidos")
    arbol.column("#0", width=10, stretch=False)
    arbol.column("nombre", width=100)
    arbol.column("apellidos", width=100)

    # Vincular la función clickEnArbol al evento clic del Treeview
    arbol.bind('<Button-1>', clickEnArbol)

    # Creación del botón para eliminar el registro seleccionado
    ctk.CTkButton(contienedatos, text="Elimina el registro seleccionado", command=eliminaRegistro).pack(padx=5, pady=5)

    # Ejecutar el bucle principal de la aplicación
    ventana_principal.mainloop()
