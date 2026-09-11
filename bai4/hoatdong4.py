#baitap4.1
chuoi_so = "25"
so = int(chuoi_so)
print(so, type(so))
so_thuc = float("3.14")
print(so_thuc, type(so_thuc))

 # tuple -> list
danh_sach = list((1, 2, 3))

# list -> tuple
bo_ba = tuple([4, 5, 6]) 

 # list -> set (tu loai bo trung lap)
tap_hop = set([1, 2, 2, 3, 3, 3])

# list cac tuple -> dict
tu_dien = dict([("a", 1), ("b", 2)]) 
print(danh_sach, bo_ba, tap_hop, tu_dien)

#baitap4.2
 #int("abc") -> quan sat loi ValueError
# int("3.14") -> quan sat loi ValueError (phai qua float() truoc)
so_hop_le = int(float("3.14")) # cach lam dung: ep qua float truoc
print(so_hop_le)

#baitap4.3
ket_qua = 5 + 3.5       # int + float -> Python tự động chuyển thành float
print(ket_qua, type(ket_qua))

ket_qua_2 = "Diem: " + str(9.0)   # phải ép str() tường minh
print(ket_qua_2)