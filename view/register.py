import tkinter as tk
from tkinter import messagebox
from view.style import StyledButton, StyledEntry
from controller.user_controller import UserController

class Register(tk.Tk):
    def __init__(self, login):
        super().__init__()
        self.title("SANA")
        self.geometry("400x600")
        self.configure(bg="#ecf0f1")
        self.resizable(False, False)

        self.login_window = login
        
        # Centrar ventana
        self.center_window()
        self.create_interface()
    
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
        title_label = tk.Label(self.head_frame, text="Registro", 
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
                                         placeholder="Ingrese un usuario",
                                         width=35)
        self.username_entry.grid(row=1, column=0, sticky="ew", pady=(0, 20))
        
        # Campo Contraseña
        pass_label = tk.Label(self.content_frame, text="Contraseña:", 
                             bg="#ecf0f1", fg="#2c3e50", 
                             font=("Arial", 12, "bold"))
        pass_label.grid(row=2, column=0, sticky="w", pady=(0, 5))
        
        self.password_entry = StyledEntry(self.content_frame, 
                                         placeholder="Ingrese una contraseña",
                                         width=35)
        # Configurar como campo de contraseña después de la creación
        self.password_entry.config(show="*")
        self.password_entry.grid(row=3, column=0, sticky="ew", pady=(0, 30))
        
        # Botón de inicio de sesión mejorado
        self.login_button = StyledButton(self.content_frame, 
                                        text="Registrarse",
                                        command=self.register,
                                        height=2)
        self.login_button.grid(row=4, column=0, sticky="ew", pady=(0, 20))
        
        # Enlaces adicionales
        links_frame = tk.Frame(self.content_frame, bg="#ecf0f1")
        links_frame.grid(row=5, column=0, pady=(10, 0))
        
        # Agregar separador y opción de registro
        tk.Label(links_frame, text="─" * 30, 
                bg="#ecf0f1", fg="#bdc3c7").pack(pady=10)
        
        login_label = tk.Label(links_frame, text="¿Ya tienes cuenta? Inicia sesión", 
                                 bg="#ecf0f1", fg="#3498db", 
                                 font=("Arial", 10, "underline"),
                                 cursor="hand2")
        login_label.pack()
        
        # Eventos para los enlaces
        login_label.bind("<Button-1>", lambda e: self.login())
        
        # Efecto hover para enlaces
        def on_enter_link(event, label, color):
            label.config(fg=color)
        
        def on_leave_link(event, label, original_color):
            label.config(fg=original_color)
        
        login_label.bind("<Enter>", lambda e: on_enter_link(e, login_label, "#3498db"))
        login_label.bind("<Leave>", lambda e: on_leave_link(e, login_label, "#3498db"))
        
        # Permitir Enter para login
        self.bind('<Return>', lambda e: self.register())
    
    def register(self):
        """Función de inicio de sesión"""
        username = self.username_entry.get_real_value()
        password = self.password_entry.get_real_value()
        user_controller = UserController()
        if username and password:
            if user_controller.create_user(username, password):
                messagebox.showinfo("Éxito", "Usuario registrado exitosamente")
                if self.login_window:
                    self.withdraw()
                    self.login_window.deiconify()
            else:
                messagebox.showerror("Error", "No se pudo registrar el usuario")
        else:
            messagebox.showerror("Error", "Rellene todos los campos")

    def login(self):
        if self.login_window:
            self.withdraw()
            self.login_window.deiconify()