import matplotlib.pyplot as plt
import numpy as np
from qtpy.QtCore import*
from qtpy.QtWidgets import*
from qtpy.QtWidgets import*
import pyqtgraph as pg
import sys as _s
import pygame

class mainF(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        widget = QWidget()
        self.setStyleSheet('background-color:black;border:2px solid gray')
        self.showFullScreen()

        graph_splt = QSplitter(Qt.Vertical)
        value_splt = QSplitter(Qt.Vertical)
        
        pygame.mixer.init()
        
        self.bpm_audio = pygame.mixer_music
        self.bpm_audio.load(r"C:\Users\Alper\Desktop\ecg_program\T12 12.1 Inch Patient Monitor (mp3cut.net).wav")
        self.bpm_audio.set_volume(1.0)

        widget.setLayout(layout)

        self.amplitude_a = []
        self.dynamic_array_a = []

        self.amplitude_b = []
        self.dynamic_array_b = []

        self.amplitude_c = []
        self.dynamic_array_c = []

        self.amplitude_d = []
        self.dynamic_array_d = []

        self.amplitude_e = []
        self.dynamic_array_e = [] 

        A_flatline = list(np.linspace(0,0,1))
        A_P_wave = list(np.sin(np.linspace(0,np.pi*2,10)))
        A_P_flat = list(np.linspace(0,0,3))
        A_Q_Wave = list(np.linspace(0,-0.2,3))
        self.A_R_wave = list(np.linspace(-0.2,10,4))
        A_S_Wave = list(np.linspace(6,-7,6))
        A_S_normal = list(np.linspace(-7,0,4))
        A_T_Flatline = list(np.linspace(0,0,1))
        A_T_Wave = list(np.sin(np.linspace(0,np.pi*2,12)))
        A_U_Wave = list(np.linspace(0,0.0,6))

        B_flatline = list(np.linspace(0,-4,2))
        B_P_wave = list(np.sin(np.linspace(0,144,1)))
        B_P_flat = list(np.linspace(0,4,3))
        B_Q_Wave = list(np.linspace(0,-4,3))
        B_R_wave = list(np.linspace(-0.2,9,4))
        B_S_Wave = list(np.linspace(6,-7,6))
        B_S_normal = list(np.linspace(-7,0,4))
        B_T_Flatline = list(np.linspace(0,0,1))
        B_T_Wave = list(np.sin(np.linspace(0,3,12)))
        B_U_Wave = list(np.linspace(0,0.0,6))

        D_1_resp_wave = list(np.linspace(0,0,2))
        D_1_1_resp_wave = list(np.linspace(0,-6,2))
        D_2_resp_wave = list(np.linspace(0,10,2))
        D_3_resp_wave = list(np.linspace(13,8,1))
        D_4_resp_wave = list(np.linspace(8,0,1))

        ffD_1_resp_wave = list(np.linspace(0,0,4))
        ffD_1_1_resp_wave = list(np.linspace(0,-6,4))
        ffD_2_resp_wave = list(np.linspace(0,10,4))
        ffD_3_resp_wave = list(np.linspace(13,8,4))
        ffD_4_resp_wave = list(np.linspace(8,0,4))

        cD_1_resp_Wave = [0,0,0,0,10,10,10,10,10,10,0,0,0,0]
        cD_2_resp_Wave = [0,0,0,0,10,10,10,10,10,10,0,0,0,0] 
        cD_3_resp_Wave = [0,0,0,0,10,10,10,10,10,10,0,0,0,0]

        spo2_bar_container = [QPushButton(),QPushButton(),QPushButton(),QPushButton(),QPushButton(),QPushButton(),
                              QPushButton(),QPushButton(),QPushButton(),QPushButton(),QPushButton(),QPushButton()]

        self.amplitude_a.extend(A_flatline)
        self.amplitude_a.extend(A_P_wave)
        self.amplitude_a.extend(A_P_flat)
        self.amplitude_a.extend(A_Q_Wave)
        self.amplitude_a.extend(self.A_R_wave)
        self.amplitude_a.extend(A_S_Wave)
        self.amplitude_a.extend(A_S_normal)
        self.amplitude_a.extend(A_T_Flatline)
        self.amplitude_a.extend(A_T_Wave)
        self.amplitude_a.extend(A_U_Wave)

        self.amplitude_b.extend(B_flatline)
        self.amplitude_b.extend(B_P_wave)
        self.amplitude_b.extend(B_P_flat)
        self.amplitude_b.extend(B_Q_Wave)
        self.amplitude_b.extend(B_R_wave)
        self.amplitude_b.extend(B_S_Wave)
        self.amplitude_b.extend(B_S_normal)
        self.amplitude_b.extend(B_T_Flatline)
        self.amplitude_b.extend(B_T_Wave)
        self.amplitude_b.extend(B_U_Wave)

        self.amplitude_c.extend(D_1_resp_wave)
        self.amplitude_c.extend(D_1_1_resp_wave)
        self.amplitude_c.extend(D_2_resp_wave)
        self.amplitude_c.extend(D_3_resp_wave)
        self.amplitude_c.extend(D_4_resp_wave)

        self.amplitude_d.extend(ffD_1_resp_wave)
        self.amplitude_d.extend(ffD_1_1_resp_wave)
        self.amplitude_d.extend(ffD_2_resp_wave)
        self.amplitude_d.extend(ffD_3_resp_wave)
        self.amplitude_d.extend(ffD_4_resp_wave)

        self.amplitude_e.extend(cD_1_resp_Wave)
        self.amplitude_e.extend(cD_2_resp_Wave)
        self.amplitude_e.extend(cD_3_resp_Wave)

        self.length_main_a = len(self.amplitude_a)
        self.length_main_b = len(self.amplitude_b)
        self.length_main_c = len(self.amplitude_c)
        self.length_main_d = len(self.amplitude_d)
        self.length_main_e = len(self.amplitude_e)

        self.index_a = 0
        self.index_b = 0
        self.index_c = 0
        self.index_d = 0
        self.index_e = 0

        plotwidget_a = pg.PlotWidget()
        self.line_a = plotwidget_a.plot([],[],pen='g')

        plotwidget_b = pg.PlotWidget()
        self.line_b = plotwidget_b.plot([],[],pen='g')

        plotwidget_c = pg.PlotWidget()
        self.line_c = plotwidget_c.plot([],[],pen='yellow')

        plotwidget_d = pg.PlotWidget()
        self.line_d = plotwidget_d.plot([],[],pen='lightblue')

        plotwidget_e = pg.PlotWidget()
        self.line_e = plotwidget_e.plot([],[],pen='white')

        self.amplitude_array_a = []

        timer_a_side = QTimer(self)
        timer_a_side.timeout.connect(self.update_bpm_signal)
        timer_a_side.timeout.connect(self.update_spo2_signal)

        timer_b_side = QTimer(self)
        timer_b_side.timeout.connect(self.update_co2_signal)
        
        timer_c_side = QTimer(self)
        timer_c_side.timeout.connect(self.update_etCo2_signal)

        timer_f_side = QTimer(self)
        timer_f_side.timeout.connect(self.update_saturation_signal)

        timer_spo2_bar_side = QTimer(self)
        timer_spo2_bar_side.timeout.connect(self.update_spo2_breath_bars)
        timer_spo2_bar_side.start(40)
        
        timer_c_side.start(35)
        timer_a_side.start(25)
        timer_b_side.start(25)
        timer_f_side.start(50)

        self.nıbp_lbl = QLabel('NIBP')
        self.nıbp_val_lbl = QLabel('120 / 80')

        self.bpm_lbl = QLabel('ECG | bpm')
        self.bpm_val_lbl = QLabel('88')

        self.resp_lbl = QLabel('Resp')
        self.resp_val_lbl = QLabel(text='25')

        self.temp_lbl = QLabel('Temp')
        self.temp_lbl_t1 = QLabel('t1  97.5')
        self.temp_lbl_t2 = QLabel('t2  97.0')

        self.spo2_label = QLabel(text='SpO²')
        self.spo2_val_label = QLabel(text='98')
        self.spo2_bars = spo2_bar_container

        self.co2_lbl = QLabel('CO²')

        self.nıbp_lbl.setAlignment(Qt.AlignCenter)
        self.nıbp_val_lbl.setMaximumWidth(15000)
        self.bpm_lbl.setAlignment(Qt.AlignCenter)
        self.bpm_val_lbl.setMaximumWidth(15000)
        self.co2_lbl.setAlignment(Qt.AlignCenter)
        self.resp_lbl.setAlignment(Qt.AlignCenter)
        self.resp_val_lbl.setMaximumWidth(15000)
        self.temp_lbl.setAlignment(Qt.AlignCenter)
        self.temp_lbl_t1.setAlignment(Qt.AlignCenter)
        self.temp_lbl_t2.setAlignment(Qt.AlignCenter)
        self.spo2_label.setAlignment(Qt.AlignCenter)
        self.spo2_val_label.setMaximumWidth(15000)
        #self.co2...setAlignment(Qt.AlignCenter)

        self.bpm_lbl.setStyleSheet('font-weight:bolder;font-size:45px;color:green')
        self.bpm_val_lbl.setStyleSheet('font-weight:bolder;font-size:90px;color:green')
        self.spo2_label.setStyleSheet('font-weight:bolder;font-size:45px;color:orange')
        self.spo2_val_label.setStyleSheet('font-weight:bolder;font-size:95px;color:orange')
        self.resp_lbl.setStyleSheet('font-weight:bolder;font-size:45px;color:white')
        self.resp_val_lbl.setStyleSheet('font-weight:bolder;font-size:95px;color:orange')
        self.nıbp_lbl.setStyleSheet('font-weight:bolder;font-size:45px;color:white')
        self.nıbp_val_lbl.setStyleSheet('font-weight:bolder;font-size:95px;color:white')
        self.temp_lbl.setStyleSheet('font-weight:bolder;font-size:50px;color:white')
        self.temp_lbl_t1.setStyleSheet('font-weight:bolder;font-size:45px;color:white')
        self.temp_lbl_t2.setStyleSheet('font-weight:bolder;font-size:45px;color:white')

        self.bpm_splt = QSplitter(Qt.Horizontal)
        self.Temp_splt = QSplitter(Qt.Horizontal)
        self.Temp_t1t2_splt = QSplitter(Qt.Vertical)
        self.spo2_splt = QSplitter(Qt.Horizontal)
        self.nıbp_splt = QSplitter(Qt.Horizontal)
        self.resp_splt = QSplitter(Qt.Horizontal)
        self.spo2bar_splt = QSplitter(Qt.Vertical)

        self.bpm_splt.addWidget(self.bpm_lbl)
        self.bpm_splt.addWidget(self.bpm_val_lbl)

        self.Temp_splt.addWidget(self.temp_lbl)
        self.Temp_splt.addWidget(self.Temp_t1t2_splt)

        self.Temp_t1t2_splt.addWidget(self.temp_lbl_t1)
        self.Temp_t1t2_splt.addWidget(self.temp_lbl_t2)

        self.spo2_splt.addWidget(self.spo2_label)
        self.spo2_splt.addWidget(self.spo2_val_label)
        self.spo2_splt.addWidget(self.spo2bar_splt)
        for spo2_bar in self.spo2_bars:
            self.spo2bar_splt.addWidget(spo2_bar)
        
        self.nıbp_splt.addWidget(self.nıbp_lbl)
        self.nıbp_splt.addWidget(self.nıbp_val_lbl)

        self.resp_splt.addWidget(self.resp_lbl)
        self.resp_splt.addWidget(self.resp_val_lbl)

        graph_splt.addWidget(plotwidget_a)
        graph_splt.addWidget(plotwidget_b)
        graph_splt.addWidget(plotwidget_c)
        graph_splt.addWidget(plotwidget_d)
        graph_splt.addWidget(plotwidget_e)

        value_splt.addWidget(self.bpm_splt)
        value_splt.addWidget(self.spo2_splt)
        value_splt.addWidget(self.nıbp_splt)
        value_splt.addWidget(self.resp_splt)
        value_splt.addWidget(self.Temp_splt)
        value_splt.addWidget(self.co2_lbl)
        

        layout.addWidget(graph_splt)
        layout.addWidget(value_splt)

        self.spo2_index = 0
        self.direction = 1

        self.setCentralWidget(widget)


    def update_bpm_signal(self):
        if self.index_a >= self.length_main_a:
            self.index_a = 0
        
        else:
            self.amplitude_array_a.append(self.amplitude_a[self.index_a])
            x_axis = list(range(len(self.amplitude_array_a)))
            
            if len(self.amplitude_array_a) == 350:
                self.amplitude_array_a.pop(0)
                if len(self.amplitude_array_a) != len(x_axis):
                    x_axis.pop()

            if self.amplitude_array_a[len(self.amplitude_array_a) - 1 ] >= self.A_R_wave.copy().pop():
                self.bpm_audio.play()

            self.line_a.setData(x_axis,self.amplitude_array_a)
        
            self.index_a += 1
    
    def update_spo2_signal(self):
        if self.index_b >= self.length_main_b:
            self.index_b = 0
        
        else:
            self.dynamic_array_b.append(self.amplitude_b[self.index_b])
            x_axis = list(range(len(self.dynamic_array_b)))

            if len(self.dynamic_array_b) >= 350:
                self.dynamic_array_b.pop(0)
                if len(x_axis) != len(self.dynamic_array_b):
                    x_axis.pop()
            

            self.index_b += 1

            self.line_b.setData(x_axis,self.dynamic_array_b)
            
    def update_saturation_signal(self):
        if self.index_c >= self.length_main_c:
            self.index_c = 0
        
        else:
            self.dynamic_array_c.append(self.amplitude_c[self.index_c] + 0.01)
            x_axis = list(range(len(self.dynamic_array_c)))

            if len(self.dynamic_array_c) >= 110:
                self.dynamic_array_c.pop(0)
                if len(x_axis) != len(self.dynamic_array_c):
                    x_axis.pop()
            

            self.index_c += 1

            self.line_c.setData(x_axis,self.dynamic_array_c)

    def update_co2_signal(self):
        if self.index_d >= self.length_main_d:
            self.index_d = 0
        
        else:
            data = list(np.sin(np.linspace(0,10,100)))[self.index_d]
            self.dynamic_array_d.append(data)
            
            x_axis = list(range(len(self.dynamic_array_d)))

            if len(self.dynamic_array_d) >= 250:
                self.dynamic_array_d.pop(0)
                if len(x_axis) != len(self.dynamic_array_d):
                    x_axis.pop()
            

            self.index_d += 1

            self.line_d.setData(x_axis,self.dynamic_array_d)

    def update_etCo2_signal(self):
        if self.index_e >= self.length_main_e:
            self.index_e = 0
        
        else:
            self.dynamic_array_e.append(self.amplitude_e[self.index_e])
            
            x_axis = list(range(len(self.dynamic_array_e)))

            if len(self.dynamic_array_e) >= 100:
                self.dynamic_array_e.pop(0)
                if len(x_axis) != len(self.dynamic_array_e):
                    x_axis.pop()
            

            self.index_e += 1

            self.line_e.setData(x_axis,self.dynamic_array_e)
    
    def update_spo2_breath_bars(self):
        if self.direction == 1:
            if self.spo2_index < len(self.spo2_bars):
                self.spo2_bars[self.spo2_index].setStyleSheet('background-color:black')
                self.spo2_index += 1
            
            else:
                self.direction = -1
        
        else:
            if self.spo2_index == 0:
                self.direction = 1
            
            else:
                self.spo2_bars[self.spo2_index - 1].setStyleSheet('background-color:green')
                self.spo2_index -= 1

if __name__=="__main__":
    sp = QApplication([])
    sw = mainF()
    sw.show()
    _s.exit(sp.exec())
