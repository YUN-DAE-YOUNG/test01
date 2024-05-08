import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class AddressBook(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('주소록')
        
        # 이름 입력 필드
        self.name_label = QLabel('이름:')
        self.name_edit = QLineEdit()
        
        # 전화번호 입력 필드
        self.phone_label = QLabel('전화번호:')
        self.phone_edit = QLineEdit()
        
        # 저장 버튼
        self.save_button = QPushButton('저장')
        self.save_button.clicked.connect(self.save_contact)
        
        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_edit)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_edit)
        layout.addWidget(self.save_button)
        
        self.setLayout(layout)

    def save_contact(self):
        name = self.name_edit.text()
        phone = self.phone_edit.text()
        if name and phone:
            print(f'이름: {name}, 전화번호: {phone}')
            # 이 부분에 데이터베이스나 파일에 주소록 정보를 저장하는 코드를 추가할 수 있습니다.
        else:
            print('이름과 전화번호를 입력하세요.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddressBook()
    ex.show()
    sys.exit(app.exec_())
