import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("button.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)


        #버튼에 기능을 연결하는 코드
        self.btn.clicked.connect(self.crawling)


    # def button_event(self):
    #     text=self.lineEdit.text()
    #     self.label.setText(text)
    def crawling(self):
        # https://www.wordreference.com/검색
        wordput = self.lineEdit.text()
        url = f"https://www.wordreference.com/enko/{wordput}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"}
        res = requests.get(url)
        bs = BeautifulSoup(res.content, 'html.parser')
        mean = bs.select("td.ToWrd")
        print(mean)
        words = []
        for i in range(len(mean)):
            words.append(bs.select("td.ToWrd")[i].get_text())
        # print(words)
        search = "한국어"
        for word in words:
            if search in word:
                words.remove(word)
        print(words)
        wot='\n'.join(words)
        self.label.setText(wot)


        #pandas 라이브러리로 표만들기
        word_data=pd.DataFrame()
        #word_data['단어']=pd.Series(wordput)
        word_data['뜻']=pd.Series(words)

        print(word_data)
        #엑셀 형태로 저장하기
        word_data.to_excel(excel_writer=".\\words_means\\"+self.lineEdit.text()+"_means.xls")


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()