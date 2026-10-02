"""Chuong trinh quan ly sieu thi mini."""

from datetime import datetime

TEN_CUA_HANG = "SIEU THI MINI"
NGUONG_SAP_HET = 10  # ton kho <= nguong nay se bi canh bao
DO_RONG_BANG = 77
DO_RONG_HOA_DON = 50

# Chuan hoa loai san pham: khoa la du lieu nhap (viet hoa), gia tri la ten hien thi
LOAI_SP_HOP_LE = {
    "THUC PHAM": "Thuc pham",
    "DO UONG": "Do uong",
    "GIA DUNG": "Gia dung",
    "KHAC": "Khac",
}

# Cac bac giam gia theo tong tien (xep tu cao xuong thap): (moc tien, phan tram giam)
BAC_GIAM_GIA = [
    (1000000, 10),
    (500000, 5),
]

danh_sach_san_pham = [
    {"ma_sp": "SP001", "ten_sp": "Gao ST25 5kg", "loai_sp": "Thuc pham", "gia": 120000, "so_luong": 40},
    {"ma_sp": "SP002", "ten_sp": "Mi goi Hao Hao", "loai_sp": "Thuc pham", "gia": 4500, "so_luong": 200},
    {"ma_sp": "SP003", "ten_sp": "Sua tuoi Vinamilk 1L", "loai_sp": "Do uong", "gia": 32000, "so_luong": 60},
    {"ma_sp": "SP004", "ten_sp": "Nuoc suoi Aquafina", "loai_sp": "Do uong", "gia": 6000, "so_luong": 150},
    {"ma_sp": "SP005", "ten_sp": "Nuoc rua chen Sunlight", "loai_sp": "Gia dung", "gia": 28000, "so_luong": 25},
    {"ma_sp": "SP006", "ten_sp": "Giay ve sinh Pulppy", "loai_sp": "Gia dung", "gia": 55000, "so_luong": 8},
    {"ma_sp": "SP007", "ten_sp": "Dau an Tuong An 1L", "loai_sp": "Thuc pham", "gia": 52000, "so_luong": 30},
    {"ma_sp": "SP008", "ten_sp": "Pin AA (vi 4 vien)", "loai_sp": "Khac", "gia": 40000, "so_luong": 5},
]
lich_su_ban_hang = []
lich_su_nhap_hang = []


# ---------------------------------------------------------------------------
# Ham ho tro
# ---------------------------------------------------------------------------
def thoi_gian_hien_tai():
    return datetime.now().strftime("%d/%m/%Y %H:%M")


def dinh_dang_tien(so_tien):
    return f"{so_tien:,} VND"


def nhap_so_nguyen(loi_nhac, gia_tri_toi_thieu=1):
    """Yeu cau nhap so nguyen >= gia_tri_toi_thieu, nhap sai thi hoi lai."""
    while True:
        try:
            so = int(input(loi_nhac))
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so nguyen.")
            continue
        if so < gia_tri_toi_thieu:
            print(f"-> Gia tri phai lon hon hoac bang {gia_tri_toi_thieu}.")
            continue
        return so


def nhap_chuoi_khong_rong(loi_nhac):
    """Yeu cau nhap chuoi khong rong."""
    while True:
        gia_tri = input(loi_nhac).strip()
        if gia_tri:
            return gia_tri
        print("-> Khong duoc de trong, vui long nhap lai.")


def xac_nhan(loi_nhac):
    """Hoi xac nhan co/khong, tra ve True neu nguoi dung dong y."""
    return input(loi_nhac).strip().lower() in ("y", "yes", "c", "co")


def tim_san_pham_theo_ma(ma_sp):
    """Tra ve san pham co ma tuong ung, hoac None neu khong tim thay."""
    for san_pham in danh_sach_san_pham:
        if san_pham["ma_sp"] == ma_sp:
            return san_pham
    return None


def tao_ma_hoa_don():
    return f"HD{len(lich_su_ban_hang) + 1:04d}"


def tinh_tong_tien(gio_hang):
    return sum(muc["gia"] * muc["so_luong"] for muc in gio_hang)


def tinh_giam_gia(tong_tien):
    """Tra ve (phan tram giam, so tien giam) theo tong tien."""
    for moc_tien, phan_tram in BAC_GIAM_GIA:
        if tong_tien >= moc_tien:
            return phan_tram, tong_tien * phan_tram // 100
    return 0, 0


def ghi_chu_ton_kho(so_luong):
    if so_luong == 0:
        return "HET HANG"
    if so_luong <= NGUONG_SAP_HET:
        return "SAP HET"
    return ""


