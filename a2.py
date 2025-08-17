import tkinter
from tkinter import font, messagebox
import a1, a5
import a3, a4

class Navpage:
    def __init__(self):
        self.wn = tkinter.Tk()
        self.wn.title('Nav Page')
        self.wn.state('zoomed')
        self.wn.configure(bg='#2c3e50')
        f1 = font.Font(family='Helvetica', size=36, weight='bold')
        f2 = font.Font(family='Helvetica', size=16, weight='bold')
        tkinter.Label(self.wn, text='Employee Management System', font=f1, bg='#2980b9', fg='white', pady=50).pack(fill=tkinter.X)     
        tkinter.Button(self.wn, text='Employee Details', bg='#3498db', fg='white', font=f2, width=20, command=self.showemp).pack(pady=10)
        tkinter.Button(self.wn, text='Attendance', bg='#f39c12', fg='black', font=f2, width=20, command=self.showatt).pack(pady=10)          
        tkinter.Button(self.wn, text='Salary', bg='#27ae60', fg='white', font=f2, width=20, command=self.salpage).pack(pady=10)
        tkinter.Button(self.wn, text='Logout', bg='#c0392b', fg='white', font=f2, width=20, command=self.logout).pack(pady=10)
        self.wn.mainloop()

    def showemp(self):
        self.wn.destroy()
        a3.EmployeePage()

    def showatt(self):
        self.wn.destroy()
        a4.EmployeeAttendanceApp()

    def salpage(self):
        self.wn.destroy()
        a5.SalaryManagementApp()

    def logout(self):
        self.wn.destroy()
        a1.LoginPage()

if __name__ == '__main__':
    Navpage()
    
