import tkinter as tk
from tkinter import ttk
from view.category_frame import CategoryFrame

class Dashboard(tk.Tk):
    def __init__(self, login, user):
        super().__init__()
        self.title("SANA")
        self.geometry("900x650")
        self.configure(bg="#2c3e50")
        
        self.login_window = login
        self.current_user = user

        # Configurar estilos
        self.configure_styles()
        
        # Variables
        self.visible_menu = True
        self.active_boton = None
        
        # Centrar ventana
        self.center_window()
        self.create_interface()

    def configure_styles(self):
        style = ttk.Style()
        
        # Estilo para botones del menú
        style.configure("Menu.TButton",
                       background="#34495e",
                       foreground="white",
                       borderwidth=0,
                       focuscolor="none",
                       font=("Arial", 10))
        
        style.map("Menu.TButton",
                 background=[("active", "#3498db"),
                           ("pressed", "#2980b9")])
        
        # Estilo para botón activo
        style.configure("MenuActive.TButton",
                       background="#3498db",
                       foreground="white",
                       borderwidth=0,
                       focuscolor="none",
                       font=("Arial", 10, "bold"))
    
    def center_window(self):
        """Centrar la ventana en la pantalla"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{900}x{650}+{x}+{y}')

    def create_interface(self):
        # Frame principal
        self.main_frame = tk.Frame(self, bg="#2c3e50")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Frame del menú lateral
        self.menu_frame = tk.Frame(self.main_frame, bg="#34495e", width=250)
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.menu_frame.pack_propagate(False)
        
        # Frame del contenido
        self.content_frame = tk.Frame(self.main_frame, bg="#ecf0f1")
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Botón para mostrar/ocultar menú
        self.toggle_btn = tk.Button(self.content_frame, text="☰", 
                                   command=self.toggle_menu,
                                   bg="#3498db", fg="white", 
                                   font=("Arial", 16), bd=0,
                                   width=3, height=1)
        self.toggle_btn.pack(anchor="nw", padx=10, pady=10)
        
        self.create_menu()
        self.create_content()
    
    def create_menu(self):
        # Header del menú
        header_frame = tk.Frame(self.menu_frame, bg="#2c3e50", height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text="SANA", 
                              bg="#2c3e50", fg="white",
                              font=("Arial", 16, "bold"))
        title_label.pack(expand=True)
        
        # Separador
        separator = tk.Frame(self.menu_frame, bg="#2c3e50", height=2)
        separator.pack(fill=tk.X, pady=5)
        
        # Botones del menú con iconos (usando caracteres Unicode)
        self.menu_items = [
            ("🏠 Inicio", self.show_home),
            ("📊 Categorías", self.show_category),
            ("📝 Transacciones", self.show_profile),
            ("👤 Perfil", self.show_profile),
            ("⚙️ Configuración", self.show_configuration),
            ("❓ Ayuda", self.show_help),
            ("🚪 Salir", self.exit)
        ]
        
        self.buttons = []
        for i, (text, command) in enumerate(self.menu_items):
            btn = tk.Button(self.menu_frame, text=text, 
                           command=lambda cmd=command, idx=i: self.execute_command(cmd, idx),
                           bg="#34495e", fg="white", 
                           font=("Arial", 11), bd=0,
                           anchor="w", padx=20, pady=15)
            btn.pack(fill=tk.X, pady=2)
            
            # Efectos hover
            btn.bind("<Enter>", lambda e, b=btn: self.on_hover(b))
            btn.bind("<Leave>", lambda e, b=btn: self.on_leave(b))
            
            self.buttons.append(btn)
        
        # Activar el primer botón por defecto
        self.set_active_button(0)
    
    def execute_command(self, command, index):
        self.set_active_button(index)
        command()
    
    def set_active_button(self, index):
        # Resetear todos los botones
        for btn in self.buttons:
            btn.configure(bg="#34495e", fg="white")
        
        # Activar el botón seleccionado
        if 0 <= index < len(self.buttons):
            self.buttons[index].configure(bg="#3498db", fg="white")
            self.active_boton = index
    
    def on_hover(self, button):
        if button != self.buttons[self.active_boton]:
            button.configure(bg="#3498db")
    
    def on_leave(self, button):
        if button != self.buttons[self.active_boton]:
            button.configure(bg="#34495e")
    
    def toggle_menu(self):
        if self.visible_menu:
            self.menu_frame.pack_forget()
            self.toggle_btn.configure(text="☰")
        else:
            self.menu_frame.pack(side=tk.LEFT, fill=tk.Y, before=self.content_frame)
            self.toggle_btn.configure(text="✖")
        
        self.visible_menu = not self.visible_menu
    
    def create_content(self):
        self.content_container = tk.Frame(self.content_frame, bg="#ecf0f1")
        self.content_container.pack(fill=tk.BOTH, expand=True)
        
        welcome_label = tk.Label(self.content_container, 
                               text="Bienvenido a SANA",
                               bg="#ecf0f1", font=("Arial", 18, "bold"))
        welcome_label.pack(pady=20)
    
    def clear_content(self):
        for widget in self.content_container.winfo_children():
            widget.destroy()
    
    def show_home(self):
        self.clear_content()
        tk.Label(self.content_container, text="🏠 PÁGINA DE INICIO", 
                bg="#ecf0f1", font=("Arial", 20, "bold")).pack(pady=20)
        tk.Label(self.content_container, text="Esta es la página principal de la aplicación",
                bg="#ecf0f1", font=("Arial", 12)).pack()
    
    def show_category(self):
        self.clear_content()
        category = CategoryFrame(self.content_container, self.current_user[0])
        category.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
    def show_profile(self):
        self.clear_content()
        tk.Label(self.content_container, text="👤 PERFIL DE USUARIO", 
                bg="#ecf0f1", font=("Arial", 20, "bold")).pack(pady=20)
        
        # Formulario de ejemplo
        form_frame = tk.Frame(self.content_container, bg="#ecf0f1")
        form_frame.pack(pady=20)
        
        tk.Label(form_frame, text="Nombre:", bg="#ecf0f1").grid(row=0, column=0, sticky="w", pady=5)
        tk.Entry(form_frame, width=30).grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(form_frame, text="Email:", bg="#ecf0f1").grid(row=1, column=0, sticky="w", pady=5)
        tk.Entry(form_frame, width=30).grid(row=1, column=1, padx=10, pady=5)
    
    def show_configuration(self):
        self.clear_content()
        tk.Label(self.content_container, text="⚙️ CONFIGURACIÓN", 
                bg="#ecf0f1", font=("Arial", 20, "bold")).pack(pady=20)
        
        # Opciones de configuración
        config_frame = tk.Frame(self.content_container, bg="#ecf0f1")
        config_frame.pack(pady=20)
        
        tk.Checkbutton(config_frame, text="Notificaciones", bg="#ecf0f1").pack(anchor="w", pady=5)
        tk.Checkbutton(config_frame, text="Modo oscuro", bg="#ecf0f1").pack(anchor="w", pady=5)
        tk.Checkbutton(config_frame, text="Actualizaciones automáticas", bg="#ecf0f1").pack(anchor="w", pady=5)
    
    def show_contact(self):
        self.clear_content()
        tk.Label(self.content_container, text="📞 CONTACTO", 
                bg="#ecf0f1", font=("Arial", 20, "bold")).pack(pady=20)
        tk.Label(self.content_container, text="Email: contacto@miapp.com\nTeléfono: +1 234 567 890",
                bg="#ecf0f1", font=("Arial", 12)).pack()
    
    def show_help(self):
        self.clear_content()
        tk.Label(self.content_container, text="❓ AYUDA", 
                bg="#ecf0f1", font=("Arial", 20, "bold")).pack(pady=20)
        tk.Label(self.content_container, text="Documentación y soporte técnico",
                bg="#ecf0f1", font=("Arial", 12)).pack()
    
    def exit(self):
        if self.login_window:
            self.withdraw()
            self.login_window.deiconify()