# ---------------------------------------------------------------------------
# Quan ly san pham
# ---------------------------------------------------------------------------
def hien_thi_danh_sach_san_pham(danh_sach=None):
    if danh_sach is None:
        danh_sach = danh_sach_san_pham
    if not danh_sach:
        print("-> Khong co san pham nao de hien thi.")
        return
    print("\n" + "=" * DO_RONG_BANG)
    print(f"{'Ma SP':<8}{'Ten san pham':<24}{'Loai':<12}{'Gia':>12}{'Ton kho':>9}  {'Ghi chu':<10}")
    print("-" * DO_RONG_BANG)
    for sp in danh_sach:
        print(
            f"{sp['ma_sp']:<8}{sp['ten_sp']:<24.23}{sp['loai_sp']:<12}{sp['gia']:>12,}"
            f"{sp['so_luong']:>9}  {ghi_chu_ton_kho(sp['so_luong']):<10}"
        )
    print("=" * DO_RONG_BANG)


def tim_kiem_san_pham(tu_khoa):
    """Tim san pham co ten chua tu khoa (khong phan biet hoa thuong)."""
    ket_qua = [sp for sp in danh_sach_san_pham if tu_khoa.lower() in sp["ten_sp"].lower()]
    if not ket_qua:
        print(f"-> Khong tim thay san pham nao chua '{tu_khoa}'.")
        return
    print(f"\nTim thay {len(ket_qua)} san pham:")
    hien_thi_danh_sach_san_pham(ket_qua)


def them_san_pham(ma_sp, ten_sp, loai_sp, gia, so_luong):
    if not ma_sp:
        print("-> Ma san pham khong duoc de trong.")
        return
    if tim_san_pham_theo_ma(ma_sp) is not None:
        print(f"-> Ma san pham {ma_sp} da ton tai, khong the them.")
        return
    loai_chuan = LOAI_SP_HOP_LE.get(loai_sp.upper())
    if loai_chuan is None:
        print(f"-> Loai san pham khong hop le (chi nhan: {', '.join(LOAI_SP_HOP_LE.values())}).")
        return
    danh_sach_san_pham.append({
        "ma_sp": ma_sp,
        "ten_sp": ten_sp,
        "loai_sp": loai_chuan,
        "gia": gia,
        "so_luong": so_luong,
    })
    print(f"-> Da them san pham {ma_sp} - {ten_sp} thanh cong.")


def nhap_them_hang(ma_sp, so_luong):
    san_pham = tim_san_pham_theo_ma(ma_sp)
    if san_pham is None:
        print(f"-> Khong tim thay san pham {ma_sp}.")
        return
    san_pham["so_luong"] += so_luong
    lich_su_nhap_hang.append({
        "thoi_gian": thoi_gian_hien_tai(),
        "ma_sp": ma_sp,
        "ten_sp": san_pham["ten_sp"],
        "so_luong": so_luong,
    })
    print(f"-> Da nhap them {so_luong} {san_pham['ten_sp']}. Ton kho hien tai: {san_pham['so_luong']}.")


def cap_nhat_gia(ma_sp, gia_moi):
    san_pham = tim_san_pham_theo_ma(ma_sp)
    if san_pham is None:
        print(f"-> Khong tim thay san pham {ma_sp}.")
        return
    gia_cu = san_pham["gia"]
    san_pham["gia"] = gia_moi
    print(f"-> Da doi gia {san_pham['ten_sp']}: {gia_cu:,} -> {gia_moi:,} VND.")


def xoa_san_pham(ma_sp):
    san_pham = tim_san_pham_theo_ma(ma_sp)
    if san_pham is None:
        print(f"-> Khong tim thay san pham {ma_sp}.")
        return
    if not xac_nhan(f"Ban co chac muon xoa '{san_pham['ten_sp']}'? (y/n): "):
        print("-> Da huy thao tac xoa.")
        return
    danh_sach_san_pham.remove(san_pham)
    print(f"-> Da xoa san pham {ma_sp}.")


def canh_bao_ton_kho():
    sap_het = [sp for sp in danh_sach_san_pham if sp["so_luong"] <= NGUONG_SAP_HET]
    if not sap_het:
        print("-> Tat ca san pham deu con du hang.")
        return
    print(f"\nCANH BAO - SAN PHAM CON TU {NGUONG_SAP_HET} TRO XUONG:")
    for sp in sorted(sap_het, key=lambda s: s["so_luong"]):
        print(f" {sp['ma_sp']} - {sp['ten_sp']} - con {sp['so_luong']} ({ghi_chu_ton_kho(sp['so_luong'])})")


