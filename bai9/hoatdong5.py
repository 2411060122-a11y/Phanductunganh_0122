import tkinter as tk
 
cua_so = tk.Tk()
cua_so.title("Vi du bien dieu khien")
cua_so.geometry("350x260")
 
# ----- Cac bien dieu khien -----
bien_ho_ten = tk.StringVar(value="Nguyen Van A")
bien_tuoi = tk.IntVar(value=18)
bien_dong_y_dieu_khoan = tk.BooleanVar(value=False)
 
# ----- Dong 0: Ho ten -----
tk.Label(cua_so, text="Ho ten:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
tk.Entry(cua_so, textvariable=bien_ho_ten).grid(row=0, column=1, padx=10, pady=10)
 
# ----- Dong 1: Tuoi -----
tk.Label(cua_so, text="Tuoi:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
tk.Entry(cua_so, textvariable=bien_tuoi).grid(row=1, column=1, padx=10, pady=10)
 
# ----- Dong 2: Checkbutton -----
tk.Checkbutton(
    cua_so,
    text="Dong y dieu khoan",
    variable=bien_dong_y_dieu_khoan,
).grid(row=2, column=0, columnspan=2, pady=10)
 
# ----- Dong 3: Label dung CHUNG bien_ho_ten voi Entry o tren -----
# Go chu vao o "Ho ten" thi Label nay tu doi theo, khong can viet them code nao
tk.Label(cua_so, textvariable=bien_ho_ten, fg="blue").grid(row=3, column=0, columnspan=2)
 
 
def xem_gia_tri_bien():
    try:
        tuoi = bien_tuoi.get()
    except tk.TclError:  # nguoi dung go chu vao o Tuoi thay vi so nguyen
        print("Tuoi phai la so nguyen!")
        return
 
    print("Ho ten (StringVar):", bien_ho_ten.get())
    print("Tuoi (IntVar):", tuoi)
    print("Dong y dieu khoan (BooleanVar):", bien_dong_y_dieu_khoan.get())
 
    bien_tuoi.set(tuoi + 1)  # set() cap nhat gia tri, o Entry tu doi theo
 
 
# ----- Dong 4: Nut bam -----
tk.Button(
    cua_so,
    text="Xem gia tri bien (va +1 tuoi)",
    command=xem_gia_tri_bien,
).grid(row=4, column=0, columnspan=2, pady=10)
 
cua_so.mainloop()