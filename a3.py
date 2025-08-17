import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
from tkcalendar import DateEntry
import a2

class EmployeePage:
    def __init__(self):
        self.employees = [] 
        self.wn = tk.Tk()
        self.wn.title('Employee Details')
        self.wn.state('zoomed')
        self.wn.configure(bg='#34495e')
        self.setup()

    def setup(self):
        self.frm = tk.Frame(self.wn, bg='lightgray')
        self.frm.pack(pady=20)

        tk.Label(self.frm, text='Employee ID', bg='lightblue', width=15, font=('Helvetica', 12, 'bold')).grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self.frm, text='Name', bg='lightblue', width=15, font=('Helvetica', 12, 'bold')).grid(row=2, column=0, padx=10, pady=5)
        tk.Label(self.frm, text='Gender', bg='lightblue', width=15, font=('Helvetica', 12, 'bold')).grid(row=3, column=0, padx=10, pady=5)
        tk.Label(self.frm, text='Date of Birth', bg='lightblue', width=15, font=('Helvetica', 12, 'bold')).grid(row=4, column=0, padx=10, pady=5)
        tk.Label(self.frm, text='Qualification', bg='lightblue', width=15, font=('Helvetica', 12, 'bold')).grid(row=5, column=0, padx=10, pady=5)
        tk.Label(self.frm, text='Job Role', bg='lightblue', width=15, font=('Helvetica', 12, 'bold')).grid(row=6, column=0, padx=10, pady=5)

        self.emp_id = tk.StringVar()
        self.emp_name = tk.StringVar()
        self.emp_gender = tk.StringVar()
        self.emp_date = tk.StringVar()
        self.emp_qua = tk.StringVar()
        self.emp_position = tk.StringVar()
        self.emp_gender.set('MALE')

        tk.Entry(self.frm, textvariable=self.emp_id, width=30, font=('Helvetica', 12)).grid(row=1, column=1, padx=10, pady=5)
        tk.Entry(self.frm, textvariable=self.emp_name, width=30, font=('Helvetica', 12)).grid(row=2, column=1, padx=10, pady=5)
        tk.Radiobutton(self.frm, variable=self.emp_gender, text='Male', value='MALE', font=('Helvetica', 12)).grid(row=3, column=1, padx=10, pady=5)
        tk.Radiobutton(self.frm, variable=self.emp_gender, text='Female', value='FEMALE', font=('Helvetica', 12)).grid(row=3, column=2, padx=10, pady=5)

        dob_entry = DateEntry(self.frm, textvariable=self.emp_date, date_pattern='yyyy-mm-dd', width=30, font=('Helvetica', 12))
        dob_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Entry(self.frm, textvariable=self.emp_qua, width=30, font=('Helvetica', 12)).grid(row=5, column=1, padx=10, pady=5)
        tk.Entry(self.frm, textvariable=self.emp_position, width=30, font=('Helvetica', 12)).grid(row=6, column=1, padx=10, pady=5)

        tk.Button(self.frm, text='Save', command=self.add_employee, width=15, font=('Helvetica', 12, 'bold'), bg='green', fg='white').grid(row=7, column=0, pady=10, padx=10)
        tk.Button(self.frm, text='Modify', command=self.modify_employee, width=15, font=('Helvetica', 12, 'bold'), bg='orange', fg='white').grid(row=7, column=2, pady=10, padx=10)
        tk.Button(self.frm, text='Delete Employee', command=self.delete_employee, width=15, font=('Helvetica', 12, 'bold'), bg='red', fg='white').grid(row=8, column=0, pady=10, padx=10)
        tk.Button(self.frm, text='Back', command=self.exit_all, width=15, font=('Helvetica', 12, 'bold'), bg='blue', fg='white').grid(row=8, column=2, pady=10, padx=10)

        self.tree = ttk.Treeview(self.wn, columns=('ID', 'Name', 'Gender', 'Date of Birth', 'Qualification', 'Job Role'), show='headings')
        self.tree.heading('ID', text='Employee ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Gender', text='Gender')
        self.tree.heading('Date of Birth', text='Date of Birth')
        self.tree.heading('Qualification', text='Qualification')
        self.tree.heading('Job Role', text='Job Role')
        self.tree.pack()

        self.connect_and_fetch()
        self.wn.mainloop()

    def connect_and_fetch(self):
        try:
            self.con = pymysql.connect(user='root', password='rajesh@2006', host='localhost', database='project', port=3306)
            self.cr = self.con.cursor()
            self.cr.execute("SELECT * FROM employeedetails")
            self.employees = self.cr.fetchall()
            self.view_employees()
        except pymysql.Error as e:
            messagebox.showerror('Connection Error', f'Error connecting to database: {e}')

    def add_employee(self):
        emp_id = self.emp_id.get()
        emp_name = self.emp_name.get()
        emp_gender = self.emp_gender.get()
        emp_date = self.emp_date.get() 
        emp_qua = self.emp_qua.get()
        emp_position = self.emp_position.get()
        
        if emp_id and emp_name and emp_gender and emp_date and emp_qua and emp_position:
            try:
                sql = "INSERT INTO employeedetails VALUES (%s, %s, %s, %s, %s, %s)"
                values = (emp_id, emp_name, emp_gender, emp_date, emp_qua, emp_position)
                self.cr.execute(sql, values)
                self.con.commit()
                
                self.connect_and_fetch() 
                messagebox.showinfo('Success', 'Employee added successfully!')
                self.clear_entries()
            except pymysql.Error as e:
                messagebox.showerror('Database Error', f'Error adding employee: {e}')
        else:
            messagebox.showwarning('Input Error', 'Please fill all fields')
     
    def modify_employee(self):
        selected_item = self.tree.selection()
        if selected_item:
            emp_id, emp_name, emp_gender, emp_date, emp_qua, emp_position = self.tree.item(selected_item)['values']
            self.emp_id.set(emp_id)
            self.emp_name.set(emp_name)
            self.emp_gender.set(emp_gender)
            self.emp_date.set(emp_date)
            self.emp_qua.set(emp_qua)
            self.emp_position.set(emp_position)
            self.dele()
        else:
            messagebox.showwarning('Selection Error', 'Please select an employee to modify')


    def dele(self):
        selected_item = self.tree.selection()
        if selected_item:
            emp_id = self.tree.item(selected_item)['values'][0]
            self.con = pymysql.connect(user='root', password='rajesh@2006', host='localhost', database='project', port=3306)
            self.cr = self.con.cursor()
                
            delete_query = "DELETE FROM employeedetails WHERE EmployeeId= %s"
            self.cr.execute(delete_query, (emp_id,))
            self.con.commit()
                
            self.connect_and_fetch()  
                
        else:
            messagebox.showwarning('Selection Error', 'Please select an employee to delete')


    def delete_employee(self):
        selected_item = self.tree.selection()
        if selected_item:
            emp_id = self.tree.item(selected_item)['values'][0]
            try:
                delete_query = "DELETE FROM employeedetails WHERE EmployeeId= %s"
                self.cr.execute(delete_query, (emp_id,))
                self.con.commit()
                
                self.connect_and_fetch()  
                messagebox.showinfo('Success', 'Employee deleted successfully!')
                self.clear_entries()
                
            except pymysql.Error as e:
                messagebox.showerror('Database Error', f'Error deleting employee: {e}')
        else:
            messagebox.showwarning('Selection Error', 'Please select an employee to delete')

    def view_employees(self):
        self.tree.delete(*self.tree.get_children())
        for emp in self.employees:
            self.tree.insert('','end',values=emp)

    def exit_all(self):
        self.wn.destroy()
        a2.Navpage()

    def clear_entries(self):
        self.emp_id.set('')
        self.emp_name.set('')
        self.emp_gender.set('')
        self.emp_date.set('')
        self.emp_qua.set('')
        self.emp_position.set('')

if __name__ == '__main__':
    EmployeePage()