# ---------------------------------------------------------------------------
# Ban hang
# ---------------------------------------------------------------------------
def them_vao_gio(gio_hang, ma_sp, so_luong):
    san_pham = tim_san_pham_theo_ma(ma_sp)
    if san_pham is None:
        print(f"-> Khong tim thay san pham {ma_sp}.")
        return
    muc_da_co = next((m for m in gio_hang if m["ma_sp"] == ma_sp), None)
    so_luong_trong_gio = muc_da_co["so_luong"] if muc_da_co else 0
    if so_luong + so_luong_trong_gio > san_pham["so_luong"]:
        print(f"-> Khong du hang: ton kho {san_pham['so_luong']}, trong gio da co {so_luong_trong_gio}.")
        return
    if muc_da_co:
        muc_da_co["so_luong"] += so_luong
    else:
        gio_hang.append({
            "ma_sp": ma_sp,
            "ten_sp": san_pham["ten_sp"],
            "loai_sp": san_pham["loai_sp"],
            "gia": san_pham["gia"],
            "so_luong": so_luong,
        })
    print(f"-> Da them {so_luong} {san_pham['ten_sp']} vao gio hang.")


def xoa_khoi_gio(gio_hang, ma_sp):
    for muc in gio_hang:
        if muc["ma_sp"] == ma_sp:
            gio_hang.remove(muc)
            print(f"-> Da bo {muc['ten_sp']} khoi gio hang.")
            return
    print(f"-> San pham {ma_sp} khong co trong gio hang.")


def hien_thi_gio_hang(gio_hang):
    if not gio_hang:
        print("-> Gio hang dang trong.")
        return
    tong_tien = tinh_tong_tien(gio_hang)
    phan_tram, so_tien_giam = tinh_giam_gia(tong_tien)
    print("\nGIO HANG HIEN TAI:")
    print(f"{'Ma SP':<8}{'Ten san pham':<24}{'SL':>4}{'Don gia':>12}{'Thanh tien':>14}")
    print("-" * 62)
    for muc in gio_hang:
        thanh_tien = muc["gia"] * muc["so_luong"]
        print(f"{muc['ma_sp']:<8}{muc['ten_sp']:<24.23}{muc['so_luong']:>4}{muc['gia']:>12,}{thanh_tien:>14,}")
    print("-" * 62)
    print(f"Tong tien: {dinh_dang_tien(tong_tien)}")
    if phan_tram > 0:
        print(f"Giam gia {phan_tram}%: -{dinh_dang_tien(so_tien_giam)}")
        print(f"Can thanh toan: {dinh_dang_tien(tong_tien - so_tien_giam)}")


def in_hoa_don(hoa_don):
    print("\n" + "=" * DO_RONG_HOA_DON)
    print(f"{TEN_CUA_HANG:^{DO_RONG_HOA_DON}}")
    print(f"{'HOA DON BAN HANG':^{DO_RONG_HOA_DON}}")
    print("-" * DO_RONG_HOA_DON)
    print(f"Ma HD: {hoa_don['ma_hd']}    Thoi gian: {hoa_don['thoi_gian']}")
    print(f"Khach hang: {hoa_don['ten_khach']}")
    print("-" * DO_RONG_HOA_DON)
    print(f"{'San pham':<22}{'SL':>4}{'Don gia':>12}{'Thanh tien':>12}")
    for muc in hoa_don["chi_tiet"]:
        thanh_tien = muc["gia"] * muc["so_luong"]
        print(f"{muc['ten_sp']:<22.21}{muc['so_luong']:>4}{muc['gia']:>12,}{thanh_tien:>12,}")
    print("-" * DO_RONG_HOA_DON)
    print(f"{'Tong tien:':<20}{dinh_dang_tien(hoa_don['tong_tien']):>30}")
    print(f"{'Giam gia:':<20}{'-' + dinh_dang_tien(hoa_don['giam_gia']):>30}")
    print(f"{'THANH TOAN:':<20}{dinh_dang_tien(hoa_don['thanh_toan']):>30}")
    print(f"{'Tien khach dua:':<20}{dinh_dang_tien(hoa_don['tien_khach']):>30}")
    print(f"{'Tien thoi lai:':<20}{dinh_dang_tien(hoa_don['tien_thoi']):>30}")
    print("=" * DO_RONG_HOA_DON)
    print(f"{'Cam on quy khach!':^{DO_RONG_HOA_DON}}")


