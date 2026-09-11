tu_dien_anh_viet = {
    "the purpose of our lives is to be happy": "muc dich cua doi song la hanh phuc",
    "life goes on": "cuoc song van tiep dien",
    "turn your wounds into wisdom": "bien vet thuong thanh su thong thai"
}
# Tra tu
print(tu_dien_anh_viet.get(
    "the purpose of our lives is to be happy",
    "Khong tim thay tu nay"
))
print(tu_dien_anh_viet.get(
    "life goes on",
    "Khong tim thay tu nay"
))
print(tu_dien_anh_viet.get(
    "turn your wounds into wisdom",
    "Khong tim thay tu nay"
))
# Them tu moi
tu_dien_anh_viet["computer"] = "may tinh"

# Xoa mot tu
tu_dien_anh_viet.pop("computer")

# In tu dien hien tai
print("Tu dien hien tai:")

for tu, nghia in tu_dien_anh_viet.items():
    print(tu, ":", nghia)