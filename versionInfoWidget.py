from PySide6.QtWidgets import QWidget, QApplication
from ui_version_info_widget import Ui_Form
from project_config_reader import ProjectConfigReader


class VersionInfoWidget(Ui_Form, QWidget):
    def __init__(self, parent=..., f=...):
        if parent == ...:
            parent = None
        if f == ...:
            f = None
        super().__init__(parent)
        self.setupUi(self)

    def setVersionInfo(self, vi: ProjectConfigReader):
        if vi.has_attr("HasVersionInfo"):
            if vi["HasVersionInfo"]:
                self.checkBox_enable.setChecked(True)
            else:
                self.checkBox_enable.setChecked(False)
        dick = {
            "Companyname": self.lineEdit_company_name,
            "Filedescription": self.lineEdit_file_desc,
            "Copyrights": self.lineEdit_legal_copyr,
            "Trademarks": self.lineEdit_legal_trademark,
            "Originalname": self.lineEdit_orig_filename,
            "Productversion": self.lineEdit_product_version,
            "Fileversion": self.lineEdit_fileversion,
            "Productname": self.lineEdit_product_name,
            "Internalname": self.lineEdit_inside_name,
        }
        for i in dick.keys():
            if vi.has_attr(i):
                if not vi[i]:
                    continue
                dick[i].setText(str(vi[i]))


if __name__ == "__main__":
    a = QApplication(list())
    viw = VersionInfoWidget()
    viw.show()
    a.exec()
