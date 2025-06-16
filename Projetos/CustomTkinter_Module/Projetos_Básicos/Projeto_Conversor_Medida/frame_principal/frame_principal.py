from customtkinter import CTkFrame
from .widgets_frame_principal import LabelInfoNúmero, EntryMedidaMetros, LabelResultado, ButtonConverter, ButtonLimpar

class FramePrincipal(CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.__label_info_número = LabelInfoNúmero(self)
        self.__entry_medida_metros = EntryMedidaMetros(self)
        self.__label_resultado = LabelResultado(self)
        self.__button_converter = ButtonConverter(self)
        self.__button_limpar = ButtonLimpar(self)

        self.__entry_medida_metros.focus()

        self.__label_info_número.grid(row=0, column=0, padx=(10, 5), pady=(10, 10))
        self.__entry_medida_metros.grid(row=0, column=1, padx=(0, 10), pady=(10, 10))
        self.__button_converter.grid(row=1, column=0, columnspan=2, padx=(0, 120), pady=(0, 15))
        self.__button_limpar.grid(row=1, column=0, columnspan=2, padx=(120, 0), pady=(0, 15))
        
        self.__show_buttons = [
            self.__button_converter.get_show(), self.__button_limpar.get_show()
        ]

        self.__cópia_show_buttons = []
        self.__count = self.__tamanho_widget_resultado = 0
        self.__medida = ''

        self.update()
        self.__atualização()


    def __atualização(self):
        self.__show_buttons = [
            self.__button_converter.get_show(), self.__button_limpar.get_show()
        ]

        self.__medida = self.__entry_medida_metros.get_medida()

        if self.__show_buttons[0] == True and self.__show_buttons[1] == False:
            self.__button_converter.configure(state='disabled')
            self.__button_limpar.configure(state='normal')

            self.__cópia_show_buttons = self.__show_buttons.copy()

            if self.__medida != '':
                self.__entry_medida_metros.configure(state='disabled')
                
                self.__label_resultado.set_resultado(self.__medida)
                self.__label_resultado.grid(row=2, column=0, columnspan=2, padx=(10, 10), pady=(0, 15))
                
                self.__count = 0

                if self.__label_resultado.winfo_width() >= 533:
                    self.__tamanho_widget_resultado = self.__label_resultado.winfo_width()

            else:
                self.__button_converter.set_false_resultado()

        elif self.__show_buttons[0] == False and self.__show_buttons[1] == True:
            self.__button_converter.configure(state='normal')
            self.__button_limpar.configure(state='disabled')

            self.__entry_medida_metros.configure(state='normal')
            
            if self.__count == 0:
                self.__entry_medida_metros.delete(0, 'end')
                self.__count += 1
            
            self.__cópia_show_buttons = self.__show_buttons.copy()

            self.__tamanho_widget_resultado = 0

            self.__label_resultado.grid_forget()

        elif self.__show_buttons[0] == False and self.__show_buttons[1] == False:
            self.__button_converter.configure(state='normal')
            self.__button_limpar.configure(state='disabled')
            self.__cópia_show_buttons = self.__show_buttons.copy()

        else:
            if self.__cópia_show_buttons[0] == True and self.__cópia_show_buttons[1] == False:
                self.__button_converter.set_false_resultado()
            
            elif self.__cópia_show_buttons[0] == False and self.__cópia_show_buttons[1] == True:
                self.__button_limpar.set_false_resultado()

        self.after(1, self.__alteração_padx)


    def __alteração_padx(self):
        if self.__tamanho_widget_resultado == 0:
            self.__label_info_número.grid_configure(padx=(10, 10))
            self.__entry_medida_metros.grid_configure(padx=(10, 10))
        else:
            self.__label_info_número.grid_configure(padx=(120, 10))
            self.__entry_medida_metros.grid_configure(padx=(10, 120))

        self.after(1, self.__atualização)