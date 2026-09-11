quan_ly_diem = {
    "Phan Duc Tung Anh": [8.0, 7.5, 9.0],
    "Phan Duc Tung Duong": [6.0, 6.5, 5.5],
    "Le Van Minh": [9.0, 9.5, 8.5]
}

# Them sinh vien moi
quan_ly_diem["Nguyen Van A"] = [7.0, 8.0, 7.5]

# Sua diem mon dau tien cua mot sinh vien
quan_ly_diem["Phan Duc Tung Duong"][0] = 7.0

# Tao dictionary luu diem trung binh
diem_trung_binh = {}

# Tinh diem trung binh cho tung sinh vien
for ho_ten, danh_sach_diem in quan_ly_diem.items():
    diem_trung_binh[ho_ten] = round(
        sum(danh_sach_diem) / len(danh_sach_diem), 2
    )

# In bang diem trung binh
print("BANG DIEM TRUNG BINH:")

for ho_ten, dtb in diem_trung_binh.items():
    dat_loai_gioi = dtb >= 8.0
    print(f"{ho_ten:<20} - DTB: {dtb:<5} - Dat loai Gioi? {dat_loai_gioi}")