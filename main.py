
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import os
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

main_ui = uic.loadUiType(resource_path("main.ui"))[0]

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
# main_ui = uic.loadUiType("main.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class MainWindowClass(QMainWindow, main_ui) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.button_process.clicked.connect(self.action)

    def action(self):
        #edit_input의 text를 label_output의 text변경
        self.label_output.setText(self.edit_input.text())
        self.edit_input.setText("")



if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = MainWindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