def thanh_toan(gio_hang, ten_khach):
    """Thanh toan gio hang. Tra ve True neu giao dich hoan tat."""
    if not gio_hang:
        print("-> Gio hang dang trong, khong the thanh toan.")
        return False

    tong_tien = tinh_tong_tien(gio_hang)
    phan_tram, so_tien_giam = tinh_giam_gia(tong_tien)
    phai_tra = tong_tien - so_tien_giam
    print(f"\n-> Tong tien: {dinh_dang_tien(tong_tien)} | Giam {phan_tram}%: {dinh_dang_tien(so_tien_giam)}")
    print(f"-> Khach can tra: {dinh_dang_tien(phai_tra)}")

    while True:
        tien_khach = nhap_so_nguyen("Nhap so tien khach dua (0 de huy thanh toan): ", 0)
        if tien_khach == 0:
            print("-> Da huy thanh toan.")
            return False
        if tien_khach >= phai_tra:
            break
        print(f"-> Tien khach dua con thieu {dinh_dang_tien(phai_tra - tien_khach)}.")

    # Tru ton kho sau khi thanh toan thanh cong
    for muc in gio_hang:
        san_pham = tim_san_pham_theo_ma(muc["ma_sp"])
        san_pham["so_luong"] -= muc["so_luong"]

    hoa_don = {
        "ma_hd": tao_ma_hoa_don(),
        "thoi_gian": thoi_gian_hien_tai(),
        "ten_khach": ten_khach,
        "chi_tiet": [dict(muc) for muc in gio_hang],
        "tong_tien": tong_tien,
        "giam_gia": so_tien_giam,
        "thanh_toan": phai_tra,
        "tien_khach": tien_khach,
        "tien_thoi": tien_khach - phai_tra,
    }
    lich_su_ban_hang.append(hoa_don)
    in_hoa_don(hoa_don)
    return True


def hien_thi_menu_ban_hang():
    print("\n--- BAN HANG ---")
    print("1. Them san pham vao gio")
    print("2. Xem gio hang")
    print("3. Bo san pham khoi gio")
    print("4. Thanh toan")
    print("0. Huy / Quay lai")


def ban_hang():
    gio_hang = []
    ten_khach = input("Nhap ten khach (Enter de bo qua): ").strip().title() or "Khach le"
    hien_thi_danh_sach_san_pham()

    while True:
        hien_thi_menu_ban_hang()
        lua_chon = input("Chon thao tac: ").strip()
        if lua_chon == "1":
            ma_sp = input("Nhap ma san pham: ").strip().upper()
            so_luong = nhap_so_nguyen("Nhap so luong: ")
            them_vao_gio(gio_hang, ma_sp, so_luong)
        elif lua_chon == "2":
            hien_thi_gio_hang(gio_hang)
        elif lua_chon == "3":
            ma_sp = input("Nhap ma san pham can bo: ").strip().upper()
            xoa_khoi_gio(gio_hang, ma_sp)
        elif lua_chon == "4":
            if thanh_toan(gio_hang, ten_khach):
                break
        elif lua_chon == "0":
            if gio_hang and not xac_nhan("Gio hang chua thanh toan, ban co chac muon huy? (y/n): "):
                continue
            print("-> Da thoat che do ban hang.")
            break
        else:
            print("-> Lua chon khong hop le, vui long chon lai.")


# ---------------------------------------------------------------------------
# Lich su va thong ke
# ---------------------------------------------------------------------------
def xem_lich_su_hoa_don():
    if not lich_su_ban_hang:
        print("-> Chua co hoa don nao.")
        return
    print("\nLICH SU HOA DON:")
    for hd in lich_su_ban_hang:
        print(f" {hd['ma_hd']} - {hd['thoi_gian']} - {hd['ten_khach']} - {hd['thanh_toan']:,} VND")

    ma_hd = input("\nNhap ma hoa don de xem chi tiet (Enter de bo qua): ").strip().upper()
    if not ma_hd:
        return
    for hd in lich_su_ban_hang:
        if hd["ma_hd"] == ma_hd:
            in_hoa_don(hd)
            return
    print(f"-> Khong tim thay hoa don {ma_hd}.")


def xem_lich_su_nhap_hang():
    if not lich_su_nhap_hang:
        print("-> Chua co lan nhap hang nao.")
        return
    print("\nLICH SU NHAP HANG:")
    for lan_nhap in lich_su_nhap_hang:
        print(f" {lan_nhap['thoi_gian']} - {lan_nhap['ma_sp']} - {lan_nhap['ten_sp']} - +{lan_nhap['so_luong']}")


