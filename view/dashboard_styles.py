import tkinter as tk

class StyledEntry(tk.Entry):
    """Entry personalizado con estilos mejorados"""
    def __init__(self, parent, placeholder="", **kwargs):
        default_config = {
            'font': ('Arial', 11),
            'bg': '#ffffff',
            'fg': '#2c3e50',
            'relief': 'solid',
            'bd': 1,
            'highlightthickness': 2,
            'highlightcolor': '#3498db',
            'highlightbackground': '#bdc3c7'
        }
        
        for key, value in default_config.items():
            if key not in kwargs:
                kwargs[key] = value
        
        super().__init__(parent, **kwargs)
        
        self.placeholder = placeholder
        self.placeholder_color = '#95a5a6'
        self.normal_color = kwargs.get('fg', '#2c3e50')
        
        if placeholder:
            self.insert(0, placeholder)
            self.config(fg=self.placeholder_color)
            
        self.bind('<FocusIn>', self.on_focus_in)
        self.bind('<FocusOut>', self.on_focus_out)
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
        
    def on_focus_in(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg=self.normal_color)
        self.config(highlightbackground='#3498db', bg='#f8f9fa')
        
    def on_focus_out(self, event):
        if not self.get():
            self.insert(0, self.placeholder)
            self.config(fg=self.placeholder_color)
        self.config(highlightbackground='#bdc3c7', bg='#ffffff')
        
    def on_enter(self, event):
        if not self.focus_get() == self:
            self.config(bg='#f8f9fa')
            
    def on_leave(self, event):
        if not self.focus_get() == self:
            self.config(bg='#ffffff')
    
    def get_real_value(self):
        value = self.get()
        return "" if value == self.placeholder else value

class StyledButton(tk.Button):
    """Botón personalizado con estilos mejorados"""
    def __init__(self, parent, style_type="primary", **kwargs):
        # Estilos predefinidos
        styles = {
            "primary": {"bg": "#3498db", "hover": "#2980b9", "pressed": "#21618c"},
            "success": {"bg": "#27ae60", "hover": "#229954", "pressed": "#1e8449"},
            "danger": {"bg": "#e74c3c", "hover": "#c0392b", "pressed": "#a93226"},
            "warning": {"bg": "#f39c12", "hover": "#e67e22", "pressed": "#d35400"},
            "secondary": {"bg": "#95a5a6", "hover": "#7f8c8d", "pressed": "#6c7b7d"}
        }
        
        colors = styles.get(style_type, styles["primary"])
        
        default_config = {
            'font': ('Arial', 10, 'bold'),
            'bg': colors["bg"],
            'fg': 'white',
            'relief': 'flat',
            'bd': 0,
            'cursor': 'hand2',
            'activebackground': colors["hover"],
            'activeforeground': 'white'
        }
        
        for key, value in default_config.items():
            if key not in kwargs:
                kwargs[key] = value
                
        super().__init__(parent, **kwargs)
        
        self.original_bg = colors["bg"]
        self.hover_bg = colors["hover"]
        self.pressed_bg = colors["pressed"]
        
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