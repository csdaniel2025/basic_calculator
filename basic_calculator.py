import tkinter as tk
import customtkinter as ctk


class Basic_Calculator():
    def __init__(self, display):
        self.display = display
        self.display.geometry("450x600") 
        self.display.configure(bg="#333333")
        self.display.title("Basic Calculator")
        
        self.frame = tk.Frame(self.display, bg="#333333")
        self.frame.pack(expand=True)
        
        #nubmers
        self.num_pad = [
                "1", "2", "3", 
                "4", "5", "6", 
                "7", "8", "9", 
                "0"
                ]
        #operators
        self.num_opt = ["÷", "×", "-", "+"]
        #clearing
        self.num_erase = ["C", "⌫", "."]
    
        #
        self.A = 0
        self.B = None
        self.arith_opt = None
        self.result = None

    
        self.show_widgets()
        
        
    def clear_all(self):
        self.A = 0
        self.B = None
        self.arith_opt = None
        self.result = None
  
        
    def convert_nubmers(self, value):
        print(value)
        if value == "Error":
            return "Error"
        elif value % 1 == 0:
            num = int(value)
            return str(num)
        return str(value)
        
    def calculating(self, val):
        current_text = self.screenBot.cget("text")
        if val in self.num_pad:
            if current_text == "0":
                self.screenBot.configure(text=val)
            elif current_text != "0":
                self.screenBot.configure(text=current_text + val)
                
        elif val in self.num_opt:
            if self.arith_opt is None:
                self.A = current_text
                self.arith_opt = val
                self.screenTop.configure(text=current_text + f" {self.arith_opt} ")
                self.screenBot.configure(text="0")
        elif val == ".":
            if "." not in current_text:
                self.screenBot.configure(text=current_text + val)
        elif val == "=":
            if self.A != "0" and self.arith_opt != None:
                self.B = current_text
                print(self.A, self.arith_opt, self.B) #check variable values
                numA = float(self.A)
                numB = float(self.B)
                
                if self.arith_opt == "÷" and self.B != "0":
                    self.result = self.convert_nubmers(numA / numB)
                elif self.arith_opt == "÷" and self.B == "0":
                    self.result = self.convert_nubmers("Error")
                elif self.arith_opt == "×":
                    self.result = self.convert_nubmers(numA * numB)
                elif self.arith_opt == "-":
                    self.result = self.convert_nubmers(numA - numB)
                elif self.arith_opt == "+":
                    self.result = self.convert_nubmers(numA + numB)
                    
                  
                self.screenTop.configure(text=self.A + f" {self.arith_opt} " + self.B)
                self.screenBot.configure(text=self.result)
                self.clear_all()
                
                
        elif val == "C":
            self.screenTop.configure(text="0")
            self.screenBot.configure(text="0") 
            self.clear_all()
            print(self.A, self.arith_opt, self.B) #check variable values  
        elif val == "⌫":
            self.screenBot.configure(text=current_text[0:-1])
            current_text = self.screenBot.cget("text")
            if current_text == "":
                self.screenBot.configure(text="0")
                    
            
        
    def show_widgets(self):

        # header = ctk.CTkLabel(self.frame, text="Calculator", font=("Ubuntu", 35))
        # header.grid(row=0, column=0, columnspan=6, pady=20)
        
        self.screenTop = ctk.CTkLabel(self.frame, text="0", font=("Ubuntu", 25), text_color="black", fg_color="#F5FFFA", width=260, height=50, anchor="e")
        self.screenTop.grid(row=1, column=0, columnspan=6, pady=1)
        
        self.screenBot = ctk.CTkLabel(self.frame, text="0", font=("Ubuntu", 25), text_color="black", fg_color="#F5FFFA", width=260, height=40, anchor="e")
        self.screenBot.grid(row=2, column=0, columnspan=6, pady=(4, 6))
        
        for i in range(len(self.num_pad) - 1):
            num = self.num_pad[i]
            numbers = ctk.CTkButton(self.frame, text=num, width=60, height=50, text_color="black", fg_color="#F5FFFA", hover_color="#B3B3B3",
                                command=lambda v=num: self.calculating(v))
            
            rw = i // 3 + 4
            cl = i % 3 + 0
            
            numbers.grid(row=rw, column=cl, padx=5, pady=5)
            
        zero = ctk.CTkButton(self.frame, text="0", width=60, height=50, text_color="black", fg_color="#F5FFFA", hover_color="#B3B3B3",
                                command=lambda v="0": self.calculating(v))
        zero.grid(row=7, column=1, padx=5, pady=5) 
            
        for i in range(len(self.num_opt)):
            opt = self.num_opt[i]
            operators = ctk.CTkButton(self.frame, text=opt, width=55, height=50, text_color="black", fg_color="#F5FFFA", hover_color="#B3B3B3",
                                command=lambda v=opt: self.calculating(v))
            
            operators.grid(row=i + 3, column=3, padx=5, pady=5)
            
        for i in range(len(self.num_erase)):
            ers = self.num_erase[i]
            erase = ctk.CTkButton(self.frame, text=ers, width=60, height=50, text_color="black", fg_color="#F5FFFA", hover_color="#B3B3B3",
                                command=lambda v=ers: self.calculating(v))
            
            cl = i % 3 + 0
            erase.grid(row=3, column=cl, padx=5, pady=5)
            
          
        equal = ctk.CTkButton(self.frame, text="=", width=60, height=50, text_color="black", fg_color="#F5FFFA", hover_color="#B3B3B3",
                                command=lambda v="=": self.calculating(v))
        equal.grid(row=7, column=2, padx=5, pady=5) 
        
        
            
            

display = tk.Tk()
mainrunner = Basic_Calculator(display)
display.mainloop()