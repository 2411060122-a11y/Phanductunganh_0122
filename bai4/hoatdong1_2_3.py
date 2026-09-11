# hoatdong1
#bai1.1
sinh_vien = {
"ho_ten": "Phan Duc Tung Anh",
"nam_sinh": 2006,
"diem_tb": 8.5
}
print(sinh_vien["ho_ten"]) # truy xuat theo khoa
print(sinh_vien.get("diem_tb")) # truy xuat an toan bang get()
print(sinh_vien.get("lop", "Chua co")) # get() voi gia tri mac dinh neu khong co khoa
 
#bai1.2
# Khai báo sinh viên
sinh_vien = {
    "ho_ten": " phan duc tung anh",
    "nam_sinh": 2006,
    "diem_tb": 8.5
}

# Thêm khóa mới
sinh_vien["lop"] = "CNTT01"

# Sửa giá trị khóa đã có
sinh_vien["diem_tb"] = 9.0

print(sinh_vien)

# Xóa theo khóa, trả về giá trị vừa xóa
diem_cu = sinh_vien.pop("diem_tb")

print(sinh_vien, "- diem da xoa:", diem_cu)

# Cập nhật/thêm nhiều khóa cùng lúc
sinh_vien.update({
    "nam_sinh": 2006,
    "email": "phanductunganh@example.com"
})

print(sinh_vien)

# hoatdong2
diem_mon_hoc = {"Toan": 9.0, "Ly": 8.5, "Hoa": 7.5, "Van": 8.5}
for mon in diem_mon_hoc.keys():
    print(mon)
for diem in diem_mon_hoc.values():
    print(diem)
for mon, diem in diem_mon_hoc.items():
    print(f"{mon}: {diem}")
tong_diem = 0
for diem in diem_mon_hoc.values():
    tong_diem = tong_diem + diem
print("Diem trung binh:", round(tong_diem / len(diem_mon_hoc), 2))

#hoatdong3
#baitap3.1
diem_mon_hoc = {"Toan": 9.0, "Ly": 7.5, "Hoa": 8.4, "Van": 7.7}
diem_cong_diem = {mon: round(diem + 0.5, 2) for mon, diem in diem_mon_hoc.items()}
print(diem_cong_diem)
ten_mon_viet_hoa = {mon.upper(): diem for mon, diem in diem_mon_hoc.items()}
print(ten_mon_viet_hoa)

#baitap3.2
mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}

# Giao: môn học chung ở 2 học kỳ
print(mon_hoc_ky1 & mon_hoc_ky2)

# Hợp: tất cả môn học của cả 2 học kỳ
print(mon_hoc_ky1 | mon_hoc_ky2)

# Hiệu: môn chỉ có ở học kỳ 1
print(mon_hoc_ky1 - mon_hoc_ky2)



