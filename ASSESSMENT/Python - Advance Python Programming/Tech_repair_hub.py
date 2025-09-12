"""
RepairMate - A simplified desktop Repair Management app
Features implemented:
- SQLite3 persistence for customers, devices, repair_orders
- Classes with inheritance (Person -> Customer)
- Device linking to customers (one-to-many)
- Repair order creation, assignment, status tracking
- Billing & invoice generation (saved as CSV)
- Basic Admin and Technician roles in Tkinter GUI
- Regex-based search for device models and order status
- File I/O (invoices CSV), exception handling, user-defined exceptions

How to run:
- Requires Python 3.x (tested on 3.8+)
- Run: python repairmate.py

This file is a compact but complete demonstration for module assessment.
"""

import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
import re
import csv
import os
from datetime import datetime

# ---------------------------
# Exceptions
# ---------------------------
class RepairMateError(Exception):
    """Base user-defined exception for RepairMate"""
    pass

class AccessDenied(RepairMateError):
    pass

class MissingFieldError(RepairMateError):
    pass

# ---------------------------
# Data Layer (SQLite)
# ---------------------------
DB_FILE = 'repairmate.db'
INVOICE_FOLDER = 'invoices'
os.makedirs(INVOICE_FOLDER, exist_ok=True)

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    # Customers
    cur.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT,
        email TEXT,
        address TEXT,
        created_at TEXT
    )
    ''')
    # Devices
    cur.execute('''
    CREATE TABLE IF NOT EXISTS devices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        model TEXT,
        serial TEXT,
        notes TEXT,
        created_at TEXT,
        FOREIGN KEY(customer_id) REFERENCES customers(id)
    )
    ''')
    # Repair Orders
    cur.execute('''
    CREATE TABLE IF NOT EXISTS repair_orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        device_id INTEGER,
        issue TEXT,
        assigned_to TEXT,
        status TEXT,
        parts_cost REAL DEFAULT 0,
        labor_cost REAL DEFAULT 0,
        tax_percent REAL DEFAULT 18.0,
        created_at TEXT,
        updated_at TEXT,
        FOREIGN KEY(device_id) REFERENCES devices(id)
    )
    ''')
    conn.commit()
    conn.close()

# ---------------------------
# OOP Domain
# ---------------------------
class Person:
    def __init__(self, name, phone=None, email=None):
        self.name = name
        self.phone = phone
        self.email = email

class Customer(Person):
    def __init__(self, name, phone=None, email=None, address=None, customer_id=None):
        super().__init__(name, phone, email)
        self.address = address
        self.id = customer_id

    def save(self):
        if not self.name:
            raise MissingFieldError("Customer name is required")
        conn = get_db_connection()
        cur = conn.cursor()
        now = datetime.utcnow().isoformat()
        if self.id is None:
            cur.execute('INSERT INTO customers (name,phone,email,address,created_at) VALUES (?,?,?,?,?)',
                        (self.name, self.phone, self.email, self.address, now))
            self.id = cur.lastrowid
        else:
            cur.execute('UPDATE customers SET name=?, phone=?, email=?, address=? WHERE id=?',
                        (self.name, self.phone, self.email, self.address, self.id))
        conn.commit()
        conn.close()
        return self.id

    @staticmethod
    def get(customer_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM customers WHERE id=?', (customer_id,))
        row = cur.fetchone()
        conn.close()
        if row:
            return Customer(row['name'], row['phone'], row['email'], row['address'], row['id'])
        return None

class Device:
    def __init__(self, customer_id, model, serial=None, notes=None, device_id=None):
        self.customer_id = customer_id
        self.model = model
        self.serial = serial
        self.notes = notes
        self.id = device_id

    def save(self):
        if not self.model:
            raise MissingFieldError("Device model required")
        conn = get_db_connection()
        cur = conn.cursor()
        now = datetime.utcnow().isoformat()
        if self.id is None:
            cur.execute('INSERT INTO devices (customer_id,model,serial,notes,created_at) VALUES (?,?,?,?,?)',
                        (self.customer_id, self.model, self.serial, self.notes, now))
            self.id = cur.lastrowid
        else:
            cur.execute('UPDATE devices SET model=?, serial=?, notes=? WHERE id=?',
                        (self.model, self.serial, self.notes, self.id))
        conn.commit()
        conn.close()
        return self.id

    @staticmethod
    def get(device_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM devices WHERE id=?', (device_id,))
        row = cur.fetchone()
        conn.close()
        if row:
            return Device(row['customer_id'], row['model'], row['serial'], row['notes'], row['id'])
        return None

class RepairOrder:
    VALID_STATUSES = ['Pending', 'In Progress', 'Completed', 'Cancelled']

    def __init__(self, device_id, issue, assigned_to=None, status='Pending', parts_cost=0.0, labor_cost=0.0, tax_percent=18.0, order_id=None):
        self.device_id = device_id
        self.issue = issue
        self.assigned_to = assigned_to
        self.status = status
        self.parts_cost = float(parts_cost)
        self.labor_cost = float(labor_cost)
        self.tax_percent = float(tax_percent)
        self.id = order_id

    def save(self):
        if not self.issue:
            raise MissingFieldError("Issue description is required")
        if self.status not in RepairOrder.VALID_STATUSES:
            raise RepairMateError(f"Invalid status: {self.status}")
        conn = get_db_connection()
        cur = conn.cursor()
        now = datetime.utcnow().isoformat()
        if self.id is None:
            cur.execute('''INSERT INTO repair_orders (device_id,issue,assigned_to,status,parts_cost,labor_cost,tax_percent,created_at,updated_at)
                           VALUES (?,?,?,?,?,?,?,?,?)''',
                        (self.device_id, self.issue, self.assigned_to, self.status, self.parts_cost, self.labor_cost, self.tax_percent, now, now))
            self.id = cur.lastrowid
        else:
            cur.execute('''UPDATE repair_orders SET issue=?, assigned_to=?, status=?, parts_cost=?, labor_cost=?, tax_percent=?, updated_at=? WHERE id=?''',
                        (self.issue, self.assigned_to, self.status, self.parts_cost, self.labor_cost, self.tax_percent, now, self.id))
        conn.commit()
        conn.close()
        return self.id

    def calculate_total(self):
        subtotal = self.parts_cost + self.labor_cost
        tax = subtotal * (self.tax_percent / 100.0)
        total = subtotal + tax
        return {'subtotal': subtotal, 'tax': tax, 'total': total}

    @staticmethod
    def list_for_customer(customer_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''SELECT ro.* FROM repair_orders ro JOIN devices d ON ro.device_id = d.id WHERE d.customer_id = ? ORDER BY ro.created_at DESC''', (customer_id,))
        rows = cur.fetchall()
        conn.close()
        return [dict(r) for r in rows]