def thong_ke_doanh_thu():
    if not lich_su_ban_hang:
        print("-> Chua co giao dich ban hang nao.")
        return

    tong_doanh_thu = 0
    tong_giam_gia = 0
    so_luong_ban = {}   # ten san pham -> so luong da ban
    doanh_thu_loai = {}  # loai san pham -> doanh thu (truoc giam gia)

    for hd in lich_su_ban_hang:
        tong_doanh_thu += hd["thanh_toan"]
        tong_giam_gia += hd["giam_gia"]
        for muc in hd["chi_tiet"]:
            so_luong_ban[muc["ten_sp"]] = so_luong_ban.get(muc["ten_sp"], 0) + muc["so_luong"]
            doanh_thu_loai[muc["loai_sp"]] = (
                doanh_thu_loai.get(muc["loai_sp"], 0) + muc["gia"] * muc["so_luong"]
            )

    so_hoa_don = len(lich_su_ban_hang)
    print("\n" + "=" * 50)
    print(f"{'THONG KE DOANH THU':^50}")
    print("=" * 50)
    print(f"So hoa don          : {so_hoa_don}")
    print(f"Tong doanh thu      : {dinh_dang_tien(tong_doanh_thu)}")
    print(f"Tong tien da giam   : {dinh_dang_tien(tong_giam_gia)}")
    print(f"Trung binh/hoa don  : {dinh_dang_tien(tong_doanh_thu // so_hoa_don)}")

    print("\nTOP 3 SAN PHAM BAN CHAY:")
    ban_chay = sorted(so_luong_ban.items(), key=lambda cap: cap[1], reverse=True)[:3]
    for thu_hang, (ten_sp, so_luong) in enumerate(ban_chay, start=1):
        print(f" {thu_hang}. {ten_sp} - {so_luong} san pham")

    print("\nDOANH THU THEO LOAI (truoc giam gia):")
    for loai_sp, doanh_thu in sorted(doanh_thu_loai.items(), key=lambda cap: cap[1], reverse=True):
        print(f" {loai_sp:<12}: {dinh_dang_tien(doanh_thu)}")
    print("=" * 50)


# ---------------------------------------------------------------------------
# Menu va vong lap chinh
# ---------------------------------------------------------------------------
def hien_thi_menu():
    print(f"\n===== QUAN LY {TEN_CUA_HANG} =====")
    print("1.  Hien thi danh sach san pham")
    print("2.  Tim kiem san pham theo ten")
    print("3.  Them san pham moi")
    print("4.  Nhap them hang")
    print("5.  Cap nhat gia san pham")
    print("6.  Xoa san pham")
    print("7.  Ban hang / Thanh toan")
    print("8.  Canh bao hang sap het")
    print("9.  Xem lich su hoa don")
    print("10. Xem lich su nhap hang")
    print("11. Thong ke doanh thu")
    print("0.  Thoat chuong trinh")


def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban: ").strip()

        if lua_chon == "1":
            hien_thi_danh_sach_san_pham()
        elif lua_chon == "2":
            tu_khoa = nhap_chuoi_khong_rong("Nhap tu khoa can tim: ")
            tim_kiem_san_pham(tu_khoa)
        elif lua_chon == "3":
            ma_sp = input("Nhap ma san pham moi: ").strip().upper()
            ten_sp = nhap_chuoi_khong_rong("Nhap ten san pham: ")
            loai_sp = input(f"Nhap loai ({'/'.join(LOAI_SP_HOP_LE.values())}): ").strip()
            gia = nhap_so_nguyen("Nhap gia ban: ")
            so_luong = nhap_so_nguyen("Nhap so luong ton ban dau: ", 0)
            them_san_pham(ma_sp, ten_sp, loai_sp, gia, so_luong)
        elif lua_chon == "4":
            ma_sp = input("Nhap ma san pham can nhap hang: ").strip().upper()
            so_luong = nhap_so_nguyen("Nhap so luong nhap them: ")
            nhap_them_hang(ma_sp, so_luong)
        elif lua_chon == "5":
            ma_sp = input("Nhap ma san pham can doi gia: ").strip().upper()
            gia_moi = nhap_so_nguyen("Nhap gia moi: ")
            cap_nhat_gia(ma_sp, gia_moi)
        elif lua_chon == "6":
            ma_sp = input("Nhap ma san pham can xoa: ").strip().upper()
            xoa_san_pham(ma_sp)
        elif lua_chon == "7":
            ban_hang()
        elif lua_chon == "8":
            canh_bao_ton_kho()
        elif lua_chon == "9":
            xem_lich_su_hoa_don()
        elif lua_chon == "10":
            xem_lich_su_nhap_hang()
        elif lua_chon == "11":
            thong_ke_doanh_thu()
        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break
        else:
            print("-> Lua chon khong hop le, vui long chon lai.")


if __name__ == "__main__":
    chay_chuong_trinh()
