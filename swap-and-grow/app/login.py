import customtkinter as ctk
from PIL import Image, ImageTk


def iniciar_sesion(crear_ventana_principal):
    # Crear ventana de login
    ventana_login = ctk.CTk()
    ventana_login.geometry("500x350")
    ventana_login.maxsize(500,350)
    ventana_login.minsize(500,350)
    ventana_login.title("Login")

    # Cargar la imagen del logo
    ruta_logo = "static/img/logo_swap.png"  
    my_image = ctk.CTkImage(light_image=Image.open(ruta_logo), dark_image=Image.open(ruta_logo), size=(100, 100))
    # Widget para mostrar el logo
    label_logo = ctk.CTkLabel(ventana_login, image=my_image, text="")
    label_logo.pack(pady=10)

    # Elementos de la ventana de login
    etiqueta_usuario = ctk.CTkLabel(ventana_login, text="Usuario:")
    etiqueta_usuario.pack(pady=5)
    entrada_usuario = ctk.CTkEntry(ventana_login)
    entrada_usuario.pack(pady=5)
    etiqueta_contraseña = ctk.CTkLabel(ventana_login, text="Contraseña:")
    etiqueta_contraseña.pack(pady=5)
    entrada_contraseña = ctk.CTkEntry(ventana_login, show="*")
    entrada_contraseña.pack(pady=5)

    def verificar_credenciales(nombre_usuario, contraseña):
    # Verificar las credenciales
        if nombre_usuario == "admin" and contraseña == "admin":
            ventana_login.destroy()  # Cerrar la ventana de login
            crear_ventana_principal()  # Abrir la ventana principal
        else:
            ctk.messagebox.showerror("Error", "Credenciales incorrectas")

    def handle_login():
        nombre_usuario = entrada_usuario.get()
        contraseña = entrada_contraseña.get()
        verificar_credenciales(nombre_usuario, contraseña)

    # Botón para iniciar sesión
    boton_iniciar_sesion = ctk.CTkButton(ventana_login, text="Iniciar Sesión", command=handle_login)
    boton_iniciar_sesion.pack(pady=10)

    ventana_login.mainloop()
