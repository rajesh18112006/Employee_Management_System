import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
import a2

class EmployeeAttendanceApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Employee Attendance Management")
        self.window.configure(bg='#34495e')
        self.create_widgets()      
        self.con = pymysql.connect(user='root', password='rajesh@2006', host='localhost', database='project', port=3306)
        self.cr = self.con.cursor()
        self.connectall()
        
    def create_widgets(self):

        self.employee_id_label = tk.Label(self.window, text="Employee ID:", bg='#f0f0f0', font=('Helvetica', 12))
        self.employee_id_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.employee_id_entry = tk.Entry(self.window, font=('Helvetica', 12))
        self.employee_id_entry.grid(row=0, column=1, padx=10, pady=10)
        

        self.employee_name_label = tk.Label(self.window, text="Employee Name:", bg='#f0f0f0', font=('Helvetica', 12))
        self.employee_name_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.employee_name_entry = tk.Entry(self.window, font=('Helvetica', 12))
        self.employee_name_entry.grid(row=1, column=1, padx=10, pady=10)


        self.employee_position_label = tk.Label(self.window, text="Jobroll:", bg='#f0f0f0', font=('Helvetica', 12))
        self.employee_position_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.employee_position_entry = tk.Entry(self.window, font=('Helvetica', 12))
        self.employee_position_entry.grid(row=2, column=1, padx=10, pady=10)


        self.monthly_present_days_label = tk.Label(self.window, text="Monthly Present Days:", bg='#f0f0f0', font=('Helvetica', 12))
        self.monthly_present_days_label.grid(row=3, column=0, padx=10, pady=10)
        
        self.monthly_present_days_entry = tk.Entry(self.window, font=('Helvetica', 12))
        self.monthly_present_days_entry.grid(row=3, column=1, padx=10, pady=10)
        

        self.leave_days_label = tk.Label(self.window, text="Leave Days:", bg='#f0f0f0', font=('Helvetica', 12))
        self.leave_days_label.grid(row=4, column=0, padx=10, pady=10)
        
        self.leave_days_entry = tk.Entry(self.window, font=('Helvetica', 12))
        self.leave_days_entry.grid(row=4, column=1, padx=10, pady=10)


        self.overtime_hours_label = tk.Label(self.window, text="Overtime Hours:", bg='#f0f0f0', font=('Helvetica', 12))
        self.overtime_hours_label.grid(row=5, column=0, padx=10, pady=10)
        
        self.overtime_hours_entry = tk.Entry(self.window, font=('Helvetica', 12))
        self.overtime_hours_entry.grid(row=5, column=1, padx=10, pady=10)
        

        self.button_add = tk.Button(self.window, text="Add Record", command=self.add_record, font=('Helvetica', 12, 'bold'), bg='#4CAF50', fg='white')
        self.button_add.grid(row=6, column=0, padx=10, pady=10)

        self.button_show = tk.Button(self.window, text="Delete", command=self.delete_emp, font=('Helvetica', 12, 'bold'), bg='#FF5733', fg='white')
        self.button_show.grid(row=6, column=1, padx=10, pady=10)
        
        self.button_back = tk.Button(self.window, text="Back", command=self.backit, font=('Helvetica', 12, 'bold'), bg='#3498DB', fg='white')
        self.button_back.grid(row=6, column=2, padx=10, pady=10)
        
        self.button_search = tk.Button(self.window, text="Search", command=self.search_employee, font=('Helvetica', 12, 'bold'), bg='#FFC300', fg='white')
        self.button_search.grid(row=0, column=2, padx=10, pady=10)


        self.tree = ttk.Treeview(self.window, columns=("Employee ID", "Employee Name", "Jobroll", "Monthly Present Days", "Overtime Hours", "Leave Days"), show="headings")
        self.tree.heading("Employee ID", text="Employee ID", anchor=tk.CENTER)
        self.tree.heading("Employee Name", text="Employee Name", anchor=tk.CENTER)
        self.tree.heading("Jobroll", text="Job Roll", anchor=tk.CENTER)
        self.tree.heading("Monthly Present Days", text="Monthly Present Days", anchor=tk.CENTER)
        self.tree.heading("Overtime Hours", text="Overtime Hours", anchor=tk.CENTER)
        self.tree.heading("Leave Days", text="Leave Days", anchor=tk.CENTER)
        self.tree.grid(row=7, column=0, columnspan=4, padx=10, pady=10, sticky=tk.W+tk.E)

    def connectall(self):
        try:
            self.cr.execute("SELECT * FROM attendance")
            rows = self.cr.fetchall()
            for record in self.tree.get_children():
                self.tree.delete(record)           
            for row in rows:
                self.tree.insert("", tk.END, values=row)
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"Error fetching records: {e}")



    def add_record(self):
        employee_id = self.employee_id_entry.get()
        employee_name = self.employee_name_entry.get()
        employee_position = self.employee_position_entry.get()
        monthly_present_days = self.monthly_present_days_entry.get()
        overtime_hours = self.overtime_hours_entry.get()
        leave_days = self.leave_days_entry.get()
        if not (employee_id and employee_name and employee_position and monthly_present_days and leave_days and overtime_hours):
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        try:
            monthly_present_days = int(monthly_present_days)
            leave_days = int(leave_days)
            overtime_hours = float(overtime_hours)
            if not (monthly_present_days + leave_days == 30):
                raise ValueError("Total days not matching.")
            if not (0 <= monthly_present_days <= 31):
                raise ValueError("Monthly Present Days must be between 0 and 31.")
            if not (0 <= leave_days <= 31):
                raise ValueError("Leave Days must be between 0 and 31.")
            if overtime_hours < 0:
                raise ValueError("Overtime Hours cannot be negative.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        try:

            check_query = "SELECT COUNT(*) FROM employeedetails WHERE employeeid = %s"
            self.cr.execute(check_query, (employee_id,))
            count = self.cr.fetchone()[0]
            if count == 0:
                messagebox.showerror("Error", f"There is no Employee with the Employee ID {employee_id}.")
                self.clear_entries()
                return
            query_name = "SELECT employeename FROM employeedetails WHERE employeeid = %s"
            self.cr.execute(query_name, (employee_id,))
            actual_name = self.cr.fetchone()[0]            
            if employee_name != actual_name:
                messagebox.showerror("Error", f"Employee name {employee_name} does not match the name in employeedetails.")
                self.clear_entries()
                return
            query_jobroll = "SELECT jobroll FROM employeedetails WHERE employeeid = %s"
            self.cr.execute(query_jobroll, (employee_id,))
            actual_jobroll = self.cr.fetchone()[0]            
            if employee_position != actual_jobroll:
                messagebox.showerror("Error", f"Jobroll {employee_position} does not match the jobroll in employeedetails.")
                self.clear_entries()
                return          
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"Error checking details: {e}")
            return
        try:

            sql = "INSERT INTO attendance(employeeid, employeename, jobroll, present, overtime, leavedays) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (employee_id, employee_name, employee_position, monthly_present_days, overtime_hours, leave_days)
            self.cr.execute(sql, values)
            self.con.commit()
            self.tree.insert("", tk.END, values=(employee_id, employee_name, employee_position, monthly_present_days, overtime_hours, leave_days))          
            messagebox.showinfo("Success", "Record added successfully.")
            self.clear_entries()
            
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"Error adding record: {e}")



    def delete_emp(self):
        selected_item = self.tree.selection()
        if selected_item:
            employee_id = self.tree.item(selected_item)['values'][0]
            try:
                delete_query = "DELETE FROM attendance WHERE EmployeeId= %s"
                self.cr.execute(delete_query, (employee_id,))
                self.con.commit()
                
                self.connectall()  
                
                messagebox.showinfo('Success', 'Employee deleted successfully!')
            except pymysql.Error as e:
                messagebox.showerror('Database Error', f'Error deleting employee: {e}')
        else:
            messagebox.showwarning('Selection Error', 'Please select an employee to delete')



    def backit(self):
        self.window.destroy()
        a2.Navpage()

    def clear_entries(self):
        self.employee_id_entry.delete(0, tk.END)
        self.employee_name_entry.delete(0, tk.END)
        self.employee_position_entry.delete(0, tk.END)
        self.monthly_present_days_entry.delete(0, tk.END)
        self.leave_days_entry.delete(0, tk.END)
        self.overtime_hours_entry.delete(0, tk.END)

    def search_employee(self):
        employee_id = self.employee_id_entry.get()     
        if not employee_id:
            messagebox.showerror("Error", "Please enter Employee ID to search.")
            return        
        try:
            sql = "SELECT employeename, jobroll FROM employeedetails WHERE employeeid = %s"
            self.cr.execute(sql, (employee_id,))
            result = self.cr.fetchone()            
            if result:
                employee_name, jobroll = result
                self.employee_name_entry.delete(0, tk.END)
                self.employee_position_entry.delete(0, tk.END)
                self.employee_name_entry.insert(0, employee_name)
                self.employee_position_entry.insert(0, jobroll)
            else:
                messagebox.showinfo("Search Result", f"No employee found with ID {employee_id}.")
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"Error searching employee: {e}")

    def start(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = EmployeeAttendanceApp()
    app.start()

