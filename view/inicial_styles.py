import tkinter as tk

class StyledEntry(tk.Entry):
    """Entry personalizado con estilos mejorados"""
    def __init__(self, parent, placeholder="", **kwargs):
        # Configuración por defecto
        default_config = {
            'font': ('Arial', 12),
            'bg': '#ffffff',
            'fg': '#2c3e50',
            'relief': 'solid',
            'bd': 1,
            'highlightthickness': 2,
            'highlightcolor': '#3498db',
            'highlightbackground': '#bdc3c7'
        }
        
        # Combinar configuración por defecto con kwargs
        for key, value in default_config.items():
            if key not in kwargs:
                kwargs[key] = value
        
        super().__init__(parent, **kwargs)
        
        self.placeholder = placeholder
        self.placeholder_color = '#95a5a6'
        self.normal_color = kwargs.get('fg', '#2c3e50')
        
        # Configurar placeholder
        if placeholder:
            self.insert(0, placeholder)
            self.config(fg=self.placeholder_color)
            
        # Eventos para placeholder y efectos hover
        self.bind('<FocusIn>', self.on_focus_in)
        self.bind('<FocusOut>', self.on_focus_out)
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
        
    def on_focus_in(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg=self.normal_color)
        # Efecto de focus
        self.config(highlightbackground='#3498db', bg='#f8f9fa')
        
    def on_focus_out(self, event):
        if not self.get():
            self.insert(0, self.placeholder)
            self.config(fg=self.placeholder_color)
        # Remover efecto de focus
        self.config(highlightbackground='#bdc3c7', bg='#ffffff')
        
    def on_enter(self, event):
        if not self.focus_get() == self:
            self.config(bg='#f8f9fa')
            
    def on_leave(self, event):
        if not self.focus_get() == self:
            self.config(bg='#ffffff')
    
    def get_real_value(self):
        """Obtiene el valor real sin el placeholder"""
        value = self.get()
        return "" if value == self.placeholder else value

class StyledButton(tk.Button):
    """Botón personalizado con estilos mejorados"""
    def __init__(self, parent, **kwargs):
        # Configuración por defecto
        default_config = {
            'font': ('Arial', 12, 'bold'),
            'bg': '#3498db',
            'fg': 'white',
            'relief': 'flat',
            'bd': 0,
            'cursor': 'hand2',
            'activebackground': '#2980b9',
            'activeforeground': 'white'
        }
        
        # Combinar configuración por defecto con kwargs
        for key, value in default_config.items():
            if key not in kwargs:
                kwargs[key] = value
                
        super().__init__(parent, **kwargs)
        
        # Guardar colores originales
        self.original_bg = kwargs.get('bg', '#3498db')
        self.hover_bg = '#2980b9'
        self.pressed_bg = '#21618c'
        
        # Eventos para efectos hover y click
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
        self.bind('<Button-1>', self.on_click)
        self.bind('<ButtonRelease-1>', self.on_release)
        
    def on_enter(self, event):
        self.config(bg=self.hover_bg)
        
    def on_leave(self, event):
        self.config(bg=self.original_bg)
        
    def on_click(self, event):
        self.config(bg=self.pressed_bg)
        
    def on_release(self, event):
        self.config(bg=self.hover_bg)