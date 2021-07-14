
import tkinter as tk
from tkinter import messagebox, END
import tkinter.font as font

import scalaSintactico as stx
import scalaLexer as sl

ventana = tk.Tk()



def analisis_sintactico_semantico():
        code_lines = str(input_entry.get("1.0","end-1c"))
        stx.error_status[0] = False
        output_entry.delete('1.0', END)
        try:
                result = stx.parser.parse(code_lines, tracking=True)
                
                if (stx.error_status[0] == False):
                        output_entry.insert('1.0', "Sintaxis OK")
                else:
                        output_entry.insert('1.0', "Sintaxis Error!!")


        except:
                print(error)
                return

        messagebox.showinfo(message="Analisis sintáctico/semántico completado", title="Análisis Sintáctico/Semántico")


def analisis_lexico():
        code_lines = str(input_entry.get("1.0","end-1c"))
        output_entry.delete('1.0', END)
        lexer = sl.lexer
        try:
                lexer.input(code_lines)
                tokens = sl.getTokens(lexer)
                for i, tok in enumerate(tokens):

                        output_entry.insert(str(i)+'.0', str(tok)+"\n")
                
        except EOFError:
                return
        messagebox.showinfo(message="Analisis léxico completado", title="Análisis Léxico")



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

input_entry = tk.Text(ventana,font=("Courier", 12))
input_entry.place(x = 2* width*0.03,
        y = 50,
        width=width*0.45,
        height=height*0.80)


output_entry = tk.Text(ventana,font=("Courier", 12))
output_entry.place(x = width/2 + 2*width*0.03,
        y = 50,
        width=width*0.45,
        height=height*0.80)

lexico_boton = tk.Button(text="A. Léxico", command=analisis_lexico, bg='#0052cc', fg='#f8f8f8')
sintactico_boton = tk.Button(text="A. Sintáctico/Semántico", command=analisis_sintactico_semantico, bg='#0052cc', fg='#f8f8f8')

lexico_boton.place(x = width/4,
        y = 650,
        width=width*0.25,
        height=40)

sintactico_boton.place(x =width*0.31 +width/4,
        y = 650,
        width=width*0.25,
        height=40)
lexico_boton["font"] = boton_font
sintactico_boton["font"] = boton_font

ventana.mainloop()