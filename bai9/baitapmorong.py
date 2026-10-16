import re
import tkinter as tk
from tkinter import messagebox

TOAN_TU = "+-*/"


def dinh_dang_so(so):
    """Bo '.0' neu ket qua la so nguyen (5.0 -> 5), lam tron de tranh loi so thuc."""
    if so == int(so):
        return str(int(so))
    return str(round(so, 10))


def xoa_man_hinh():
    bien_man_hinh.set("")
    bien_vua_tinh_xong.set(False)


def bam_phim(ky_tu):
    bieu_thuc = bien_man_hinh.get()

    # Sau khi bam "=": go so moi -> bat dau lai; go toan tu -> tinh tiep tren ket qua
    if bien_vua_tinh_xong.get():
        if ky_tu not in TOAN_TU:
            bieu_thuc = ""
        bien_vua_tinh_xong.set(False)

    if ky_tu in TOAN_TU:
        if bieu_thuc == "":
            return  # khong cho bat dau bang toan tu
        if bieu_thuc[-1] in TOAN_TU:
            bieu_thuc = bieu_thuc[:-1]  # bam 2 toan tu lien tiep -> thay toan tu cu

    bien_man_hinh.set(bieu_thuc + ky_tu)


def tinh_ket_qua():
    bieu_thuc = bien_man_hinh.get()
    if bieu_thuc == "":
        return

    # Doi moi so thanh float de tranh loi SyntaxError voi so bat dau bang 0 (vd "08")
    bieu_thuc_chuan = re.sub(
        r"\d+\.?\d*|\.\d+", lambda m: str(float(m.group())), bieu_thuc
    )

    try:
        # eval an toan o day vi chuoi chi duoc tao tu cac nut bam (0-9 . + - * /)
        ket_qua = eval(bieu_thuc_chuan)
        bien_man_hinh.set(dinh_dang_so(ket_qua))
        bien_vua_tinh_xong.set(True)
    except ZeroDivisionError:
        messagebox.showerror("Loi", "Khong the chia cho 0.")
        xoa_man_hinh()
    except (SyntaxError, OverflowError, NameError):  # NameError: so qua lon -> "inf"
        messagebox.showerror("Loi", "Bieu thuc khong hop le.")
        xoa_man_hinh()


# ----- Giao dien -----
cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("300x400")
cua_so.resizable(False, False)

bien_man_hinh = tk.StringVar(value="")
bien_vua_tinh_xong = tk.BooleanVar(value=False)

# Dong 0: Man hinh hien thi (Label gan voi StringVar)
tk.Label(
    cua_so,
    textvariable=bien_man_hinh,
    font=("Arial", 22),
    anchor="e",
    bg="white",
    relief="sunken",
    bd=2,
    height=2,
).grid(row=0, column=0, columnspan=4, padx=6, pady=8, sticky="nsew")

# Dong 1-4: Ban phim so va toan tu
phim = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]

for chi_so_hang, hang in enumerate(phim, start=1):
    for chi_so_cot, ky_tu in enumerate(hang):
        if ky_tu == "=":
            lenh = tinh_ket_qua
        else:
            lenh = lambda k=ky_tu: bam_phim(k)  # k=ky_tu de "chot" gia tri cua tung nut

        tk.Button(cua_so, text=ky_tu, font=("Arial", 16), command=lenh).grid(
            row=chi_so_hang, column=chi_so_cot, padx=6, pady=4, sticky="nsew"
        )

# Dong 5: Nut xoa
tk.Button(cua_so, text="C", font=("Arial", 16), command=xoa_man_hinh).grid(
    row=5, column=0, columnspan=4, padx=6, pady=4, sticky="nsew"
)

# Cho cac cot/hang gian deu de nut co kich thuoc bang nhau
for c in range(4):
    cua_so.grid_columnconfigure(c, weight=1)
for r in range(1, 6):
    cua_so.grid_rowconfigure(r, weight=1)

cua_so.mainloop()