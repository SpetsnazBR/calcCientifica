import tkinter as tk
from tkinter import messagebox
import math

class CalculadoraCientifica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica Python")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        self.expressao = ""
        self.input_text = tk.StringVar()

        visor_frame = tk.Frame(self.root, width=400, height=100, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        visor_frame.pack(side=tk.TOP)

        visor = tk.Entry(visor_frame, font=('arial', 24, 'bold'), textvariable=self.input_text, width=22, bg="#eee", bd=0, justify=tk.RIGHT)
        visor.grid(row=0, column=0)
        visor.pack(ipady=20) 
        
        botoes_frame = tk.Frame(self.root, width=400, height=500, bg="grey")
        botoes_frame.pack()
        
        botoes = [
            ('C', 0, 0), ('√', 0, 1), ('^', 0, 2), ('/', 0, 3),
            ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('*', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('-', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('+', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('log', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('π', 5, 2), ('=', 5, 3)
        ]

        for (texto, linha, col) in botoes:
            tk.Button(botoes_frame, text=texto, width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                      command=lambda t=texto: self.ao_clicar(t)).grid(row=linha, column=col, padx=1, pady=1)

    def ao_clicar(self, botao):
        if botao == "C":
            self.expressao = ""
        elif botao == "=":
            try:
            
                temp_expr = self.expressao.replace('π', str(math.pi)).replace('^', '**')
                resultado = str(eval(temp_expr))
                self.expressao = resultado
            except Exception as e:
                messagebox.showerror("Erro", "Cálculo Inválido")
                self.expressao = ""
        elif botao in ["sin", "cos", "tan", "log", "√"]:
            self.calcular_cientifico(botao)
            return
        else:
            self.expressao += str(botao)
        
        self.input_text.set(self.expressao)

    def calcular_cientifico(self, operacao):
        try:
            val = float(self.expressao)
            if operacao == "sin": res = math.sin(math.radians(val))
            elif operacao == "cos": res = math.cos(math.radians(val))
            elif operacao == "tan": res = math.tan(math.radians(val))
            elif operacao == "log": res = math.log10(val)
            elif operacao == "√": res = math.sqrt(val)
            
            self.expressao = str(round(res, 4))
            self.input_text.set(self.expressao)
        except:
            messagebox.showerror("Erro", "Valor inválido para esta função")
            self.expressao = ""

if __name__ == "__main__":
    root = tk.Tk()
    CalculadoraCientifica(root)
    root.mainloop()