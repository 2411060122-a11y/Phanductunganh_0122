# Hoạt động 5:pass, break, continue
#Bài tập 5.1 – pass
print("\n========== BÀI 5.1 ==========")

diem = 7.5
if diem >= 8.0:
 pass # chua cai dat logic cho truong hop nay, se bo sung sau
elif diem >= 5.0:
 print("Dat yeu cau")
else:
    pass

# Bài tập 5.2 – break: Kiểm tra số nguyên tố:
print ("\n========== BÀI 5.2 ==========")
so = 86
la_so_nguyen_to = ("\nTrue")

if so < 2:
    la_so_nguyen_to = ("\nFalse")
else:
    for i in range(2, so):
        if so % i == 0:
            la_so_nguyen_to = ("\nFalse")
        break # thoat ngay khi tim thay uoc so, khong can kiem tra tiep
print(f"{so} \nco phai so nguyen to khong? {la_so_nguyen_to}")

#Bài tập 5.3 – break: Tìm số nguyên tố đầu tiên lớn hơn n:
print("\n========== BÀI 5.3 ==========")

n = 22
so_hien_tai = n + 1

while True:
    la_so_nguyen_to = True

    for i in range(2, so_hien_tai):
        if so_hien_tai % i == 0:
            la_so_nguyen_to = False
            break

    if la_so_nguyen_to:
        break

    so_hien_tai += 1

print(f"Số nguyên tố đầu tiên lớn hơn {n} là: {so_hien_tai}")
#Bài tập 5.4 – continue: Lọc phần tử hợp lệ trong danh sách:
print("\n========== BÀI 5.4 ==========")

danh_sach = [5, -3, 8, 0, -1, 12, 7, 9]
danh_sach_hop_le = []
for so in danh_sach:
    if so <= 0:
        continue # bo qua cac so khong duong, khong them vao danh sach ket qua
danh_sach_hop_le.append(so)
print("Cac so hop le (duong):", danh_sach_hop_le)

#Hoạt động 6: Vòng lặp lồng nhau – In hình bằng ký tự
#Bài tập 6.1 – Tam giác sao::
print("\n========== BÀI 6.1 ==========")
n = 8
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
print()

#Bài tập 6.2 – Hình thoi sao:
print("\n========== BÀI 6.2 ==========")

n = 12
# Nua tren cua hinh thoi
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
# Nua duoi cua hinh thoi
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))