import tkinter as tk

# Opciones válidas para cada proyecto
opciones = {
    "T-Mobile": ["RadiosT", "AntenasT", "RadiosVT"],
    "Verizon": ["RadiosV"],
    "AT&T": ["AntenasA"],
    "Watch Com.": ["AntenasW", "AntenasWC"] 
}

def imprimir_materiales(equipos):
    # Obtener proyecto seleccionado
    proyecto = project.get() 

    # Inicializar el contador para cada equipo
    counters = {equipo: 1 for equipo in opciones.get(proyecto, [])}

    materials = []
    equipos = equipos.split(',')
    for equipo in equipos:
        equipo = equipo.strip()

        # Verificar si el equipo ingresado es válido para el proyecto seleccionado
        if equipo in opciones.get(proyecto, []):
            # Obtener el contador para el equipo actual
            idx = counters[equipo]
            counters[equipo] += 1
            if equipo == "RadiosT":
                materials.append("{:<1} {:<2}".format(str(idx)+".", '"Radio ALOHA AFIG Total 6"'))
                materials.append("{:<1} {:<2}".format(str(idx+1)+".", "Lug 90'total 6"))
                materials.append("{:<1} {:<2}".format(str(idx+2)+".", "Ret-cable total Total 3"))
                idx_total = idx + 2

            elif equipo == "AntenasT":
                materials.append("{:<1} {:<2}".format(str(idx)+".", '"Antenas 65C 8 puerto total 3"'))
                materials.append("{:<1} {:<2}".format(str(idx+1)+".", "RF Jumpers Mimi to mimi 24"))
                materials.append("{:<1} {:<2}".format(str(idx+2)+".", "snapping total 180"))
                idx_total = idx + 2
                
            elif equipo == "RadiosVT":
                materials.append("{:<1} {:<2}".format(str(idx)+".", '"Radio 6601 8845 Total 6"'))
                materials.append("{:<1} {:<2}".format(str(idx+1)+".", "Lug 90'total 6"))
                materials.append("{:<1} {:<2}".format(str(idx+2)+".", "Heat Shrink"))
                idx_total = idx + 3

            elif equipo == "AntenasA":
                materials.append("{:<1} {:<2}".format(str(idx)+".", '"Antenas 65C 8 puerto total 3"'))
                materials.append("{:<1} {:<2}".format(str(idx+1)+".", "RF Jumpers Mimi to mimi 24"))
                materials.append("{:<1} {:<2}".format(str(idx+2)+".", "snapping total 180"))
                idx_total = idx + 3

            elif equipo == "AntenasW":
                materials.append("{:<1} {:<2}".format(str(idx)+".", '"Antenas 65C 8 puerto total 3"'))
                materials.append("{:<1} {:<2}".format(str(idx+1)+".", "RF Jumpers Mimi to mimi 24"))
                materials.append("{:<1} {:<2}".format(str(idx+2)+".", "snapping total 180"))
                idx_total = idx + 3
                
            elif equipo == "AntenasWC":
                materials.append("{:<1} {:<2}".format(str(idx)+".", '"Antenas 65C 8 puerto total 3"'))
                materials.append("{:<1} {:<2}".format(str(idx+1)+".", "RF Jumpers Mimi to mimi 24"))
                materials.append("{:<1} {:<2}".format(str(idx+2)+".", "snapping total 180"))
                idx_total = idx + 3    

            else:
                # Mostrar mensaje de error si el equipo ingresado no es válido para el proyecto seleccionado
                result_label.config(text=f"Equipo '{equipo}' no es válido para el proyecto '{proyecto}'")
                return
            
            
            # Agregar la línea horizontal después de cada resultado
            if counters[equipo] > 1:
             materials.append("-" * 50) 
             materials.append("")  # Agregar una línea en blanco para separar las listas de materiales

    
    result = "\n".join(materials)
    result_label.config(text=result, font=("Arial", 16))
    
    
def clear_results(label):
     label.config(text="")

def clear_input(entry):
      entry.delete(0, tk.END)

root = tk.Tk()
root.title("Ingreso de equipo")
root.geometry("850x700")

equipo_entry = tk.Entry(root, width=50, borderwidth=3) 
equipo_entry.pack()

buttons_frame = tk.Frame(root)
buttons_frame.pack()

# Botones de aceptar y borrar
project = tk.StringVar(value="PROYECTO")
tk.OptionMenu(buttons_frame, project, *opciones.keys()).pack(side=tk.LEFT, padx=10)
tk.Button(buttons_frame, text="Aceptar", command=lambda: imprimir_materiales(equipo_entry.get())).pack(side=tk.LEFT, padx=10)
tk.Button(buttons_frame, text="Limpiar ▼", command=lambda: clear_results(result_label)).pack(side=tk.LEFT, padx=10)
tk.Button(buttons_frame, text="Borrar ▲", command=lambda: clear_input(equipo_entry)).pack(side=tk.LEFT, padx=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack()

root.mainloop()