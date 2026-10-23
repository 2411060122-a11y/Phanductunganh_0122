import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit,
    QListWidget, QVBoxLayout, QHBoxLayout, QMessageBox
)

class UngDungToDo(QWidget):
    def __init__(self):
        super().__init__()
        self.ds = []                      # (noi_dung, da_xong)
        self.setWindowTitle("Ghi chu cong viec")
        self.resize(420, 420)

        self.o_nhap = QLineEdit()
        nut_them = QPushButton("Them")
        nut_them.clicked.connect(self.them)
        h1 = QHBoxLayout()
        h1.addWidget(self.o_nhap)
        h1.addWidget(nut_them)

        self.list = QListWidget()

        nut_xong = QPushButton("Danh dau hoan thanh")
        nut_xong.clicked.connect(self.xong)
        nut_xoa = QPushButton("Xoa cong viec")
        nut_xoa.clicked.connect(self.xoa)
        h2 = QHBoxLayout()
        h2.addWidget(nut_xong)
        h2.addWidget(nut_xoa)

        main = QVBoxLayout()
        main.addWidget(QLabel("TO-DO LIST"))
        main.addLayout(h1)
        main.addWidget(self.list)
        main.addLayout(h2)
        self.setLayout(main)

    def lam_moi(self):
        self.list.clear()
        for nd, xong in self.ds:
            self.list.addItem(("[Da xong] " if xong else "[Chua xong] ") + nd)

    def them(self):
        nd = self.o_nhap.text().strip()
        if nd == "":
            QMessageBox.critical(self, "Loi", "Vui long nhap cong viec.")
            return
        self.ds.append((nd, False))
        self.o_nhap.clear()
        self.lam_moi()

    def xoa(self):
        i = self.list.currentRow()
        if i < 0:
            QMessageBox.critical(self, "Loi", "Vui long chon cong viec.")
            return
        self.ds.pop(i)
        self.lam_moi()

    def xong(self):
        i = self.list.currentRow()
        if i < 0:
            QMessageBox.critical(self, "Loi", "Vui long chon cong viec.")
            return
        self.ds[i] = (self.ds[i][0], True)
        self.lam_moi()

app = QApplication(sys.argv)
w = UngDungToDo()
w.show()
sys.exit(app.exec_())