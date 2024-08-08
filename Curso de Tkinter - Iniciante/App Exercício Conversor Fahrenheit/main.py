from tkinter import *

#GUI
root = Tk()
root.title('Conversor de Temperatura'.upper())
root.geometry('400x200+500+200')
root.resizable(0, 0)

#função
def clique_button_converter_grau():
    label_temperatura_em_celsius['text'] = f'{(float(entry_grau.get()) - 32) * (5 / 9):.1f}°C - Celsius'


#widget
frame_conversor = Frame(root)

label_informação_textual = Label(
    frame_conversor, text='Insira o valor em Fahrenheit - (°F)', font='Arial 13 bold', padx=70
)

entry_grau = Entry(
    frame_conversor, width=25, justify='center' ,bd=3, relief='sunken', font='Arial 12'
)

label_temperatura_em_celsius = Label(
    frame_conversor, font='Arial 15'
)

button_converter_grau = Button(
    frame_conversor, text='Converter', font='Arial 15', padx=10, bg='#75a3a3', command=clique_button_converter_grau
)

#layout
frame_conversor.grid()

label_informação_textual.grid(row=0)
entry_grau.grid(row=1)
label_temperatura_em_celsius.grid(row=2, pady= 25)
button_converter_grau.grid(row=3)

#foco 
entry_grau.focus()

#GUI
root.mainloop()