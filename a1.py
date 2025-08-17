import tkinter
from tkinter import font, messagebox
import a1, a2

class LoginPage:
    def __init__(self):
        self.wn = tkinter.Tk()
        self.wn.title('Login Page')
        self.wn.state('zoomed')
        title_font = font.Font(family='Helvetica', size=36, weight='bold')
        label_font = font.Font(family='Helvetica', size=16)
        button_font = font.Font(family='Helvetica', size=16)
        button_font2 = font.Font(family='Helvetica', size=12)
        bg_color = 'red'  
        tkinter.Label(self.wn, text='🏦 Employee Management System 🏢', font=title_font, bg=bg_color, fg='black', pady=50).pack(fill=tkinter.X)
        frm = tkinter.Frame(self.wn, bg=bg_color)
        frm.pack(pady=50)
        tkinter.Label(frm, text='Username:', font=label_font, bg=bg_color, fg='black').grid(row=0, column=0, padx=20, pady=10, sticky='w')
        self.t1 = tkinter.StringVar()
        tkinter.Entry(frm, font=label_font, textvariable=self.t1).grid(row=0, column=1, padx=20, pady=10)
        tkinter.Label(frm, text='Password:', font=label_font, bg=bg_color, fg='black').grid(row=1, column=0, padx=20, pady=10, sticky='w')
        self.t2 = tkinter.StringVar()
        tkinter.Entry(frm, font=label_font, textvariable=self.t2, show='*').grid(row=1, column=1, padx=20, pady=10)
        tkinter.Button(frm, text='Login', font=button_font, command=self.login, bg='#2ecc71', fg='white').grid(row=2, column=0, padx=20, pady=20)        
        tkinter.Button(frm, text='Exit Page', font=button_font2, command=self.exit, bg='#e74c3c', fg='white').grid(row=2, column=2, padx=20, pady=15)
        self.wn.mainloop()
    def login(self):
        if self.t1.get() == 'admin' and self.t2.get() == 'admin':
            messagebox.showinfo('EMS', 'successfully logging in....◝')
            self.wn.destroy()
            a2.Navpage()
        else:
            if self.t1.get() != 'admin' and self.t2.get() != 'admin':
                messagebox.showinfo('EMS', 'Wrong Username and Password')
            elif self.t1.get()!='admin':
                messagebox.showinfo('EMS', 'Wrong Username')
            else:
                 messagebox.showinfo('EMS', 'Wrong Password')            
    def exit(self):
        self.wn.destroy()
if __name__ == '__main__':
    LoginPage()
