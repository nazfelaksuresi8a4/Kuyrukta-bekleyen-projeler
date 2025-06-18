from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as QtFigureCanvasKit 
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT 
import matplotlib.pyplot as plt
import sys as _s
import numpy as np
import pyqtgraph as pg
import winsound as ws


class mainUİ(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Waw file analysis program')

        #program-widgets
        main_widget = QWidget()

        self.setCentralWidget(main_widget)

        left_widget = QWidget()
        right_widget = QWidget()
        graph_settings_widget = QWidget()

        #zone-1-main))
        self.splt_1_v = QSplitter(Qt.Vertical)
        self.splt_2_v = QSplitter(Qt.Vertical)
        
        #zone-2-second))
        self.splt_3_h = QSplitter(Qt.Horizontal)
        self.splt_4_v = QSplitter(Qt.Vertical)
        self.splt_5_v = QSplitter(Qt.Vertical)

        self.splt_4_1 = QSplitter(Qt.Vertical)
        self.splt_4_2 = QSplitter(Qt.Vertical)
        
        #widget-settings
        main_layout = QHBoxLayout()
        left_layout = QHBoxLayout()
        graph_settings_screen_layout = QHBoxLayout()
        right_layout = QVBoxLayout()

        main_widget.setLayout(main_layout)
        left_widget.setLayout(left_layout)
        right_widget.setLayout(right_layout)
        graph_settings_widget.setLayout(graph_settings_screen_layout)

        main_layout.addWidget(left_widget)
        main_layout.addWidget(right_widget)

        left_layout.addWidget(self.splt_1_v)
        left_layout.addWidget(self.splt_2_v)

        right_layout.addWidget(self.splt_3_h)
        right_layout.addWidget(self.splt_4_v)
        right_layout.addWidget(self.splt_5_v)

        #widgets-tools
        self.visulaizer_label = QLabel(text='Ses grafiği')

        self.fig = Figure(figsize=(5,4))
        self.canvas = QtFigureCanvasKit(self.fig)

        self.median_button_icons = ["❚❚",
                                    "▶"]

        self.back = QPushButton(text='⏮')
        self.stop = QPushButton(text="▶")
        self.forward = QPushButton(text='⏭')

        self.graph_settings_label = QLabel(text='Grafik seçenekleri || Grafik Ayarları')
        self.graph_settings_label.setAlignment(Qt.AlignCenter)

        self.check_boxes_with_graph_settings = [QCheckBox(text='Çizgi Grafiği (PLOT)'),QCheckBox(text='Ampirik kümülatif dağılım grafiği'),QCheckBox(text='Histogram grafiği (HİST)'),QCheckBox(text='Bar grafiği (BAR)')]

        self.graph_apperance_settings = [QLabel(text='İncelik/kalınlık'),QSpinBox(),QLabel(text='Yükseklik(historgamlar için)'),QSpinBox(),QLabel(text='Grafik Rengi'),QComboBox(),QLabel(text='Grafik monitörü plan rengi'),QComboBox()]

        self.colors = ['Kırmızı','Mavi','Sarı','Yeşil','Turuncu','Beyaz']

        self.graph_apperance_settings[1].setRange(0,10)
        self.graph_apperance_settings[3].setRange(0,50)
        
        for graph_colors in self.colors: 
            self.graph_apperance_settings[5].addItem(graph_colors)
            self.graph_apperance_settings[len(self.graph_apperance_settings)-1].addItem(graph_colors)

        self.back.setMaximumWidth(30)
        self.stop.setMaximumWidth(30)
        self.forward.setMaximumWidth(30)

        self.volume_slider = QSlider()
        self.volume_slider.setRange(0,100)
        self.volume_slider.setValue(50)
        self.volume_slider.setMaximumSize(40,QWIDGETSIZE_MAX)

        self.volume_indicator = QLabel('Ses seviyesi: %50')
        self.volume_indicator.setAlignment(Qt.AlignCenter)

        self.file_system_label = QLabel('Dosya sistemi')
        self.file_system_label.setAlignment(Qt.AlignCenter)

        self.root_path_input = QLineEdit()
        self.root_path_input.setPlaceholderText('set file system path....')

        self.root_path_apply_button = QPushButton(text='Girilen dizini tanımla')

        self.file_sys_model = QFileSystemModel()
        self.file_system_view = QTreeView()
        self.file_system_view.setModel(self.file_sys_model)

        #widget-tools-settings

        self.splt_1_v.addWidget(self.volume_indicator)
        self.splt_1_v.addWidget(self.volume_slider)

        self.splt_2_v.addWidget(self.file_system_label)
        self.splt_2_v.addWidget(self.root_path_input)
        self.splt_2_v.addWidget(self.root_path_apply_button)
        self.splt_2_v.addWidget(self.file_system_view)

        self.splt_3_h.addWidget(self.back)
        self.splt_3_h.addWidget(self.stop)
        self.splt_3_h.addWidget(self.forward)

        self.splt_4_v.addWidget(graph_settings_widget)
        
        graph_settings_screen_layout.addWidget(self.splt_4_1)
        graph_settings_screen_layout.addWidget(self.splt_4_2)

        for graph_settings_1 in self.check_boxes_with_graph_settings:
            self.splt_4_1.addWidget(graph_settings_1)
        
        for graph_settings_2 in self.graph_apperance_settings:
            self.splt_4_2.addWidget(graph_settings_2) 

        self.splt_5_v.addWidget(self.visulaizer_label)
        self.splt_5_v.addWidget(self.canvas)    

        #menu bars
        self.main_menu_bar = self.menuBar()

        self.file_menu = self.main_menu_bar.addMenu('File')
        self.view_menu = self.main_menu_bar.addMenu('View')
        self.help_menu = self.main_menu_bar.addMenu('Help')







if __name__=="__main__":
    sp = QApplication([])
    sw = mainUİ()
    sw.show()
    _s.exit(sp.exec_())
