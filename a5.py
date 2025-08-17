import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
from tkcalendar import DateEntry  
from datetime import datetime

class SalaryManagementApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Salary Management")

        self.create_widgets()
        self.root.configure(bg='#34495e')
  
        self.con = pymysql.connect(user='root', password='rajesh@2006', host='localhost', database='project', port=3306)
        self.cr = self.con.cursor()
        self.connectall()
        
    def create_widgets(self):
        self.employee_id_label = tk.Label(self.root, text="Employee ID:", font=('Helvetica', 12))
        self.employee_id_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.employee_id_entry = tk.Entry(self.root, font=('Helvetica', 12))
        self.employee_id_entry.grid(row=0, column=1, padx=10, pady=10)

        self.employee_name_label = tk.Label(self.root, text="Employee Name:", font=('Helvetica', 12))
        self.employee_name_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.employee_name_entry = tk.Entry(self.root, font=('Helvetica', 12))
        self.employee_name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.button_delete = tk.Button(self.root, text="Delete Record", command=self.delete_record, font=('Helvetica', 12, 'bold'), bg='#FF5733', fg='white')
        self.button_delete.grid(row=9, column=1, padx=10, pady=10)

        self.button_delete = tk.Button(self.root, text="Back", command=self.back_it, font=('Helvetica', 12, 'bold'), bg='brown', fg='white')
        self.button_delete.grid(row=9, column=2, padx=10, pady=10)

        self.monthly_present_days_label = tk.Label(self.root, text="Monthly Present Days:", font=('Helvetica', 12))
        self.monthly_present_days_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.monthly_present_days_entry = tk.Entry(self.root, font=('Helvetica', 12))
        self.monthly_present_days_entry.grid(row=2, column=1, padx=10, pady=10)

        self.leave_days_label = tk.Label(self.root, text="Leave Days:", font=('Helvetica', 12))
        self.leave_days_label.grid(row=3, column=0, padx=10, pady=10)
        
        self.leave_days_entry = tk.Entry(self.root, font=('Helvetica', 12))
        self.leave_days_entry.grid(row=3, column=1, padx=10, pady=10)

        self.overtime_hours_label = tk.Label(self.root, text="Overtime Hours:", font=('Helvetica', 12))
        self.overtime_hours_label.grid(row=4, column=0, padx=10, pady=10)
        
        self.overtime_hours_entry = tk.Entry(self.root, font=('Helvetica', 12))
        self.overtime_hours_entry.grid(row=4, column=1, padx=10, pady=10)

        self.basic_pay_label = tk.Label(self.root, text="Basic Pay (Monthly):", font=('Helvetica', 12))
        self.basic_pay_label.grid(row=5, column=0, padx=10, pady=10)
        
        self.basic_pay_entry = tk.Entry(self.root, font=('Helvetica', 12))
        self.basic_pay_entry.grid(row=5, column=1, padx=10, pady=10)
        self.basic_pay_entry.insert(0, "30000")

        self.reduction_label = tk.Label(self.root, text="Reduction:", font=('Helvetica', 12))
        self.reduction_label.grid(row=6, column=0, padx=10, pady=10)
        
        self.reduction_entry = tk.Entry(self.root, font=('Helvetica', 12))
        self.reduction_entry.grid(row=6, column=1, padx=10, pady=10)

        self.total_salary_label = tk.Label(self.root, text="Total Salary:", font=('Helvetica', 12))
        self.total_salary_label.grid(row=7, column=0, padx=10, pady=10)
        
        self.total_salary_entry = tk.Entry(self.root, font=('Helvetica', 12))
        self.total_salary_entry.grid(row=7, column=1, padx=10, pady=10)

        self.issue_date_label = tk.Label(self.root, text="Issue Date (YYYY-MM-DD):", font=('Helvetica', 12))
        self.issue_date_label.grid(row=8, column=0, padx=10, pady=10)
        
        self.issue_date_entry = DateEntry(self.root, font=('Helvetica', 12), date_pattern='yyyy-mm-dd')
        self.issue_date_entry.grid(row=8, column=1, padx=10, pady=10)

        self.button_fetch = tk.Button(self.root, text="Fetch Details", command=self.fetch_employee_details, font=('Helvetica', 12))
        self.button_fetch.grid(row=0, column=2, padx=10, pady=10)

        self.button_calculate = tk.Button(self.root, text="Calculate Salary", command=self.calculate_salary, font=('Helvetica', 12, 'bold'), bg='#4CAF50', fg='white')
        self.button_calculate.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

        self.tree = ttk.Treeview(self.root, columns=("Employee ID", "Employee Name", "Basic Pay (Monthly)", "Reduction", "Total Salary", "Issue Date"), show="headings")
        self.tree.heading("Employee ID", text="Employee ID")
        self.tree.heading("Employee Name", text="Employee Name")
        self.tree.heading("Basic Pay (Monthly)", text="Basic Pay (Monthly)")
        self.tree.heading("Reduction", text="Reduction")
        self.tree.heading("Total Salary", text="Total Salary")
        self.tree.heading("Issue Date", text="Issue Date")
        self.tree.grid(row=10, column=0, columnspan=3, padx=10, pady=10)

    def connectall(self):
        try:
            self.cr.execute("SELECT * FROM salary")
            rows = self.cr.fetchall()
            for record in self.tree.get_children():
                self.tree.delete(record)
            for row in rows:
                self.tree.insert("", tk.END, values=row)
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"Error fetching records: {e}")

    def fetch_employee_details(self):
        employee_id = self.employee_id_entry.get()
        if not employee_id:
            messagebox.showerror("Error", "Please enter Employee ID.")
            return
        
        try:
            self.cr.execute("SELECT * FROM attendance WHERE EmployeeId=%s", (employee_id,))
            attendance_data = self.cr.fetchone()
            if attendance_data:
                self.employee_name_entry.delete(0, tk.END)
                self.employee_name_entry.insert(0, attendance_data[1])
                self.monthly_present_days_entry.delete(0, tk.END)
                self.monthly_present_days_entry.insert(0, attendance_data[3])
                self.leave_days_entry.delete(0, tk.END)
                self.leave_days_entry.insert(0, attendance_data[5])
                self.overtime_hours_entry.delete(0, tk.END)
                self.overtime_hours_entry.insert(0, attendance_data[4])
            else:
                messagebox.showerror("Error", f"No attendance record found for Employee ID {employee_id}.")
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"Error fetching attendance data: {e}")

    def calculate_salary(self):
        try:
            employee_id = self.employee_id_entry.get()
            employee_name = self.employee_name_entry.get()
            monthly_present_days = int(self.monthly_present_days_entry.get())
            leave_days = int(self.leave_days_entry.get())
            overtime_hours = float(self.overtime_hours_entry.get())
            basic_pay_monthly = float(self.basic_pay_entry.get())
            oneday = basic_pay_monthly / 30

            try:
                self.cr.execute("SELECT COUNT(*) FROM attendance WHERE EmployeeId=%s", (employee_id,))
                count = self.cr.fetchone()[0]

                if count == 0:
                    messagebox.showerror("Error", f"There is no Employee with the employee ID of {employee_id} ")
                    self.clear_data()
                    return
                
                query_name = "SELECT employeename FROM employeedetails WHERE employeeid = %s"
                self.cr.execute(query_name, (employee_id,))
                actual_name = self.cr.fetchone()[0]
                
                if employee_name != actual_name:
                    messagebox.showerror("Error", f"Employee name {employee_name} does not match the name in employeedetails.")
                    return
            except pymysql.Error as e:
                messagebox.showerror("Database Error", f"Error adding record: {e}")

            try:       
                salary_amount = basic_pay_monthly
                overtime_pay = round(overtime_hours * (oneday / 8))
                reduction_amount = leave_days * oneday
                total_salary = salary_amount - reduction_amount + overtime_pay

                self.cr.execute("SELECT * FROM salary WHERE employeeid = %s", (employee_id,))
                if self.cr.fetchone() is None:
                    issue_date = self.issue_date_entry.get()
                    self.cr.execute("INSERT INTO salary (employeeid, employeename, basicpay, reduction, totalsalary, issuedate) "
                                    "VALUES (%s, %s, %s, %s, %s, %s)", 
                                    (employee_id, employee_name, basic_pay_monthly, reduction_amount, total_salary, issue_date))
                    self.con.commit()
                    messagebox.showinfo("Success", "Salary details added successfully.")
                else:
                    messagebox.showinfo("Success", "Employee salary already calculated.")
            except pymysql.Error as e:
                messagebox.showerror("Error", f"Error calculating salary: {e}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical values.")

    def back_it(self):
        self.root.quit()
        
    def delete_record(self):
        pass


if __name__ == "__main__":
    app = SalaryManagementApp()
    app.root.mainloop()
