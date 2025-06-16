from customtkinter import CTkFrame
from .widgets_frame_principal import LabelMédia, ButtonLimpar, ButtonCalcular, LabelPrimeiraNota, LabelSegundaNota, EntryPrimeiraNota, EntrySegundaNota

class FramePrincipal(CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.configure(corner_radius=0)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.__label_primeira_nota = LabelPrimeiraNota(self)
        self.__label_segunda_nota = LabelSegundaNota(self)
        self.__entry_primeira_nota = EntryPrimeiraNota(self)
        self.__entry_segunda_nota = EntrySegundaNota(self)

        self.__button_calcular = ButtonCalcular(self)
        self.__button_limpar = ButtonLimpar(self)

        self.__label_média = LabelMédia(self)

        self.__label_primeira_nota.grid(row=0, column=0, padx=(15,15), pady=(10,0))
        self.__entry_primeira_nota.grid(row=1, column=0, padx=(10,0))
        self.__label_segunda_nota.grid(row=2, column=0, padx=(15,15), pady=(20,0))
        self.__entry_segunda_nota.grid(row=3, column=0, padx=(10,0), pady=(0, 15))

        self.__button_calcular.grid(row=0, column=1, padx=(15, 15), pady=(15, 5))
        self.__button_limpar.grid(row=1, column=1, padx=(12, 8))

        self.__label_média.grid(row=2, rowspan=2, column=1)

        self.__cliques_buttons = [
            self.__button_calcular.get_clique(), self.__button_limpar.get_clique()
        ]

        self.__notas = []
        self.__cópia_clique = []
        self.__count = 0

        self.__atualizações()

    
    def __atualizações(self):
        self.__cliques_buttons = [
            self.__button_calcular.get_clique(), self.__button_limpar.get_clique()
        ]

        if self.__cliques_buttons[0] == True and self.__cliques_buttons[1] == False:
            self.__button_calcular.configure(state='disabled')
            self.__button_limpar.configure(state='normal')
            
            self.__entry_primeira_nota.configure(state='disabled')
            self.__entry_segunda_nota.configure(state='disabled')

            self.__notas = [
                self.__entry_primeira_nota.get_nota(), 
                self.__entry_segunda_nota.get_nota()
            ]

            try:
                for c in range(0, 2):
                    self.__notas[c] = float(f'{self.__notas[c]:.1f}')

                self.__label_média.set_média(self.__notas[0], self.__notas[1])
                self.__label_média.set_text(True)
            except:
                self.__button_calcular.set_clique_false()

                self.__entry_primeira_nota.configure(state='normal')
                self.__entry_segunda_nota.configure(state='normal')

            self.__count = 0
            self.__cópia_clique.clear()

        elif self.__cliques_buttons[0] == False and self.__cliques_buttons[1] == True:
            self.__button_calcular.configure(state='normal')
            self.__button_limpar.configure(state='disabled')
            self.__entry_primeira_nota.configure(state='normal')
            self.__entry_segunda_nota.configure(state='normal')

            if self.__count == 0:
                self.__entry_primeira_nota.delete(0, 'end')
                self.__entry_primeira_nota.set_nota()
                self.__entry_segunda_nota.delete(0, 'end')
                self.__entry_segunda_nota.set_nota()
                self.__notas.clear()
                self.__count += 1

            if self.__cópia_clique[0] == True and self.__cópia_clique[1] == True:
                self.__cópia_clique.clear()

            self.__label_média.set_text(False)

        elif self.__cliques_buttons[0] == False and self.__cliques_buttons[1] == False:
            self.__button_calcular.configure(state='normal')
            self.__button_limpar.configure(state='disabled')

        else:
            if self.__cópia_clique[0] == True and self.__cópia_clique[1] == False:
                self.__button_calcular.set_clique_false()
                self.__cópia_clique.clear()
            
            elif self.__cópia_clique[0] == False and self.__cópia_clique[1] == True:
                self.__button_limpar.set_clique_false()
                self.__cópia_clique.clear()
        
        if self.__cópia_clique == []:
            self.__cópia_clique = self.__cliques_buttons.copy()

        self.after(1, self.__atualizações)