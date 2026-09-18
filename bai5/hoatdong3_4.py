# Hoạt động 3: Vòng lặp for

print("========== FOR VOI RANGE() ==========")

for i in range(1, 11):
    print(i)

print("\n========== DUYET LIST ==========")

diem_so = [8.5, 7.0, 9.2, 7.5]
for diem in diem_so:
    print("Điểm:", diem)


print("\n========== DUYET TUPLE ==========")

toa_do = (6, 7)

for gia_tri in toa_do:
    print(gia_tri)


print("\n========== DUYET DICTIONARY ==========")

diem_mon = {
    "Toan": 9.0,
    "Ly": 8.5
}
for mon, diem in diem_mon.items():
    print(mon, "-", diem)


print("\n========== DUYET STRING ==========")

ten = "Tung Anh"

for ky_tu in ten:
    print(ky_tu)


print("\n========== BANG CUU CHUONG ==========")

n = 6
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

#Hoạt động 4: Vòng lặp while
#Bài tập 4.1 – Tính giai thừa của n:
print("\n========== BÀI 4.1 ==========")

n = 8
giai_thua = 1
i = 1
while i <= n:
    giai_thua = giai_thua * i
    i += 1
print(f"{n}! = {giai_thua}")

#Bài tập 4.2 – Tính tổng các chữ số của một số:
print("\n========== BÀI 4.2 ==========")
so = 6767
so_tam = so
tong_chu_so = 0
while so_tam > 0:
    chu_so = so_tam % 10
    tong_chu_so += chu_so
    so_tam = so_tam // 10
print(f"Tong cac chu so cua {so} la: {tong_chu_so}")