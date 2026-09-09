# Hoạt động 5 - Mini project: Đăng ký thông tin cá nhân

# Nhập thông tin
ho_ten = input("Nhap ho ten: ")
sdt = input("Nhap so dien thoai: ")
email = input("Nhap email: ")

# Chuẩn hóa họ tên
ho_ten_chuan = " ".join(ho_ten.split()).title()

# Kiểm tra số điện thoại có đủ 10 ký tự
sdt_hop_le = len(sdt) == 10

# Kiểm tra email có chứa ký tự @
email_hop_le = "@" in email

# In kết quả
print(f"Ho ten (da chuan hoa): {ho_ten_chuan}")
print(f"So dien thoai hop le (du 10 ky tu)? {sdt_hop_le}")
print(f"Email hop le (co ky tu @)? {email_hop_le}")