#Hoạt động 4: Phạm vi biến – local, global, từ khóa global
print("\n========== Hoạt động 4 ==========")

so_luot_truy_cap = 0  # biến global


def tang_luot_truy_cap():
    global so_luot_truy_cap
    so_luot_truy_cap += 1


def vi_du_bien_local():
    so_luot_truy_cap = 100  # đây là biến LOCAL
    print("Bên trong hàm, biến local =", so_luot_truy_cap)


tang_luot_truy_cap()
tang_luot_truy_cap()

print("So luot truy cap (global):", so_luot_truy_cap)

vi_du_bien_local()

print("Sau khi gọi ham, bien global la:", so_luot_truy_cap)

#Hoạt động 5: Hàm lambda kết hợp map(), filter(), sorted()
#Bài tập 5.1 – map() với lambda:
print("\n========== BÀI 5.1 ==========")

danh_sach_so = [11, 24, 36, 42, 55]
binh_phuong = list(map(lambda x: x ** 2, danh_sach_so))
print(binh_phuong)

#Bài tập 5.2 – filter() với lambda:
print("\n========== BÀI 5.2 ==========")

so_chan = list(filter(lambda x: x % 2 == 0, danh_sach_so))
print(so_chan)

#Bài tập 5.3 – sorted() với lambda:
print("\n========== BÀI 5.3 ==========")

danh_sach_sv = [
    {"ten": "Tung Anh", "diem": 8.5},
    {"ten": "Aly", "diem": 7.0},
    {"ten": "Huyen", "diem": 9.2}
]

# Sắp xếp theo điểm tăng dần
sap_xep_theo_diem = sorted(
    danh_sach_sv,
    key=lambda sv: sv["diem"]
)

# Sắp xếp theo điểm giảm dần
sap_xep_giam_dan = sorted(
    danh_sach_sv,
    key=lambda sv: sv["diem"],
    reverse=True
)

print("Sắp xếp theo điểm tăng dần:")
for sv in sap_xep_theo_diem:
    print(sv["ten"], "-", sv["diem"])

print("--- Giảm dần ---")
for sv in sap_xep_giam_dan:
    print(sv["ten"], "-", sv["diem"])