# ---------------------------
# Utility Functions
# ---------------------------
def regex_search_orders(pattern, field='status'):
    """Search repair_orders for given regex pattern on 'status' or device model"""
    conn = get_db_connection()
    cur = conn.cursor()
    results = []
    if field == 'status':
        cur.execute('SELECT * FROM repair_orders')
        rows = cur.fetchall()
        for r in rows:
            if re.search(pattern, r['status'], re.IGNORECASE):
                results.append(dict(r))
    elif field == 'model':
        # join devices
        cur.execute('''SELECT ro.* , d.model FROM repair_orders ro JOIN devices d ON ro.device_id = d.id''')
        rows = cur.fetchall()
        for r in rows:
            if re.search(pattern, r['model'], re.IGNORECASE):
                results.append(dict(r))
    conn.close()
    return results

def save_invoice_csv(order_id, customer_name, device_model, breakdown):
    filename = f"invoice_{order_id}_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.csv"
    path = os.path.join(INVOICE_FOLDER, filename)
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['RepairMate Invoice'])
        writer.writerow(['Order ID', order_id])
        writer.writerow(['Customer', customer_name])
        writer.writerow(['Device', device_model])
        writer.writerow([])
        writer.writerow(['Subtotal', f"{breakdown['subtotal']:.2f}"])
        writer.writerow(['Tax', f"{breakdown['tax']:.2f}"])
        writer.writerow(['Total', f"{breakdown['total']:.2f}"])
    return path

# ---------------------------
# Simple Role-Based Access
# ---------------------------
USERS = {
    'admin': {'password': 'admin123', 'role': 'Admin'},
    'tech': {'password': 'tech123', 'role': 'Technician'}
}

