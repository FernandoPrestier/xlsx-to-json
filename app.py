import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os


def convertir():
    archivo = filedialog.askopenfilename(
        title="Seleccionar Excel",
        filetypes=[("Excel", "*.xlsx *.xls")]
    )

    if not archivo:
        return

    try:
        df = pd.read_excel(archivo)
        df = df.fillna("")

        salida = os.path.join(
            os.path.dirname(archivo),
            "productos.json"
        )

        df.to_json(
            salida,
            orient="records",
            indent=2,
            force_ascii=False
        )

        messagebox.showinfo(
            "Completado",
            f"Archivo creado:\n{salida}"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )


app = tk.Tk()
app.title("Excel a JSON")
app.geometry("400x200")

label = tk.Label(
    app,
    text="Convertidor de catálogo Excel → JSON",
    font=("Arial", 12)
)

label.pack(pady=30)

boton = tk.Button(
    app,
    text="Seleccionar Excel",
    command=convertir,
    width=20,
    height=2
)

boton.pack()

app.mainloop()
