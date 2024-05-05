import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from conexion_db import DatabaseConnection

# Configuración de customtkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

# Función para crear y mostrar la ventana de inicio de sesión
def iniciar_sesion():
    # Crear ventana de login
    ventana_login = ctk.CTk()
    ventana_login.geometry("500x350")
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
    ventana_principal.title("SWAP & GROW")

    # Permitir que la ventana sea extensible al maximizar
    ventana_principal.resizable(True, True)

    # Crear el panel principal que ocupará toda la ventana
    panel_principal = ctk.CTkFrame(ventana_principal)
    panel_principal.pack(fill="both", expand=True)

    # -----------------------Crear el panel para el encabezado (top)------------------
    panel_top = ctk.CTkFrame(panel_principal, height=100, border_width=2, fg_color="#E0F2D2")
    panel_top.pack(side="top", fill="x")

    # Cargar la imagen del logo
    ruta_logo_usuario = "static/img/usuario.png"  
    my_image = ctk.CTkImage(light_image=Image.open(ruta_logo_usuario), dark_image=Image.open(ruta_logo_usuario), size=(30, 30))
    # Widget para mostrar el logo
    label_logo = ctk.CTkLabel(panel_top, image=my_image, text="")
    label_logo.pack(side="right", pady=5, padx=5)

    def cerrar_sesion():
        ventana_principal.destroy()  # Cierra la ventana principal de Tkinter
        iniciar_sesion() #Vuelve a la ventana del login

    button = ctk.CTkButton(panel_top, text="Cerrar sesión", command=cerrar_sesion)
    button.pack(side="right")
    
    #-----------------------Crear el panel para el menú (aside izquierdo)------------------
    panel_izquierdo = ctk.CTkFrame(panel_principal, width=200, border_width=2, fg_color="#5B5B5B")
    panel_izquierdo.pack(side="left", fill="y")

    titulo_menu = ctk.CTkLabel(panel_izquierdo, text="MENU", font=("Verdana", 22), text_color="white")
    titulo_menu.pack(side="top", pady=30, padx=60)

    button_m1 = ctk.CTkButton(panel_izquierdo, width=180, height=120, fg_color="transparent", corner_radius=0, text="SUPERCONTROLADOR", command="none", hover_color="#BCBCBC")
    button_m1.pack(side="top")
    button_m2 = ctk.CTkButton(panel_izquierdo, width=180, height=120, fg_color="transparent", corner_radius=0, text="...", command="none", hover_color="#BCBCBC")
    button_m2.pack(side="top")
    button_m3 = ctk.CTkButton(panel_izquierdo, width=180, height=120, fg_color="transparent", corner_radius=0, text="...", command="none", hover_color="#BCBCBC")
    button_m3.pack(side="top", pady=5, padx=5)
    button_m4 = ctk.CTkButton(panel_izquierdo, width=180, height=120, fg_color="transparent", corner_radius=0, text="...", command="none", hover_color="#BCBCBC")
    button_m4.pack(side="top")

    
    #-----------------------Crear el panel para el panel derecho-----------------------
    panel_derecho = ctk.CTkFrame(panel_principal, border_width=2, fg_color="#F2F2F2")
    panel_derecho.pack(side="right", fill="both", expand=True)

        

    ventana_principal.mainloop()


# Punto de entrada para iniciar el proceso de inicio de sesión
iniciar_sesion()


