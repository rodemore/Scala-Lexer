
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

ventana = tk.Tk()

def analisis_lexico():
    messagebox.showinfo(message="Analisis léxico completado", title="Análisis Léxico")

def analisis_semantico():
    messagebox.showinfo(message="Analisis semantico completado", title="Análisis Semántico")



ventana.title("Scala Lexer")

width =  1200
height = 720
boton_font = font.Font(size=18)
ventana.geometry(str(width)+"x"+str(height))

ventana.configure(background = '#f8f8f8')


input_label = tk.Label(ventana, text="Input", bg= "#f8f8f8",fg="#516370")
input_label.config(font=("Courier", 24))
input_label.place(x = width/4, y =15)

output_label = tk.Label(ventana, text="Output",bg= "#f8f8f8", fg="#516370", state='disabled')

output_label.config(font=("Courier", 24))
output_label.place(x = width*3/4, y =15)

input_entry = tk.Entry(ventana)
input_entry.place(x = 2* width*0.03,
        y = 50,
        width=width*0.45,
        height=height*0.80)


output_entry = tk.Entry(ventana)
output_entry.place(x = width/2 + 2*width*0.03,
        y = 50,
        width=width*0.45,
        height=height*0.80)

lexico_boton = tk.Button(text="Analisis léxico", command=analisis_lexico, bg='#0052cc', fg='#f8f8f8')
semantico_boton = tk.Button(text="Analisis Semántico", command=analisis_semantico, bg='#0052cc', fg='#f8f8f8')

lexico_boton.place(x = width/4,
        y = 650,
        width=width*0.25,
        height=40)

semantico_boton.place(x =width*0.31 +width/4,
        y = 650,
        width=width*0.25,
        height=40)
lexico_boton["font"] = boton_font
semantico_boton["font"] = boton_font

ventana.mainloop()