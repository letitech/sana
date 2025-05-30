import tkinter as tk
from tkinter import ttk, messagebox
from view.dashboard_styles import StyledButton, StyledEntry
from controller.category_controller import CategoryController

class CategoryFrame(tk.Frame):
    """Frame principal para operaciones CRUD"""
    def __init__(self, parent, user_id):
        super().__init__(parent, bg="#ecf0f1")
        self.db = CategoryController()
        self.selected_category_id = None
        self.current_user_id = user_id
        self.create_interface()
        self.load_data()
    
    def create_interface(self):
        """Crear la interfaz de usuario"""
        # Título principal
        title_frame = tk.Frame(self, bg="#ecf0f1")
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(title_frame, text="Gestión de Categorías", 
                bg="#ecf0f1", fg="#2c3e50", 
                font=("Arial", 18, "bold")).pack()
        
        # Frame de búsqueda
        self.create_search_section()
        
        # Frame de formulario
        self.create_form_section()
        
        # Frame de botones
        self.create_buttons_section()
        
        # Frame de TreeView
        self.create_treeview_section()
    
    def create_search_section(self):
        """Crear sección de búsqueda"""
        search_frame = tk.LabelFrame(self, text="Búsqueda", 
                                   bg="#ecf0f1", fg="#2c3e50",
                                   font=("Arial", 12, "bold"))
        search_frame.pack(fill=tk.X, padx=10, pady=(0, 15))
        
        search_container = tk.Frame(search_frame, bg="#ecf0f1")
        search_container.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(search_container, text="Buscar:", 
                bg="#ecf0f1", fg="#2c3e50", 
                font=("Arial", 11)).pack(side=tk.LEFT, padx=(0, 10))
        
        self.search_entry = StyledEntry(search_container, 
                                      placeholder="Nombre...",
                                      width=40)
        self.search_entry.pack(side=tk.LEFT, padx=(0, 10))
        self.search_entry.bind('<KeyRelease>', self.on_search)
        
        StyledButton(search_container, text="Buscar", 
                    command=self.search_categories,
                    style_type="primary").pack(side=tk.LEFT, padx=(0, 5))
        
        StyledButton(search_container, text="Limpiar", 
                    command=self.clear_search,
                    style_type="secondary").pack(side=tk.LEFT)
    
    def create_form_section(self):
        """Crear sección del formulario"""
        form_frame = tk.LabelFrame(self, text="Datos de la categoría", 
                                 bg="#ecf0f1", fg="#2c3e50",
                                 font=("Arial", 12, "bold"))
        form_frame.pack(fill=tk.X, padx=10, pady=(0, 15))
        
        form_container = tk.Frame(form_frame, bg="#ecf0f1")
        form_container.pack(fill=tk.X, padx=15, pady=15)
        
        # Campo Nombre
        tk.Label(form_container, text="Nombre:", 
                bg="#ecf0f1", fg="#2c3e50", 
                font=("Arial", 11, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        self.name_entry = StyledEntry(form_container, 
                                      placeholder="Ingrese el nombre de la categoría",
                                      width=30)
        self.name_entry.grid(row=1, column=0, sticky="ew", padx=(0, 10), pady=(0, 15))

        # Campo de selección (ID)
        tk.Label(form_container, text="ID Categoría:", 
                bg="#ecf0f1", fg="#2c3e50", 
                font=("Arial", 11, "bold")).grid(row=2, column=1, sticky="w", pady=(0, 5))
        
        self.id_var = tk.StringVar()
        self.id_combobox = ttk.Combobox(form_container, textvariable=self.id_var,
                                      width=27, state="readonly")
        self.id_combobox.grid(row=3, column=1, sticky="ew")
        self.id_combobox.bind('<<ComboboxSelected>>', self.on_category_select)
        
        # Configurar grid
        form_container.grid_columnconfigure(0, weight=1)
        form_container.grid_columnconfigure(1, weight=1)
    
    def create_buttons_section(self):
        """Crear sección de botones"""
        buttons_frame = tk.Frame(self, bg="#ecf0f1")
        buttons_frame.pack(fill=tk.X, padx=10, pady=(0, 15))
        
        # Botones principales
        StyledButton(buttons_frame, text="➕ Registrar", 
                    command=self.create_category,
                    style_type="success",
                    width=12).pack(side=tk.LEFT, padx=(0, 5))
        
        StyledButton(buttons_frame, text="📝 Actualizar", 
                    command=self.update_category,
                    style_type="warning",
                    width=12).pack(side=tk.LEFT, padx=(0, 5))
        
        StyledButton(buttons_frame, text="🗑️ Eliminar", 
                    command=self.delete_category,
                    style_type="danger",
                    width=12).pack(side=tk.LEFT, padx=(0, 5))
        
        StyledButton(buttons_frame, text="🔄 Actualizar Lista", 
                    command=self.refresh_data,
                    style_type="primary",
                    width=15).pack(side=tk.LEFT, padx=(0, 5))
        
        StyledButton(buttons_frame, text="🧹 Limpiar", 
                    command=self.clear_form,
                    style_type="secondary",
                    width=12).pack(side=tk.LEFT)
    
    def create_treeview_section(self):
        """Crear sección del TreeView"""
        tree_frame = tk.LabelFrame(self, text="Lista de categorías", 
                                 bg="#ecf0f1", fg="#2c3e50",
                                 font=("Arial", 12, "bold"))
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        # Crear TreeView con scrollbars
        tree_container = tk.Frame(tree_frame, bg="#ecf0f1")
        tree_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Configurar TreeView
        columns = ("ID", "Nombre")
        self.tree = ttk.Treeview(tree_container, columns=columns, show="headings", height=10)
        
        # Configurar columnas
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        
        # Ajustar ancho de columnas
        self.tree.column("ID", width=50, minwidth=50)
        self.tree.column("Nombre", width=150, minwidth=100)
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(tree_container, orient=tk.VERTICAL, command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(tree_container, orient=tk.HORIZONTAL, command=self.tree.xview)
        
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Pack TreeView y scrollbars
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Eventos del TreeView
        self.tree.bind('<ButtonRelease-1>', self.on_tree_select)
        self.tree.bind('<Double-1>', self.on_tree_double_click)
    
    def load_data(self):
        """Cargar datos en el TreeView"""
        # Limpiar TreeView
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Cargar usuarios
        categories = self.db.read_categories(self.current_user_id)
        for category in categories:           
            self.tree.insert("", tk.END, values=(category[0], category[1]))
        
        # Actualizar combobox de IDs
        self.update_id_combobox()
    
    def update_id_combobox(self):
        """Actualizar combobox de IDs"""
        categories = self.db.read_categories(self.current_user_id)
        ids = [f"{category[0]} - {category[1]}" for category in categories]
        self.id_combobox['values'] = ids
    
    def on_search(self, event):
        """Búsqueda en tiempo real"""
        search_term = self.search_entry.get_real_value()
        if len(search_term) >= 2:  # Buscar solo si hay al menos 2 caracteres
            self.search_categories()
        elif len(search_term) == 0:
            self.load_data()
    
    def search_categories(self):
        """Realizar búsqueda"""
        search_term = self.search_entry.get_real_value()
        if not search_term:
            self.load_data()
            return
        
        # Limpiar TreeView
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Buscar categorías
        categories = self.db.search_categories(search_term)
        if categories:
            for category in categories: 
                self.tree.insert("", tk.END, values=(category[0], category[1]))
    
    def clear_search(self):
        """Limpiar búsqueda"""
        self.search_entry.delete(0, tk.END)
        self.search_entry.insert(0, self.search_entry.placeholder)
        self.search_entry.config(fg=self.search_entry.placeholder_color)
        self.load_data()
    
    def on_tree_select(self, event):
        """Evento de selección en TreeView"""
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            values = item['values']
            
            # Llenar formulario con datos seleccionados
            self.clear_form()
            self.name_entry.insert(0, values[1])
            self.name_entry.config(fg=self.name_entry.normal_color)
            
            # Seleccionar en combobox
            category_text = f"{values[0]} - {values[1]}"
            self.id_var.set(category_text)
            self.selected_category_id = values[0]
    
    def on_tree_double_click(self, event):
        """Evento de doble clic en TreeView"""
        self.on_tree_select(event)
        messagebox.showinfo("Categoría Seleccionada", 
                          f"Categoría: {self.name_entry.get()}")
    
    def on_category_select(self, event):
        """Evento de selección en combobox"""
        selected = self.id_var.get()
        if selected:
            category_id = selected.split(" - ")[0]
            self.selected_category_id = category_id
            
            # Buscar categoría y llenar formulario
            categories = self.db.read_categories(self.current_user_id)
            for category in categories:
                if str(category[0]) == category_id:
                    self.clear_form()
                    self.name_entry.insert(0, category[1])
                    self.name_entry.config(fg=self.name_entry.normal_color)
                    
                    break
    
    def validate_form(self):
        """Validar formulario"""
        nombre = self.name_entry.get_real_value()
        
        if not nombre:
            messagebox.showerror("Error", "El nombre es obligatorio")
            return False
        
        return True
    
    def create_category(self):
        """Agregar category"""
        if not self.validate_form():
            return
        
        try:
            name = self.name_entry.get_real_value()
            
            self.db.create_category(name, self.current_user_id)
            messagebox.showinfo("Éxito", "Categoría registrada correctamente")
            self.clear_form()
            self.refresh_data()
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar categoría: {str(e)}")
    
    def update_category(self):
        """Actualizar categoría"""
        if not self.selected_category_id:
            messagebox.showerror("Error", "Seleccione una categoría para actualizar")
            return
        
        if not self.validate_form():
            return
        
        try:
            name = self.name_entry.get_real_value()
            
            self.db.update_category(name, self.selected_category_id)
            messagebox.showinfo("Éxito", "Categoría actualizada correctamente")
            self.clear_form()
            self.refresh_data()
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar categoría: {str(e)}")
    
    def delete_category(self):
        """Eliminar categoría"""
        if not self.selected_category_id:
            messagebox.showerror("Error", "Seleccione una categoría para eliminar")
            return
        
        name = self.name_entry.get_real_value()
        confirm = messagebox.askyesno("Confirmar", 
                                    f"¿Está seguro de eliminar la categoría '{name}'?")
        
        if confirm:
            try:
                self.db.delete_category(self.selected_category_id)
                messagebox.showinfo("Éxito", "Categoría eliminado correctamente")
                self.clear_form()
                self.refresh_data()
            except Exception as e:
                messagebox.showerror("Error", f"Error al eliminar categoría: {str(e)}")
    
    def clear_form(self):
        """Limpiar formulario"""
        # Limpiar entries
        entries = [self.name_entry]
        for entry in entries:
            entry.delete(0, tk.END)
            # entry.insert(0, entry.placeholder)
            entry.config(fg=entry.placeholder_color)
        
        # Limpiar combobox
        self.id_var.set("")
        self.selected_category_id = None
    
    def refresh_data(self):
        """Actualizar datos"""
        self.load_data()
        messagebox.showinfo("Actualizado", "Datos actualizados correctamente")