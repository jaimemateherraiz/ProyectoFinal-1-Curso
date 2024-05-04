import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

# Configuración de customtkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

# Función para crear y mostrar la ventana de inicio de sesión
def iniciar_sesion():
    # Crear ventana de login
    ventana_login = ctk.CTk()
    ventana_login.geometry("500x350")
    ventana_login.title("Inicio de Sesión")

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

    # Función para verificar las credenciales
    def verificar_credenciales():
        nombre_usuario = entrada_usuario.get()
        contraseña = entrada_contraseña.get()

        # Verificar las credenciales
        if nombre_usuario == "admin" and contraseña == "admin":
            ventana_login.destroy()  # Cerrar la ventana de login
            crear_ventana_principal()  # Abrir la ventana principal
        else:
            ctk.messagebox.showerror("Error", "Credenciales incorrectas")

    # Botón para iniciar sesión
    boton_iniciar_sesion = ctk.CTkButton(ventana_login, text="Iniciar Sesión", command=verificar_credenciales)
    boton_iniciar_sesion.pack(pady=10)

    ventana_login.mainloop()

def crear_ventana_principal():
    
    # Crear ventana principal
    ventana_principal = ctk.CTk()
    ventana_principal.geometry("1000x600")
    ventana_principal.title("Ventana Principal")

    # Permitir que la ventana sea extensible al maximizar
    ventana_principal.resizable(True, True)

    # Crear el panel principal que ocupará toda la ventana
    panel_principal = ctk.CTkFrame(ventana_principal)
    panel_principal.pack(fill="both", expand=True)

    # -----------------------Crear el panel para el encabezado (top)------------------
    panel_top = ctk.CTkFrame(panel_principal, height=60, border_width=2, fg_color="#F2F2F2")
    panel_top.pack(side="top", fill="x")

    # Cargar la imagen del logo
    ruta_logo_usuario = "static/img/usuario.png"  
    my_image = ctk.CTkImage(light_image=Image.open(ruta_logo_usuario), dark_image=Image.open(ruta_logo_usuario), size=(30, 30))
    # Widget para mostrar el logo
    label_logo = ctk.CTkLabel(panel_top, image=my_image, text="")
    label_logo.pack(side="right", pady=5, padx=5)
    
    #-----------------------Crear el panel para el menú (aside izquierdo)------------------
    panel_izquierdo = ctk.CTkFrame(panel_principal, width=200, border_width=2, fg_color="#F2F2F2")
    panel_izquierdo.pack(side="left", fill="y")

    #-----------------------Crear el panel para el panel derecho-----------------------
    panel_derecho = ctk.CTkFrame(panel_principal, border_width=2, fg_color="#F2F2F2")
    panel_derecho.pack(side="right", fill="both", expand=True)

    ventana_principal.mainloop()

# Punto de entrada para iniciar el proceso de inicio de sesión
iniciar_sesion()


