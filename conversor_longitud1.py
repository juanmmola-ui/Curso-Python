import tkinter as tk
from tkinter import messagebox

def convertir():
    try:
        valor = float(entrada.get())
        
        # Validación: Solo números positivos
        if valor < 0:
            messagebox.showerror("Error", "Por favor, ingresa solo números positivos.")
            return

        origen = unidad_origen.get()
        destino = unidad_destino.get()

        # Tabla de conversión a metros (base común)
        factores = {"Metros": 1.0, "Centímetros": 0.01, "Pulgadas": 0.0254, "Pies": 0.3048}
        
        # Lógica: convertir a metros primero, luego a la unidad destino
        valor_en_metros = valor * factores[origen]
        resultado = valor_en_metros / factores[destino]

        resultado_label.config(text=f"Resultado: {resultado:.4f} {destino}")
        
    except ValueError:
        messagebox.showerror("Error", "Ingresa un número válido.")

# Configuración ventana
ventana = tk.Tk()
ventana.title("Conversor Profesional")
ventana.geometry("300x350")

unidades = ["Metros", "Centímetros", "Pulgadas", "Pies"]

# Widgets
tk.Label(ventana, text="Valor a convertir:").pack(pady=5)
entrada = tk.Entry(ventana)
entrada.pack()

tk.Label(ventana, text="De:").pack(pady=5)
unidad_origen = tk.StringVar(ventana)
unidad_origen.set(unidades[0])
tk.OptionMenu(ventana, unidad_origen, *unidades).pack()

tk.Label(ventana, text="A:").pack(pady=5)
unidad_destino = tk.StringVar(ventana)
unidad_destino.set(unidades[1])
tk.OptionMenu(ventana, unidad_destino, *unidades).pack()

tk.Button(ventana, text="Convertir", command=convertir).pack(pady=20)
resultado_label = tk.Label(ventana, text="Resultado: ", font=("Arial", 12, "bold"))
resultado_label.pack()

ventana.mainloop()