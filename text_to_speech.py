# -*- coding: utf-8 -*-

import sys
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from matplotlib import rc
import matplotlib.pyplot as plt
import seaborn as sns
from sympy import *
from sympy import sqrt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

rc('font',family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setupUI()
        self.setLayout(self.layout)
        self.setGeometry(200, 200, 1000, 700)
        self.text_audio = "샘플입니다."
        self.text_audio_1 = "첫번째그래프 설명"
        self.text_audio_2 = "두번째그래프 설명"

    def setupUI(self):
        
        self.setWindowTitle("PyChart Viewer v0.1")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.pushButton = QPushButton("차트그리기")
        self.lineEdit_x1 = QLineEdit()
        self.lineEdit_x2 = QLineEdit()
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label_error = QLabel(" ")
        self.label_error.setStyleSheet("Color: red")

        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.label1 = QLabel("그래프")
        self.label1.setStyleSheet("font-size : 18pt")
        self.blank = QLabel(" ")
        self.label2= QLabel("# 그래프 설명")
        self.mp3 = QPushButton("재생")
        self.mp3.clicked.connect(self.playSound)
        self.label2.setStyleSheet("font-size : 18pt")
        self.graph_explain1 = QLabel("블라블라")
        self.graph_explain2 = QLabel("블라블라")
        self.graph_explain3 = QLabel("블라블라")

        #노래
        playLayout = QHBoxLayout()
        playLayout.addWidget(self.label2)
        playLayout.addWidget(self.mp3)

        # Left Layout
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.label1)
        leftLayout.addWidget(self.canvas)
        leftLayout.addWidget(self.blank)
        leftLayout.addLayout(playLayout)
        leftLayout.addWidget(self.graph_explain1)
        leftLayout.addWidget(self.graph_explain2)
        leftLayout.addWidget(self.graph_explain3)
        leftLayout.addStretch(1)

        # Right Layout
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.lineEdit1)
        rightLayout.addWidget(self.lineEdit2)
        rightLayout.addWidget(self.pushButton)
        rightLayout.addWidget(self.label_error)
        rightLayout.addWidget(self.lineEdit_x1)
        rightLayout.addWidget(self.lineEdit_x2)
        rightLayout.addStretch(1)

        self.layout = QHBoxLayout()
        self.layout.addLayout(leftLayout)
        self.layout.addLayout(rightLayout)
        self.layout.setStretchFactor(leftLayout, 1)
        self.layout.setStretchFactor(rightLayout, 0)


    def graphExplainX(self,equ):

        try :
            # x절편
            x=Symbol('x')
            equation = eval(equ)
            x_inter = str(solve(equation)[0])

            # 그래프 설명
            #self.graph_explain1.setText("y = "+equ+" 그래프의 "+"x절편은 "+x_inter+"이고,")#+"   ( "+x_inter+" , 0 )")
            #self.graph_explain1.adjustSize()
            text = "의 x절편은 "+x_inter+"이고, "
            return text
            

        except IndexError:
            text = "는 x과 만나지 않고, "
            return text

    def graphExplainY(self,equ):

        try :
            # y절편
            x=Symbol('x')
            y=Symbol('y')
            equation1 = eval(equ+"-y")
            equation2 = x
            y_dict = solve((equation1,equation2),dict=True)[0]
            y_inter = str(y_dict[y])

            text2 = "y절편은 "+y_inter+"이다."
            return text2

        except IndexError:
            text2 = "y축과 만나지 않는다."
            return text2
    
    def tangentPoint(self,equ1,equ2):

        try :
            # x절편
            x=Symbol('x')
            y=Symbol('y')
            equation1 = eval(equ1+"-y")
            equation2 = eval(equ2+"-y")
            xy_dict = solve((equation1,equation2),dict=True)[0]
            x_inter = str(xy_dict[x])
            y_inter = str(xy_dict[y])

            # 그래프 설명
            #self.graph_explain1.setText("y = "+equ+" 그래프의 "+"x절편은 "+x_inter+"이고,")#+"   ( "+x_inter+" , 0 )")
            #self.graph_explain1.adjustSize()
            text = "두 그래프의 접점은 ( "+x_inter+", "+y_inter+" )이다."
            print(text)
            return text
            

        except IndexError:
            print("두 그래프의 접점은 존재하지 않는다.")

    def quadrant(self,equ):
        from numpy import sqrt,cos,sin,tan
        qua1,qua2,qua3,qua4 = false,false,false,false
        
        try :
            for x in np.arange(-10,11) :
                y_qu = eval(equ)
                if x>0 and y_qu.real>0:
                    qua1 = true
                elif x>0 and y_qu.real<0:
                    qua4 = true
                elif x<0 and y_qu.real>0:
                    qua2 = true
                elif x<0 and y_qu.real<0:
                    qua3 = true
            text = " 제 "        
            if(qua1==true) : text+="1사분면 "
            if(qua2==true) : text+="2사분면 "
            if(qua3==true) : text+="3사분면 "
            if(qua4==true) : text+="4사분면 "
            text+="에 위치한다."
            return text

        except IndexError:
            print("사분면 에러")

    def pushButtonClicked(self):
        from numpy import sqrt,cos,sin,tan
        
        #try :
            # 입력받은 수식을 변수에 넣기
        equ1 = self.lineEdit1.text()
        equ2 = self.lineEdit2.text()
        x1 = self.lineEdit_x1.text()
        x2 = self.lineEdit_x2.text()
            
            # error경고메세지 초기화
        self.label_error.setText(" ")
        self.label_error.adjustSize()

            # 그래프 설명 초기화
        self.graph_explain1.setText(" ")
        self.graph_explain1.adjustSize()
        self.graph_explain2.setText(" ")
        self.graph_explain2.adjustSize()

            # 그래프 그리는 부분 초기화
        self.fig.clear()
        ax = self.fig.add_subplot(111)
            
            # x,y축 그리기
        ax.axvline(x=0,color='black')
        ax.axhline(y=0,color='black')

        if(x1=="" or x2 =="") :
            x = np.arange(-10,11,step = 0.01)
        else :
            x = np.arange(int(x1),int(x2),step = 0.1)
        y1 = eval(equ1)

        
        tol=100
        y1[y1 > tol] = np.inf
        y1[y1 < -tol] = -np.inf
        
        ax.plot(x,y1,lw=1)

        #두번째 수식 입력이 null이 아니면 그리기
        if(equ2!="") :
            y2 = eval(equ2)
        
            tol=100
            y2[y2 > tol] = np.inf
            y2[y2 < -tol] = -np.inf
        
            ax.plot(x,y2,lw=1)

        ax.grid()
        ax.set_xlabel("x축")
        ax.set_ylabel("y축",rotation=0)

            #redraw
        self.canvas.draw_idle()

            # 그래프 제목 설정
        self.label1.setText("y = "+equ1+"  그래프 출력")
        self.label1.adjustSize()
        print("첫번째 수식 : "+str(equ1))
        print("두번째 수식 : "+str(equ2))

        ### 첫번째 수식
        ## 1. 이차함수일 때
        if "x**2" in equ1 or "x*x" in equ1:
            print("이차함수")
            equ_split1 = equ1.split("*x**2")
            print("첫:"+equ_split1[0])
            if(eval(equ_split1[0])>0):
                how = "아래"
            else:
                how = "위"
            equ_split2 = equ_split1[1].split("*x")
            print("두:"+equ_split2[0])
            xx = (-1)*eval(equ_split2[0])/(2*eval(equ_split1[0]))
            x=Symbol('x')
            y=Symbol('y')
            equation1 = eval(equ1+"-y")
            equation2 = x-xx
            xy_dict = solve((equation1,equation2),dict=True)[0]
            print("답:"+str(xy_dict[y]))
            print(xx)

            ## 제곱표시로 바꾸기
            if "x**2" in equ1 :
                equ1_re = equ1.replace("x**2","x^2")
            elif "x*x" in equ1 :
                equ1_re = equ1.replace("x*x","x^2")

            ## 곱하기 표시 지우기
            equ1_re = equ1_re.replace("*","")

            ax.scatter(round(xx,2),round(xy_dict[y],2),c='red',s=50)
            self.text_audio_1 = "이차함수 y = "+equ1_re+" 그래프의 꼭짓점은 ("+ str(round(xx,2))+", "+str(round(xy_dict[y],2))+")이고, "+how+"로 볼록한 포물선이다. "+self.quadrant(equ1)
            self.graph_explain1.setText(self.text_audio_1)
            self.graph_explain1.adjustSize()

            ## 이콜, 루트, 괄호 음성 변환
            audio_graph1 = "이차함수 y = "+equ1_re
            audio_graph1 = audio_graph1.replace("^2","제곱")
            audio_graph1 = audio_graph1.replace("="," 이콜,")
            audio_graph1 = audio_graph1.replace("sqrt","루트")
            audio_graph1 = audio_graph1.replace("(","괄호 열고,")
            audio_graph1 = audio_graph1.replace(")",",괄호 닫고")
            self.text_audio_1 = audio_graph1+" 그래프의 꼭짓점은 ("+ str(round(xx,2))+", "+str(round(xy_dict[y],2))+")이고, "+how+"로 볼록한 포물선이다. "+self.quadrant(equ1)

        else :
            ## 곱하기 표시 지우기
            equ1_re = equ1.replace("*","")

            self.text_audio_1 = "y = "+equ1_re+" 그래프"+self.graphExplainX(equ1) + self.graphExplainY(equ1) + self.quadrant(equ1)

            self.graph_explain1.setText(self.text_audio_1)
            self.graph_explain1.adjustSize()

            ## 이콜, 루트, 괄호 음성 변환
            audio_graph1 = "y = "+equ1_re
            audio_graph1 = audio_graph1.replace("^2","제곱")
            audio_graph1 = audio_graph1.replace("="," 이콜,")
            audio_graph1 = audio_graph1.replace("sqrt","루트")
            audio_graph1 = audio_graph1.replace("(","괄호 열고,")
            audio_graph1 = audio_graph1.replace(")",",괄호 닫고")
            self.text_audio_1 = audio_graph1+" 그래프"+self.graphExplainX(equ1) + self.graphExplainY(equ1) + self.quadrant(equ1)
        
        ### 두번째 수식    
        if(equ2!="") :

            ## 1. 이차함수일 때
            if "x**2" in equ2 or "x*x" in equ2:
                print("이차함수")
                equ2_split1 = equ2.split("*x**2")
                print("첫:"+equ2_split1[0])
                if(eval(equ2_split1[0])>0):
                    how = "아래"
                else:
                    how = "위"
                equ2_split2 = equ2_split1[1].split("*x")
                print("두:"+equ2_split2[0])
                xx = (-1)*eval(equ2_split2[0])/(2*eval(equ2_split1[0]))
                x=Symbol('x')
                y=Symbol('y')
                equation2_1 = eval(equ2+"-y")
                equation2_2 = x-xx
                xy_dict2 = solve((equation2_1,equation2_2),dict=True)[0]
                print("답:"+str(xy_dict2[y]))
                print(xx)

                ## 제곱표시로 바꾸기
                if "x**2" in equ2 :
                    equ2_re = equ2.replace("x**2","x^2")
                elif "x*x" in equ2 :
                    equ2_re = equ2.replace("x*x","x^2")

                ## 곱하기 표시 지우기
                equ2_re = equ2_re.replace("*","")

                ax.scatter(round(xx,2),round(xy_dict2[y],2),c='red',s=50)
                self.text_audio_2 = "이차함수 y = "+equ2_re+" 그래프의 꼭짓점은 ("+ str(round(xx,2))+", "+str(round(xy_dict2[y],2))+")이고, "+how+"로 볼록한 포물선이다. "+self.quadrant(equ2)
                self.graph_explain2.setText(self.text_audio_2)
                self.graph_explain2.adjustSize()

                ## 이콜, 루트, 괄호 음성 변환
                audio_graph2 = "이차함수 y = "+equ2_re
                audio_graph2 = audio_graph2.replace("^2","제곱")
                audio_graph2 = audio_graph2.replace("="," 이콜,")
                audio_graph2 = audio_graph2.replace("sqrt","루트")
                audio_graph2 = audio_graph2.replace("(","괄호 열고,")
                audio_graph2 = audio_graph2.replace(")",",괄호 닫고")
                self.text_audio_2 = audio_graph2+" 그래프의 꼭짓점은 ("+ str(round(xx,2))+", "+str(round(xy_dict2[y],2))+")이고, "+how+"로 볼록한 포물선이다. "+self.quadrant(equ2)

            else :
                ## 곱하기 표시 지우기
                equ2_re = equ2.replace("*","")

                self.text_audio_2 = "y = "+equ2_re+" 그래프"+self.graphExplainX(equ2) + self.graphExplainY(equ2) + self.quadrant(equ2)

                self.graph_explain2.setText(self.text_audio_2)
                self.graph_explain2.adjustSize()

                ## 이콜, 루트, 괄호 음성 변환
                audio_graph2 = "y = "+equ2_re
                audio_graph2 = audio_graph2.replace("^2","제곱")
                audio_graph2 = audio_graph2.replace("="," 이콜,")
                audio_graph2 = audio_graph2.replace("sqrt","루트")
                audio_graph2 = audio_graph2.replace("(","괄호 열고,")
                audio_graph2 = audio_graph2.replace(")",",괄호 닫고")
                self.text_audio_2 = audio_graph2+" 그래프"+self.graphExplainX(equ2) + self.graphExplainY(equ2) + self.quadrant(equ2)

            self.tangentPoint(equ1,equ2)
            self.graph_explain3.setText(self.tangentPoint(equ1,equ2))
            self.graph_explain3.adjustSize()

    def playSound(self) :
        from gtts import gTTS
        from subprocess import call
        from pydub import AudioSegment
        import os
        import time
        #매번 음성 추출 경우의 수에 따라 나오도록
        self.text_audio = self.text_audio_1+self.text_audio_2
        print(self.text_audio)
        tts = gTTS(text=self.text_audio,lang='ko') #속도는 두가지뿐.. slow=True
        tts.save("ex.mp3")
        call(["afplay","/Users/eumiing/python_project/ex.mp3"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()