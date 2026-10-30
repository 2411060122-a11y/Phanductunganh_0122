# Bài tập 2.1 - Đọc CSV & xem tổng quan
import pandas as pd
import os
print("===========Bài tập 2.1===========")
thu_muc = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv("D:/Lap_Trinh_Phython/Lap_trinh_Phython_A/bai11/diem_sinh_vien.csv")
print(df.head())
print(df.shape)
print(df.columns.tolist())

#Bài 2.2 – Thống kê theo môn học
print("\n========== Bài tập 2.2 ==========")
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()
print(diem_trung_binh_mon)
print("Diem trung binh toan bo:", df["diem"].mean())
print("Diem cao nhat:", df["diem"].max())
print("Diem thap nhat:", df["diem"].min())

#Bài 2.3 – Tính điểm trung bình từng sinh viên và lọc đạt/không đạ
print("\n========== Bài tập 2.3 ==========")
diem_tb_sv = df.groupby("ho_ten")["diem"].mean().round(2)
print(diem_tb_sv)
sinh_vien_dat = diem_tb_sv[diem_tb_sv >= 5.0]
sinh_vien_khong_dat = diem_tb_sv[diem_tb_sv < 5.0]
print("\nSinh vien dat:")
print(sinh_vien_dat)
print("\nSinh vien khong dat:")
print(sinh_vien_khong_dat)