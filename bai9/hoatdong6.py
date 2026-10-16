import tkinter as tk
from tkinter import messagebox
 
 
def xu_ly_submit():
    ho_ten = entry_ho_ten.get().strip()
    tuoi_nhap = entry_tuoi.get().strip()
    email = entry_email.get().strip()
 
    # 1. Kiem tra ho ten
    if ho_ten == "":
        messagebox.showerror("Loi", "Ho ten khong duoc de trong.")
        return
 
    # 2. Kiem tra tuoi (try-except tu Buoi 7)
    try:
        tuoi = int(tuoi_nhap)
    except ValueError:
        messagebox.showerror("Loi", "Tuoi phai la mot so nguyen.")
        return
 
    if tuoi <= 0 or tuoi > 120:  # khong bat buoc, xoa neu de bai khong yeu cau
        messagebox.showerror("Loi", "Tuoi phai nam trong khoang 1 den 120.")
        return
 
    # 3. Kiem tra email
    if "@" not in email:
        messagebox.showerror("Loi", "Email khong hop le (thieu ky tu @).")
        return
 
    # 4. Du lieu hop le
    messagebox.showinfo(
        "Thanh cong",
        f"Da nhan thong tin: {ho_ten} - {tuoi} tuoi - {email}",
    )
 
 
cua_so = tk.Tk()
cua_so.title("Form co validate")
cua_so.geometry("380x220")
 
# Dong 0: Ho ten
tk.Label(cua_so, text="Ho ten:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_ho_ten = tk.Entry(cua_so, width=25)
entry_ho_ten.grid(row=0, column=1, padx=10, pady=10)
 
# Dong 1: Tuoi
tk.Label(cua_so, text="Tuoi:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_tuoi = tk.Entry(cua_so, width=25)
entry_tuoi.grid(row=1, column=1, padx=10, pady=10)
 
# Dong 2: Email
tk.Label(cua_so, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_email = tk.Entry(cua_so, width=25)
entry_email.grid(row=2, column=1, padx=10, pady=10)
 
# Dong 3: Nut Submit
tk.Button(cua_so, text="Submit", command=xu_ly_submit).grid(
    row=3, column=0, columnspan=2, pady=15
)
 
cua_so.mainloop()