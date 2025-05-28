import tkinter as tk
from tkinter import messagebox
from view.style import StyledButton, StyledEntry
from view.register import Register
from view.dashboard import Dashboard
from controller.user_controller import UserController

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SANA")
        self.geometry("400x600")
        self.configure(bg="#ecf0f1")
        self.resizable(False, False)
        
        # Centrar ventana
        self.center_window()
        self.create_interface()

        # Ventanas
        self.dashboard_window = None
        self.register_window = None

    
    def center_window(self):
        """Centrar la ventana en la pantalla"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{400}x{600}+{x}+{y}')
    
    def create_interface(self):
        # Frame principal con padding
        self.main_frame = tk.Frame(self, bg="#ecf0f1")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Frame de cabecera
        self.head_frame = tk.Frame(self.main_frame, bg="#ecf0f1")
        self.head_frame.pack(fill=tk.X, pady=(0, 30))

        # Título con mejor diseño
        title_label = tk.Label(self.head_frame, text="Inicio de Sesión", 
                              bg="#ecf0f1", fg="#2c3e50", 
                              font=("Arial", 24, "bold"))
        title_label.pack(pady=(0, 10))
        
        # Icono de usuario más elegante
        icon_label = tk.Label(self.head_frame, text="👤", 
                             bg="#ecf0f1", font=("Arial", 60))
        icon_label.pack(pady=(0, 20))
        
        # Línea decorativa
        separator = tk.Frame(self.head_frame, height=2, bg="#bdc3c7")
        separator.pack(fill=tk.X, pady=(0, 20))
        
        # Frame del contenido con mejor estructura
        self.content_frame = tk.Frame(self.main_frame, bg="#ecf0f1")
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Configurar grid
        self.content_frame.grid_columnconfigure(0, weight=1)
        
        # Campo Usuario
        user_label = tk.Label(self.content_frame, text="Usuario:", 
                             bg="#ecf0f1", fg="#2c3e50", 
                             font=("Arial", 12, "bold"))
        user_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        self.username_entry = StyledEntry(self.content_frame, 
                                         placeholder="Ingrese su usuario",
                                         width=35)
        self.username_entry.grid(row=1, column=0, sticky="ew", pady=(0, 20))
        
        # Campo Contraseña
        pass_label = tk.Label(self.content_frame, text="Contraseña:", 
                             bg="#ecf0f1", fg="#2c3e50", 
                             font=("Arial", 12, "bold"))
        pass_label.grid(row=2, column=0, sticky="w", pady=(0, 5))
        
        self.password_entry = StyledEntry(self.content_frame, 
                                         placeholder="Ingrese su contraseña",
                                         width=35)
        # Configurar como campo de contraseña después de la creación
        self.password_entry.config(show="*")
        self.password_entry.grid(row=3, column=0, sticky="ew", pady=(0, 30))
        
        # Botón de inicio de sesión mejorado
        self.login_button = StyledButton(self.content_frame, 
                                        text="Iniciar Sesión",
                                        command=self.login,
                                        height=2)
        self.login_button.grid(row=4, column=0, sticky="ew", pady=(0, 20))
        
        # Enlaces adicionales
        links_frame = tk.Frame(self.content_frame, bg="#ecf0f1")
        links_frame.grid(row=5, column=0, pady=(10, 0))
        
        forgot_label = tk.Label(links_frame, text="¿Olvidaste tu contraseña?", 
                               bg="#ecf0f1", fg="#3498db", 
                               font=("Arial", 10, "underline"),
                               cursor="hand2")
        forgot_label.pack()
        
        # Agregar separador y opción de registro
        tk.Label(links_frame, text="─" * 30, 
                bg="#ecf0f1", fg="#bdc3c7").pack(pady=10)
        
        register_label = tk.Label(links_frame, text="¿No tienes cuenta? Regístrate aquí", 
                                 bg="#ecf0f1", fg="#3498db", 
                                 font=("Arial", 10, "underline"),
                                 cursor="hand2")
        register_label.pack()
        
        # Eventos para los enlaces
        forgot_label.bind("<Button-1>", lambda e: self.forgot_password())
        register_label.bind("<Button-1>", lambda e: self.register())
        
        # Efecto hover para enlaces
        def on_enter_link(event, label, color):
            label.config(fg=color)
        
        def on_leave_link(event, label, original_color):
            label.config(fg=original_color)
            
        forgot_label.bind("<Enter>", lambda e: on_enter_link(e, forgot_label, "#2980b9"))
        forgot_label.bind("<Leave>", lambda e: on_leave_link(e, forgot_label, "#3498db"))
        
        register_label.bind("<Enter>", lambda e: on_enter_link(e, register_label, "#3498db"))
        register_label.bind("<Leave>", lambda e: on_leave_link(e, register_label, "#3498db"))
        
        # Permitir Enter para login
        self.bind('<Return>', lambda e: self.login())
    
    def login(self):
        """Función de inicio de sesión"""
        username = self.username_entry.get_real_value()
        password = self.password_entry.get_real_value()
        user_controller = UserController()
        if username and password:
            if user_controller.login(username, password):
                messagebox.showinfo("Éxito", "Bienvenido")
                if self.dashboard_window == None:
                    self.withdraw()
                    self.dashboard_window = Dashboard(self)
                    self.dashboard_window.deiconify()
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrecto")
        else:
            messagebox.showerror("Error", "Rellene todos los campos")
    
    def forgot_password(self):
        """Función para recuperar contraseña"""
        self.show_message("Función de recuperación de contraseña", "info")
    
    def register(self):
        """Función para registro"""
        if self.register_window == None:
            self.withdraw()
            self.register_window = Register(self)
            self.register_window.deiconify()
    
    def show_message(self, message, msg_type="info"):
        """Mostrar mensaje temporal"""
        colors = {
            "success": "#27ae60",
            "error": "#e74c3c",
            "info": "#3498db"
        }
        
        # Crear label temporal para el mensaje
        msg_label = tk.Label(self.content_frame, text=message, 
                           bg="#ecf0f1", fg=colors.get(msg_type, "#3498db"),
                           font=("Arial", 10, "bold"))
        msg_label.grid(row=6, column=0, pady=10)
        
        # Eliminar mensaje después de 3 segundos
        self.after(3000, msg_label.destroy)