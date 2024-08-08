from tkinter import *

#GUI
root = Tk()
root.title('App')
root.geometry('+700+300')


#variáveis
nome_digitado_pelo_usuário = StringVar()
nome_digitado_pelo_usuário.set('Bem Vinde!')

#funcões
def clique_button_confirmar():
    nome_digitado_pelo_usuário.set(f'Bem Vinde {entry_nome.get().capitalize()}!')


#widget
label_nome = Label(root, text='Qual o seu nome?')
entry_nome = Entry(root)
button_confirmar = Button(root, text='Confirmar', command=clique_button_confirmar)
label_mostrador_nome = Label(root, textvariable=nome_digitado_pelo_usuário)

#layout
label_mostrador_nome.grid(row=0, columnspan=2)
label_nome.grid(row=1, column=0)
entry_nome.grid(row=1, column=1)
button_confirmar.grid(row=2, column=1, sticky=E)


#GUI
root.mainloop()