# ---------------------------
# GUI
# ---------------------------
class RepairMateApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('RepairMate')
        self.geometry('900x600')
        self.resizable(False, False)
        # state
        self.current_user = None
        self.current_role = None

        # initialize db
        init_db()

        # Frames
        self.frames = {}
        for F in (LoginFrame, AdminDashboard, TechnicianDashboard):
            frame = F(self)
            self.frames[F.__name__] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame('LoginFrame')

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text='RepairMate Login', font=('Arial', 18)).pack(pady=10)
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        form = tk.Frame(self)
        form.pack(pady=20)
        tk.Label(form, text='Username').grid(row=0, column=0, sticky='e')
        tk.Entry(form, textvariable=self.username).grid(row=0, column=1)
        tk.Label(form, text='Password').grid(row=1, column=0, sticky='e')
        tk.Entry(form, textvariable=self.password, show='*').grid(row=1, column=1)
        tk.Button(self, text='Login', command=self.login).pack(pady=10)

    def login(self):
        user = self.username.get().strip()
        pwd = self.password.get().strip()
        try:
            if user not in USERS or USERS[user]['password'] != pwd:
                raise AccessDenied('Invalid credentials')
            self.master.current_user = user
            self.master.current_role = USERS[user]['role']
            if self.master.current_role == 'Admin':
                self.master.show_frame('AdminDashboard')
            else:
                self.master.show_frame('TechnicianDashboard')
        except AccessDenied as e:
            messagebox.showerror('Login Failed', str(e))

class AdminDashboard(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text='Admin Dashboard', font=('Arial', 16)).pack(pady=6)
        # Tabs
        tabs = ttk.Notebook(self)
        tabs.pack(fill='both', expand=True)
        self.customer_tab = CustomerTab(tabs)
        self.device_tab = DeviceTab(tabs)
        self.order_tab = OrderTab(tabs)
        self.report_tab = ReportTab(tabs)
        tabs.add(self.customer_tab, text='Customers')
        tabs.add(self.device_tab, text='Devices')
        tabs.add(self.order_tab, text='Repair Orders')
        tabs.add(self.report_tab, text='Reports (Regex)')
        tk.Button(self, text='Logout', command=lambda: master.show_frame('LoginFrame')).pack(pady=4)

class TechnicianDashboard(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text='Technician Dashboard', font=('Arial', 16)).pack(pady=6)
        tabs = ttk.Notebook(self)
        tabs.pack(fill='both', expand=True)
        self.order_tab = OrderTab(tabs, tech_mode=True)
        self.report_tab = ReportTab(tabs)
        tabs.add(self.order_tab, text='Repair Orders')
        tabs.add(self.report_tab, text='Reports (Regex)')
        tk.Button(self, text='Logout', command=lambda: master.show_frame('LoginFrame')).pack(pady=4)

