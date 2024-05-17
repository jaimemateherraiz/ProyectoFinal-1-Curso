import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from login import iniciar_sesion
from funciones_ui import crear_ventana_principal

# Configuración de customtkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

# Punto de entrada para iniciar el proceso de inicio de sesión
iniciar_sesion(crear_ventana_principal)
