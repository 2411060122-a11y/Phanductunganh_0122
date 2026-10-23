
import sys
from pathlib import Path
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class CuaSoDangNhap(QWidget):
    def __init__(self):
        super().__init__()

        # Lay duong dan file .ui cung thu muc voi file Python
        duong_dan = (
            Path(__file__).resolve().parent / "form_dang_nhap.ui"
        )

        # Kiem tra file giao dien co ton tai khong
        if not duong_dan.is_file():
            raise FileNotFoundError(
                f"Khong tim thay file giao dien: {duong_dan}\n"
                "Hay luu form_dang_nhap.ui cung thu muc voi dang_nhap.py"
            )

        # Nap giao dien Qt Designer
        uic.loadUi(str(duong_dan), self)

        # Ket noi Signal - Slot
        self.nut_dang_nhap.clicked.connect(
            self.xu_ly_dang_nhap
        )

    def xu_ly_dang_nhap(self):
        tai_khoan = self.o_nhap_tai_khoan.text().strip()
        mat_khau = self.o_nhap_mat_khau.text()

        if tai_khoan == "" or mat_khau == "":
            QMessageBox.critical(
                self,
                "Loi",
                "Vui long nhap day du tai khoan va mat khau."
            )
            return

        QMessageBox.information(
            self,
            "Thanh cong",
            f"Xin chao {tai_khoan}, dang nhap thanh cong!"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    cua_so = CuaSoDangNhap()
    cua_so.show()

    sys.exit(app.exec_())
