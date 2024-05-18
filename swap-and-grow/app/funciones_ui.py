import customtkinter as ctk
from PIL import Image, ImageTk
from login import iniciar_sesion
from supercontrolador_db import mostrar_supercontrolador


def crear_ventana_principal():
    # Crear ventana principal
    ventana_principal = ctk.CTk()
    ventana_principal.geometry("1400x600")
    ventana_principal.minsize(1200,600)
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
        iniciar_sesion(crear_ventana_principal) #Vuelve a la ventana del login
        print("Cerrando sesion..")
    
    button = ctk.CTkButton(panel_top, text="Cerrar sesión", command=cerrar_sesion)
    button.pack(side="right")
    
    
    #-----------------------Crear el panel para el menú (aside izquierdo)------------------
    panel_izquierdo = ctk.CTkFrame(panel_principal, width=200, border_width=2, fg_color="#5B5B5B")
    panel_izquierdo.pack(side="left", fill="y")

    titulo_menu = ctk.CTkLabel(panel_izquierdo, text="MENU", font=("Verdana", 22), text_color="white")
    titulo_menu.pack(side="top", pady=30, padx=60)


    #-----------------------Crear el panel para el panel derecho-----------------------
    panel_derecho = ctk.CTkFrame(panel_principal, border_width=2, fg_color="#F2F2F2")
    panel_derecho.pack(side="right", fill="both", expand=True)

    def mostrar_administracion():
        # Limpiar el panel derecho
        for widget in panel_derecho.winfo_children():
            widget.destroy()
        
        # Crear un nuevo frame para la administración
        frame_admin = ctk.CTkFrame(panel_derecho, border_width=2, fg_color="#FFFFFF")
        frame_admin.pack(fill="both", expand=True, padx=10, pady=10)

        # Añadir contenido al frame de administración
        etiqueta_admin = ctk.CTkLabel(frame_admin, text="Panel de Administración para la BD", font=("Verdana", 22))
        etiqueta_admin.pack(pady=20)

        # Llamar a la función para mostrar el contenido del supercontrolador
        mostrar_supercontrolador(frame_admin, ventana_principal)

    def mostrar_ajustes():
        # Limpiar el panel derecho
        for widget in panel_derecho.winfo_children():
            widget.destroy()
        
        # Crear un nuevo frame para ajustes
        frame_ajustes = ctk.CTkFrame(panel_derecho, border_width=2, fg_color="#FFFFFF")
        frame_ajustes.pack(fill="both", expand=True, padx=10, pady=10)

        # Añadir contenido al frame de ajustes
        etiqueta_ajustes = ctk.CTkLabel(frame_ajustes, text="Panel de Ajustes", font=("Verdana", 22))
        etiqueta_ajustes.pack(pady=20)

    def mostrar_opcion3():
        # Limpiar el panel derecho
        for widget in panel_derecho.winfo_children():
            widget.destroy()
        
        # Crear un nuevo frame para opción 3
        frame_opcion3 = ctk.CTkFrame(panel_derecho, border_width=2, fg_color="#FFFFFF")
        frame_opcion3.pack(fill="both", expand=True, padx=10, pady=10)

        # Añadir contenido al frame de opción 3
        etiqueta_opcion3 = ctk.CTkLabel(frame_opcion3, text="Panel Opción 3", font=("Verdana", 22))
        etiqueta_opcion3.pack(pady=20)

    # Añadir botones u opciones al panel izquierdo
    opciones_menu = {
        "Administración": mostrar_administracion,
        "Ajustes": mostrar_ajustes,
        "Opción 3": mostrar_opcion3
    }

    for opcion, comando in opciones_menu.items():
        ctk.CTkButton(panel_izquierdo, text=opcion, command=lambda cmd=comando, op=opcion: (print(f"Seleccionaste {op}"), cmd())).pack(pady=10)

    ventana_principal.mainloop()
