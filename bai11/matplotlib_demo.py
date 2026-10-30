import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("D:/Lap_Trinh_Phython/Lap_trinh_Phython_A/bai11/diem_sinh_vien.csv")
print("========== BAI TAP 3.1 ==========")
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()
print(diem_trung_binh_mon)
plt.figure(figsize=(6, 4))
plt.bar(
    diem_trung_binh_mon.index,
    diem_trung_binh_mon.values,
    color="skyblue"
)
plt.title("Diem trung binh theo mon hoc")
plt.xlabel("Mon hoc")
plt.ylabel("Diem trung binh")
plt.savefig("bieu_do_cot.png")
plt.show()

print("\n========== Bài tập 3.2 ==========")
lan_kiem_tra = [1, 2, 3]
diem_qua_cac_lan = [6.5, 7.5, 8.5]
plt.figure(figsize=(6, 4))
plt.plot(lan_kiem_tra, diem_qua_cac_lan,
         marker="o", color="green")
plt.title("Xu huong diem qua cac lan kiem tra")
plt.xlabel("Lan kiem tra")
plt.ylabel("Diem")
plt.savefig("bieu_do_duong.png")
plt.show()