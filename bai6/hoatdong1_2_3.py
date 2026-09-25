#Hoạt động 1: Hàm cơ bản – def, tham số, return
#Bài tập 1.1 – Viết hàm và gọi lại nhiều lần: Viết các hàm sau, mỗi hàm gọi thử với ít nhất 3 bộ dữ liệu khác nhau:
print("\n========== BÀI 1.1 ==========")

def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bscnn(a, b):
    return a * b // uscln(a, b)

def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n

print(uscln(44, 66))
print(bscnn(4, 6))

print(kiem_tra_nguyen_to(29))
print(kiem_tra_so_hoan_thien(28)) # 28 = 1 + 2 + 4 + 7 + 14

#Bài tập 1.2 – return không giá trị và trả về nhiều giá trị:
print("\n========== BÀI 1.2 ==========")

def in_loi_chao(ten):
    print(f"Xin chao, {ten}!")
    return # ham khong tra ve gia tri (tra ve None)

def chia_lay_thuong_du(a, b):
    return a // b, a % b # tra ve nhieu gia tri qua tuple

in_loi_chao("Phan Duc Tung Anh")
thuong, du = chia_lay_thuong_du(36, 5)
print(f"Thuong: {thuong}, du: {du}")

#Hoạt động 2: Tham số mặc định & tham số từ khóa
print ("\n========== hoạt động 2 ==========")

def gioi_thieu(ten, tuoi=18, lop="Chua ro"):
    print(f"Ten: {ten} - Tuoi: {tuoi} - Lop: {lop}")


# 1. Dùng giá trị mặc định
gioi_thieu("Tung Anh")

# 2. Ghi đè giá trị mặc định của tuoi
gioi_thieu("Aly", 200)

# 3. Truyền tham số từ khóa lop
gioi_thieu("Huyen", lop="CNTT10")

# 4. Truyền tham số từ khóa
gioi_thieu(ten="Khang", lop="CNTT20", tuoi=100)

#Hoạt động 3: Tham số linh hoạt – *args và **kwargs
#Bài tập 3.1 – *args: tính tổng số lượng bất kỳ các số:
print("\n========== BÀI 3.1 ==========")

def tinh_tong(*args):
    tong = 0
    for so in args:
        tong += so
    return tong

print(tinh_tong(15, 23, 36))
print(tinh_tong(51, 12, 15, 29, 24))
print(tinh_tong()) # khong truyen so nao -> tra ve 0

#Bài tập 3.2 – **kwargs: in thông tin động:
print("\n========== BÀI 3.2 ==========")

def in_thong_tin(ho_ten, tuoi, **kwargs):

    print(f"Ho ten: {ho_ten} - Tuoi: {tuoi}")
    for khoa, gia_tri in kwargs.items():
        print(f" {khoa}: {gia_tri}")

in_thong_tin("Phan Duc Tung Anh ", 20, lop="DH14C1", que_quan="Ha Noi")
in_thong_tin("Vu Hoang Aly", 18, email="vuhoangaly@gmail.com")