# ---------------------------
# Tabs/Widgets
# ---------------------------
class CustomerTab(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # Left: form, Right: list
        left = tk.Frame(self)
        left.pack(side='left', fill='y', padx=10, pady=10)
        right = tk.Frame(self)
        right.pack(side='right', fill='both', expand=True, padx=10, pady=10)
        tk.Label(left, text='Add / Update Customer', font=('Arial', 12)).pack()
        self.name = tk.StringVar()
        self.phone = tk.StringVar()
        self.email = tk.StringVar()
        self.address = tk.StringVar()
        tk.Label(left, text='Name').pack(anchor='w')
        tk.Entry(left, textvariable=self.name).pack(fill='x')
        tk.Label(left, text='Phone').pack(anchor='w')
        tk.Entry(left, textvariable=self.phone).pack(fill='x')
        tk.Label(left, text='Email').pack(anchor='w')
        tk.Entry(left, textvariable=self.email).pack(fill='x')
        tk.Label(left, text='Address').pack(anchor='w')
        tk.Entry(left, textvariable=self.address).pack(fill='x')
        tk.Button(left, text='Save Customer', command=self.save_customer).pack(pady=6)

        # Right: list
        tk.Label(right, text='Customers', font=('Arial', 12)).pack()
        cols = ('id', 'name', 'phone', 'email')
        self.tree = ttk.Treeview(right, columns=cols, show='headings')
        for c in cols:
            self.tree.heading(c, text=c.title())
        self.tree.pack(fill='both', expand=True)
        tk.Button(right, text='Refresh', command=self.load_customers).pack(pady=4)
        self.load_customers()

    def save_customer(self):
        try:
            c = Customer(self.name.get().strip(), self.phone.get().strip(), self.email.get().strip(), self.address.get().strip())
            cid = c.save()
            messagebox.showinfo('Saved', f'Customer saved with id {cid}')
            self.load_customers()
        except RepairMateError as e:
            messagebox.showerror('Error', str(e))

    def load_customers(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT id,name,phone,email FROM customers ORDER BY id DESC')
        rows = cur.fetchall()
        conn.close()
        for r in rows:
            self.tree.insert('', 'end', values=(r['id'], r['name'], r['phone'], r['email']))

class DeviceTab(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        left = tk.Frame(self)
        left.pack(side='left', fill='y', padx=10, pady=10)
        right = tk.Frame(self)
        right.pack(side='right', fill='both', expand=True, padx=10, pady=10)
        tk.Label(left, text='Add Device', font=('Arial', 12)).pack()
        self.customer_id = tk.StringVar()
        self.model = tk.StringVar()
        self.serial = tk.StringVar()
        self.notes = tk.StringVar()
        tk.Label(left, text='Customer ID').pack(anchor='w')
        tk.Entry(left, textvariable=self.customer_id).pack(fill='x')
        tk.Label(left, text='Model').pack(anchor='w')
        tk.Entry(left, textvariable=self.model).pack(fill='x')
        tk.Label(left, text='Serial').pack(anchor='w')
        tk.Entry(left, textvariable=self.serial).pack(fill='x')
        tk.Label(left, text='Notes').pack(anchor='w')
        tk.Entry(left, textvariable=self.notes).pack(fill='x')
        tk.Button(left, text='Save Device', command=self.save_device).pack(pady=6)
        tk.Button(left, text='Load Devices for Customer', command=self.load_by_customer).pack(pady=2)

        tk.Label(right, text='Devices', font=('Arial', 12)).pack()
        cols = ('id', 'customer_id', 'model', 'serial')
        self.tree = ttk.Treeview(right, columns=cols, show='headings')
        for c in cols:
            self.tree.heading(c, text=c.title())
        self.tree.pack(fill='both', expand=True)

    def save_device(self):
        try:
            cid = int(self.customer_id.get())
            d = Device(cid, self.model.get().strip(), self.serial.get().strip(), self.notes.get().strip())
            did = d.save()
            messagebox.showinfo('Saved', f'Device saved with id {did}')
            self.load_by_customer()
        except ValueError:
            messagebox.showerror('Error', 'Customer ID must be an integer')
        except RepairMateError as e:
            messagebox.showerror('Error', str(e))

    def load_by_customer(self):
        try:
            cid = int(self.customer_id.get())
        except ValueError:
            messagebox.showerror('Error', 'Customer ID must be an integer')
            return
        for row in self.tree.get_children():
            self.tree.delete(row)
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT id, customer_id, model, serial FROM devices WHERE customer_id=? ORDER BY id DESC', (cid,))
        rows = cur.fetchall()
        conn.close()
        for r in rows:
            self.tree.insert('', 'end', values=(r['id'], r['customer_id'], r['model'], r['serial']))

class OrderTab(tk.Frame):
    def __init__(self, master, tech_mode=False):
        super().__init__(master)
        self.tech_mode = tech_mode
        left = tk.Frame(self)
        left.pack(side='left', fill='y', padx=10, pady=10)
        right = tk.Frame(self)
        right.pack(side='right', fill='both', expand=True, padx=10, pady=10)
        tk.Label(left, text='Create / Update Repair Order', font=('Arial', 12)).pack()
        self.device_id = tk.StringVar()
        self.issue = tk.StringVar()
        self.assigned_to = tk.StringVar()
        self.status = tk.StringVar(value='Pending')
        self.parts_cost = tk.StringVar(value='0')
        self.labor_cost = tk.StringVar(value='0')
        tk.Label(left, text='Device ID').pack(anchor='w')
        tk.Entry(left, textvariable=self.device_id).pack(fill='x')
        tk.Label(left, text='Issue').pack(anchor='w')
        tk.Entry(left, textvariable=self.issue).pack(fill='x')
        tk.Label(left, text='Assign To').pack(anchor='w')
        tk.Entry(left, textvariable=self.assigned_to).pack(fill='x')
        tk.Label(left, text='Status').pack(anchor='w')
        ttk.Combobox(left, textvariable=self.status, values=RepairOrder.VALID_STATUSES).pack(fill='x')
        tk.Label(left, text='Parts Cost').pack(anchor='w')
        tk.Entry(left, textvariable=self.parts_cost).pack(fill='x')
        tk.Label(left, text='Labor Cost').pack(anchor='w')
        tk.Entry(left, textvariable=self.labor_cost).pack(fill='x')
        tk.Button(left, text='Save Order', command=self.save_order).pack(pady=6)
        tk.Button(left, text='Calculate & Save Invoice', command=self.invoice_order).pack(pady=4)

        tk.Label(right, text='Repair Orders', font=('Arial', 12)).pack()
        cols = ('id','device_id','issue','assigned_to','status')
        self.tree = ttk.Treeview(right, columns=cols, show='headings')
        for c in cols:
            self.tree.heading(c, text=c.title())
        self.tree.pack(fill='both', expand=True)
        tk.Button(right, text='Refresh', command=self.load_orders).pack(pady=4)
        self.load_orders()

    def save_order(self):
        try:
            did = int(self.device_id.get())
            ro = RepairOrder(did, self.issue.get().strip(), self.assigned_to.get().strip(), self.status.get().strip(), float(self.parts_cost.get() or 0), float(self.labor_cost.get() or 0))
            oid = ro.save()
            messagebox.showinfo('Saved', f'Order saved with id {oid}')
            self.load_orders()
        except ValueError:
            messagebox.showerror('Error', 'Device ID, parts and labor cost must be numeric')
        except RepairMateError as e:
            messagebox.showerror('Error', str(e))

    def invoice_order(self):
        try:
            selected = self.tree.selection()
            if not selected:
                raise MissingFieldError('Select an order from list to invoice')
            oid = int(self.tree.item(selected[0])['values'][0])
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('SELECT ro.*, d.model, c.name as customer_name FROM repair_orders ro JOIN devices d ON ro.device_id=d.id JOIN customers c ON d.customer_id=c.id WHERE ro.id=?', (oid,))
            row = cur.fetchone()
            conn.close()
            if not row:
                raise RepairMateError('Order not found')
            ro = RepairOrder(row['device_id'], row['issue'], row['assigned_to'], row['status'], row['parts_cost'], row['labor_cost'], row['tax_percent'], row['id'])
            breakdown = ro.calculate_total()
            path = save_invoice_csv(ro.id, row['customer_name'], row['model'], breakdown)
            messagebox.showinfo('Invoice Saved', f'Invoice CSV saved to {path}')
        except RepairMateError as e:
            messagebox.showerror('Error', str(e))

    def load_orders(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT id, device_id, issue, assigned_to, status FROM repair_orders ORDER BY created_at DESC')
        rows = cur.fetchall()
        conn.close()
        for r in rows:
            self.tree.insert('', 'end', values=(r['id'], r['device_id'], r['issue'], r['assigned_to'], r['status']))

class ReportTab(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text='Regex Search / Reports', font=('Arial', 12)).pack(pady=6)
        frm = tk.Frame(self)
        frm.pack(pady=4)
        self.pattern = tk.StringVar()
        self.field = tk.StringVar(value='status')
        tk.Entry(frm, textvariable=self.pattern, width=40).grid(row=0, column=0, padx=4)
        ttk.Combobox(frm, textvariable=self.field, values=['status','model']).grid(row=0, column=1, padx=4)
        tk.Button(frm, text='Search', command=self.do_search).grid(row=0, column=2, padx=4)
        cols = ('id','device_id','issue','assigned_to','status')
        self.tree = ttk.Treeview(self, columns=cols, show='headings')
        for c in cols:
            self.tree.heading(c, text=c.title())
        self.tree.pack(fill='both', expand=True, padx=10, pady=10)

    def do_search(self):
        pat = self.pattern.get().strip()
        field = self.field.get()
        if not pat:
            messagebox.showerror('Error', 'Enter a regex pattern')
            return
        try:
            results = regex_search_orders(pat, field=field)
            for row in self.tree.get_children():
                self.tree.delete(row)
            for r in results:
                self.tree.insert('', 'end', values=(r['id'], r['device_id'], r['issue'], r['assigned_to'], r['status']))
        except re.error as e:
            messagebox.showerror('Regex Error', str(e))

# ---------------------------
# Run
# ---------------------------
if __name__ == '__main__':
    app = RepairMateApp()
    app.mainloop()
