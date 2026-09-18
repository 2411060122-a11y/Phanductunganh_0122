# Hoạt động 1: if, if-else, if-elif-else & điều kiện rút gọn
#Bài tập 1.1 - if đơn và if-else:
print("\n========== BÀI 1.1 ==========")

tuoi = 20
if tuoi >= 19:
    print("Da du tuoi truong thanh")
if tuoi >= 19:
    print("Duoc phep dang ky xe may")
else:
    print("Chua du tuoi")

#Bài tập 1.2 – if-elif-else:
print("\n========== BÀI 1.2 ==========")

diem = 9.2
if diem >= 8.0:
    print("Xep loai: Gioi")
elif diem >= 6.5:
    print("Xep loai: Kha")
elif diem >= 5.0:
    print("Xep loai: Trung binh")
else:
    print("Xep loai: Yeu")
       
#Bài tập 1.3 – Điều kiện lồng nhau:
print("\n========== BÀI 1.3 ==========")

tuoi = 18
co_giay_phep = False
if tuoi >= 19:
    if co_giay_phep:
        print("Duoc phep lai xe")
    else:
        print("Du tuoi nhung chua co giay phep")
else:
    print("Chua du tuoi lai xe")
    
#Bài tập 1.4 – #Biểu thức điều kiện rút gọn (conditional expression):
print("\n========== BÀI 1.4 ==========")

diem = 6
ket_qua = "Dat" if diem >= 5.0 else "Khong dat"
print(ket_qua)
so = -7
tri_tuyet_doi = so if so >= 0 else -so
print(tri_tuyet_doi)

#Hoạt động 2: Vận dụng if – Xếp loại học lực, tìm số lớn nhất
#Bài tập 2.1 – Xếp loại h ọc lực:
print("\n========== BÀI 2.1 ==========")

ho_ten = "Phan Duc Tung Anh"
diem_toan, diem_ly, diem_hoa = 8.0, 7.5, 6.0
dtb = round((diem_toan + diem_ly + diem_hoa) / 3, 2)
if dtb >= 8.0:
    xep_loai = "Gioi"
elif dtb >= 6.5:
    xep_loai = "Kha"
elif dtb >= 5.0:
    xep_loai = "Trung binh"
else:
    xep_loai = "Yeu"
print(f"{ho_ten} - DTB: {dtb} - Xep loai: {xep_loai}")

#Bài tập 2.2 – Tìm số lớn nhất:
print("\n========== BÀI 2.2 ==========")

a = float(input("Nhap so thu nhat: "))
b = float(input("Nhap so thu hai: "))
c = float(input("Nhap so thu ba: "))
if a >= b and a >= c:
    lon_nhat = a
elif b >= a and b >= c:
    lon_nhat = b
else:
    lon_nhat = c
print("So lon nhat la:", lon_nhat)