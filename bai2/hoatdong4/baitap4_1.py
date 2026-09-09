cau = "Lap trinh Python rat thu vi"

print(cau[0])        # ky tu dau tien
print(cau[-1])       # ky tu cuoi cung
print(cau[4:10])     # cat tu vi tri 4 den truoc vi tri 10
print(cau[8:])       # tu dau den vi tri 8
print(cau[11:])      # tu vi tri 11 den het
print(cau[::-1])     # dao nguoc chuoi

# Kiem tra cau co phai la palindrome khong
if cau == cau[::-1]:
    print("cau la palindrome")
else:
    print("cau khong phai la palindrome")