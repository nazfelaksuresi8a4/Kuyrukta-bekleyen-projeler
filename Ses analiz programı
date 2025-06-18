#Bu projede PYQT5-Pyside gui içeren modüler ve tasarımsal olarak modern bir program yazıcaz

#ne kadar basit gözüksede bazen o kadar g*t s*kici çıkabiliyorki ben bile şaşırıyom @mına koyim

#neyse işte kullnacağım modüller bence şunlar alta yazıcam amk yana ne bakıyon neyse bu arada yeni modül/framework eklenebilir haberin olsun 

#sonra neden böyle oldu deme 

#bazı modüller: 1-wave 2-csv 3-numpy 4-asyncio 5-time 6-datetime

#Bazı FrameWork'ler: PyQt5/PySide (belkide ekstra olarak Tkİnter)


#Burayada kodu yazacam amk işte Lan salakmısın üste değil alttaki boş satırlara yazıcam#


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
from tkinter import messagebox
import winsound as ws
import pygame as pyg
import datetime as dt
import random as _rd
import wave 
from pyqtgraph import exporters

class mainUİ(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Waw file analysis program')

        plt.style.use('dark_background')

        #program-widgets
        main_widget = QWidget()

        self.setCentralWidget(main_widget)

        left_widget = QWidget()
        right_widget = QWidget()
        graph_settings_widget = QWidget()
        self.menu_widget = QWidget()
        self.sound_file_info_widget = QWidget()

        self.sound_file_info_widget.setObjectName('sound_file_info_separator')
        self.menu_widget.setObjectName('side_menu')

        #zone-1-main))

        self.splt_1_v = QSplitter(Qt.Vertical)
        self.splt_2_v = QSplitter(Qt.Vertical)
        
        #zone-2-second))
        self.splt_3_h = QSplitter(Qt.Horizontal)
        self.splt_4_v = QSplitter(Qt.Vertical)
        self.splt_5_v = QSplitter(Qt.Vertical)

        self.splt_4_1 = QSplitter(Qt.Vertical)
        self.splt_4_2 = QSplitter(Qt.Vertical)

        self.sound_info_label_splt = QSplitter(Qt.Vertical)
        
        #widget-settings
        menu_layout = QVBoxLayout()
        main_layout = QHBoxLayout()

        left_layout = QHBoxLayout()
        right_layout = QVBoxLayout()

        graph_settings_screen_layout = QHBoxLayout()
        sound_file_info_screen_layout = QVBoxLayout()

        main_widget.setLayout(main_layout)

        left_widget.setLayout(left_layout)
        right_widget.setLayout(right_layout)

        graph_settings_widget.setLayout(graph_settings_screen_layout)
        self.sound_file_info_widget.setLayout(sound_file_info_screen_layout)

        self.menu_widget.setLayout(menu_layout)

        main_layout.addWidget(self.menu_widget)
        main_layout.addWidget(left_widget)
        main_layout.addWidget(right_widget)
        main_layout.addWidget(self.sound_file_info_widget)

        left_layout.addWidget(self.splt_1_v)
        left_layout.addWidget(self.splt_2_v)

        right_layout.addWidget(self.splt_3_h)
        right_layout.addWidget(self.splt_4_v)
        right_layout.addWidget(self.splt_5_v)


        #third-party-widgets#
        fun_label = QLabel(text='EĞLENCE')
        fun_label.setAlignment(Qt.AlignCenter)
        fun_label.setMaximumHeight(40)
        fun_label.setObjectName('menu_widget_fun_label')

        start_anim_graph_sin = QPushButton(text='Animasyonlu sinüs grafiği başlat')
        start_anim_graph_sincos = QPushButton(text='Animasyonlu kosinüs grafiği başlat')
        start_anim_graph_foo = QPushButton(text='Animasyonlu gürültü grafiği başlat')
        stop_all_anims = QPushButton(text='Animasyonlu grafiği durdur')

        menu_layout.addWidget(fun_label)
        menu_layout.addWidget(start_anim_graph_sin)
        menu_layout.addWidget(start_anim_graph_sincos)
        menu_layout.addWidget(start_anim_graph_foo)
        menu_layout.addWidget(stop_all_anims)

        self.menu_widget.setFixedWidth(0)

        #widgets-tools
        self.apply_sound_file = QPushButton('Ses dosyasını tanımla')
        self.procces_sound_file = QPushButton('Ses dosyasını işle')

        self.sound_info_labels = [
            QLabel('Ses dosyası bilgileri'),
            QPushButton(text='Ses kanalı: ??'),
            QPushButton(text='Sesin süresi: ??'),
            QPushButton(text='Sesin bit sayısı: ??'),
            QPushButton(text='Ses dosyası Kaç HZ: ??')
                                ]

        self.sound_info_labels[0].setObjectName('sound_info_label')
        
        sound_file_info_screen_layout.addWidget(self.sound_info_label_splt)

        self.sound_info_label_splt.addWidget(self.sound_info_labels[0])

        
        for info_label_index in range(1,len(self.sound_info_labels)):
            self.sound_info_labels[info_label_index].setEnabled(False)
            self.sound_info_label_splt.addWidget(self.sound_info_labels[info_label_index])

        self.hide_preverius_graph = QPushButton('Önizleme grafiğini sıfırla')
        self.show_preverius_graph = QPushButton('Rastgele önizleme grafiği')
        self.save_graph = QPushButton('Monitördeki Grafiği kaydet')

        self.visulaizer_label = QLabel(text='Ses grafiği')

        self.plot_item = self.canvas = pg.PlotWidget()
        self.canvas.plot(np.random.normal(0,10,50),pen='w')
        self.canvas.setBackground("#000000")

        self.median_button_icons = ["❚❚",
                                    "▶"]

        self.back = QPushButton(text='⏮')
        self.stop = QPushButton(text="▶")
        self.forward = QPushButton(text='⏭')

        self.graph_settings_label = QLabel(text='Grafik seçenekleri || Grafik Ayarları')
        self.graph_settings_label.setAlignment(Qt.AlignCenter)

        self.check_boxes_with_graph_settings = [QCheckBox(text='Çizgi Grafiği (PLOT)'),QCheckBox(text='Ampirik kümülatif dağılım grafiği'),QCheckBox(text='Histogram grafiği (HİST)'),QCheckBox(text='Bar grafiği (BAR)')]

        self.graph_apperance_settings = [QLabel(text='İncelik/kalınlık'),QSpinBox(),QLabel(text='Yükseklik(historgamlar için)'),QSpinBox(),QLabel(text='Grafik Rengi'),QComboBox(),QLabel(text='Grafik monitörü arka plan rengi'),QComboBox()]

        self.colors = ['Kırmızı','Mavi','Sarı','Yeşil','Turuncu','Beyaz']

        self.graph_apperance_settings[1].setRange(0,10)
        self.graph_apperance_settings[3].setRange(0,50)
        
        for graph_colors in self.colors: 
            self.graph_apperance_settings[5].addItem(graph_colors)
            self.graph_apperance_settings[len(self.graph_apperance_settings)-1].addItem(graph_colors)

        self.graph_apperance_settings[5].setCurrentIndex(1)

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
        self.root_path_input.setAlignment(Qt.AlignCenter)
        self.root_path_input.setPlaceholderText('set file system path....')

        self.root_path_apply_button = QPushButton(text='Girilen dizini tanımla')
        self.root_path_reset_button = QPushButton(text='Dosya sistemi dizinin sıfırla')

        self.file_sys_model = QFileSystemModel()
        self.file_sys_model.setRootPath('/')

        self.main_rootpath = self.file_sys_model.index('')

        self.file_system_view = QTreeView()
        self.file_system_view.setModel(self.file_sys_model)

        self.file_system_view.setRootIndex(self.file_sys_model.index(r'C:\Users\alper\Desktop\ftp'))

        #widget-tools-settings

        self.splt_1_v.addWidget(self.volume_indicator)
        self.splt_1_v.addWidget(self.volume_slider)

        self.splt_2_v.addWidget(self.file_system_label)
        self.splt_2_v.addWidget(self.root_path_input)
        self.splt_2_v.addWidget(self.root_path_apply_button)
        self.splt_2_v.addWidget(self.root_path_reset_button)
        self.splt_2_v.addWidget(self.file_system_view)
        self.splt_2_v.addWidget(self.apply_sound_file)
        self.splt_2_v.addWidget(self.procces_sound_file)

        container_widget = QWidget()
        container_layout = QHBoxLayout()
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)

        container_widget.setLayout(container_layout)

        self.compressor_widgets = [
            QPushButton(),
            QPushButton(),
            QPushButton(),
            QPushButton(),
            QPushButton(f'Mevcut seçili ses dosyası: --Seçilmedi--'),

                            ]

        self.compressor_widgets[4].setEnabled(False)

        for compressors in self.compressor_widgets:
            compressors.setStyleSheet('background-color:54, 54, 54;border:none')
            container_layout.addWidget(compressors)

        main_lbl = QLabel(text='Geri sar || Durdur/Başlat || Başa sar')
        container_layout.addWidget(main_lbl)

        container_layout.addWidget(self.back,alignment=Qt.AlignCenter)
        container_layout.addWidget(self.stop,alignment=Qt.AlignCenter)
        container_layout.addWidget(self.forward,alignment=Qt.AlignCenter)

        self.splt_3_h.addWidget(container_widget)

        self.splt_4_v.addWidget(graph_settings_widget)

        self.splt_1_v.setObjectName('splt_1')
        self.splt_2_v.setObjectName('splt_2')
        self.splt_3_h.setObjectName('splt_3')
        self.splt_4_v.setObjectName('splt_4')
        self.splt_5_v.setObjectName('splt_5')
        self.splt_4_1.setObjectName('splt_4_1')
        self.splt_4_2.setObjectName('splt_4_2')
        
        graph_settings_screen_layout.addWidget(self.splt_4_1)
        graph_settings_screen_layout.addWidget(self.splt_4_2)

        for graph_settings_1 in self.check_boxes_with_graph_settings:
            self.splt_4_1.addWidget(graph_settings_1)
        
        for graph_settings_2 in self.graph_apperance_settings:
            self.splt_4_2.addWidget(graph_settings_2) 

        self.splt_5_v.addWidget(self.visulaizer_label)
        self.splt_5_v.addWidget(self.canvas)    
        self.splt_5_v.addWidget(self.hide_preverius_graph)
        self.splt_5_v.addWidget(self.show_preverius_graph)
        self.splt_5_v.addWidget(self.save_graph)

        #menu bars
        self.main_menu_bar = self.menuBar()

        self.file_menu = self.main_menu_bar.addMenu('Dosya')
        self.view_menu = self.main_menu_bar.addMenu('Görüntü')
        self.help_menu = self.main_menu_bar.addMenu('Yardım')
        self.horizontal_menu_menu = self.main_menu_bar.addMenu('Yan menü')
        self.horizontal_menu_menu_btn = self.horizontal_menu_menu.addAction('Eğlence menüsünü aç')

        self.visulaizer_label.setAlignment(Qt.AlignCenter)

        self.visulaizer_label.setObjectName('visulaizer_label')
        self.back.setObjectName('back')
        self.stop.setObjectName('stop')
        self.forward.setObjectName('forward')
        self.volume_indicator.setObjectName('volume_indicator')
        self.volume_slider.setObjectName('volume_slider')
        self.file_system_label.setObjectName('file_system_label')
        self.file_system_view.setObjectName('file_system_view')
        self.root_path_input.setObjectName('root_path_input')
        self.root_path_apply_button.setObjectName('root_path_button')
        self.graph_apperance_settings[1].setObjectName('spinbox_1')
        self.graph_apperance_settings[3].setObjectName('spinbox_2')
        self.graph_apperance_settings[5].setObjectName('checkbox_1')
        self.graph_apperance_settings[len(self.graph_apperance_settings)-1].setObjectName('checkbox_1')
        self.setObjectName('main_window')

        #widget_size_optimizes#
        self.optimize_timer = QTimer()
        self.optimize_timer.timeout.connect(self.optimize_widget_sizes)
        self.optimize_timer.start(1)

        #menubar_animation_values/
        self.menubar_open = False

        #menubar_animations fresh anim/
        self.menubar_prop_animation = QPropertyAnimation(self.menu_widget,b'maximumWidth')

        #slots/event-handling/
        self.volume_slider.valueChanged.connect(self.slider_value_updater)
        self.root_path_apply_button.clicked.connect(self.file_system_root_path_updater)
        self.root_path_reset_button.clicked.connect(self.file_system_root_path_reseter)
        self.horizontal_menu_menu_btn.triggered.connect(self.trigger_side_menu)
        self.hide_preverius_graph.clicked.connect(self.hide_graph)
        self.show_preverius_graph.clicked.connect(self.show_graph)
        self.apply_sound_file.clicked.connect(self.sound_file_select_event)
        self.procces_sound_file.clicked.connect(self.procces_sound_file_event)

        #CSS Side/

        css_file = open(r'program_qss.css','r')

        readed_css_file = css_file.read()

        self.setStyleSheet(readed_css_file) 

        plotİtem = self.plot_item.getPlotItem()

        exporter = exporters.ImageExporter(plotİtem)
        exporter.export('ananin_ami.png')
    
    def procces_sound_file_event(self):
        current = self.file_system_view.currentIndex()
        file_path = self.file_sys_model.filePath(current)

        file_exception_value = bool(0)

        try:
            sound_file = wave.open(file_path)

        except:
            file_is_not_waw_error = messagebox.showwarning(title='Dosya türü hatası!',message='Lütfen bir .WAV dosyası seçin ve daha sonra tekrar deneyin!')

            file_exception_value = bool(1)
        
        if file_exception_value == bool(0):
            self.sound_file_channels = sound_file.getnchannels()

            self.sound_file_time = f'{sound_file.getnframes() / sound_file.getframerate():.2f}'

            self.sound_file_hz = sound_file.getframerate()

            if self.sound_file_channels == 2:
                self.sound_info_labels[1].setText(f'Sesin kanal türü: STERO')
            
            else:
                self.sound_info_labels[1].setText(f'Sesin kanal türü: MONO')

            self.sound_info_labels[2].setText(f'Sesin süresi: {self.sound_file_time} Saniye')
            self.sound_info_labels[3].setText(f'Sesin bit sayısı: {self.sound_file_channels*8}') 
            self.sound_info_labels[4].setText(f'Sesin HZ sayısı: {self.sound_file_hz}') 
        
        else:
            print('File is not valid!')


    def sound_file_select_event(self):
        current = self.file_system_view.currentIndex()
        file_path = self.file_sys_model.filePath(current)

        self.compressor_widgets[4].setText(f'Mevcut seçili ses dosyası: {self.file_sys_model.fileName(current)}')
       
    def hide_graph(self):
        self.canvas.clear()
        self.canvas.plot([1 for i in range(50)],pen='w')
    
    def show_graph(self):
        choose = _rd.randint(0,1)

        if choose == 0:
            self.canvas.clear()

            self.canvas.plot(np.random.normal(0,10,50),pen='w')

        elif choose == 1:
            self.canvas.clear()

            self.canvas.plot([_rd.randint(0,20) for x in range(20)],pen='w')

    def optimize_widget_sizes(self):
        self.volume_indicator.setMaximumHeight(self.file_system_label.height())
        self.volume_indicator.setMinimumHeight(self.file_system_label.height())
        self.file_system_label.setMaximumHeight(self.volume_indicator.height())
        self.file_system_label.setMinimumHeight(self.volume_indicator.height())
        self.sound_info_labels[0].setMaximumHeight(self.volume_indicator.height())
        self.sound_info_labels[0].setMinimumHeight(self.volume_indicator.height())

    def trigger_side_menu(self):
        if self.menubar_open == False:
            self.menubar_prop_animation.setDuration(300)
            self.menubar_prop_animation.setStartValue(0)
            self.menubar_prop_animation.setEndValue(300)
            self.menubar_prop_animation.start()

            self.menubar_open = True

        elif self.menubar_open == True:
            self.menubar_prop_animation.setDuration(300)
            self.menubar_prop_animation.setStartValue(300)
            self.menubar_prop_animation.setEndValue(0)
            self.menubar_prop_animation.start()

            self.menubar_open = False

    def menubar_animation_handler(self):
        if self.menubar_open == False or self.menubar_open == bool(0):
            if self.side_menu_open_index >= 140:
                self.menubar_animation_timer.stop()
                self.side_menu_open_index == 0

                return 0

            self.side_menu_open_index += 1

            self.menu_widget.setFixedWidth(self.side_menu_open_index)

    def slider_value_updater(self):
        self.slider_current_value = self.volume_slider.value()

        self.volume_indicator.setText(f'Ses seviyesi: {self.slider_current_value}')
        self.volume_indicator.setMinimumHeight(self.file_system_label.height())
        self.volume_indicator.setMaximumHeight(self.file_system_label.height())

    def file_system_root_path_updater(self):
        self.current_index = self.file_system_view.currentIndex()
        self.current_root_path = self.root_path_input.text()

        if self.current_root_path == ' ' or self.current_root_path == '':
            messagebox.showwarning(title='Dizin tanımlama hatası!',message='Dizin tanımlanırken bir sorun oluştu lütfen dizini tekrar girip deneyiniz!')
        
        else:
            pass
        try:
            self.modelİndex = self.file_sys_model.index(self.current_root_path)

            self.file_system_view.setRootIndex(self.modelİndex)
        except:
            warning_message = messagebox

            messagebox.showerror(title='Dizin tanımlama hatası!',message='Dizin tanımlanırken kritik bir sorun oluştu lütfen tekrar deneyiniz')

        finally:
            if self.file_system_view.currentIndex() != self.current_index:
                messagebox.showwarning(title='Dizin tanımlama hatası!',message='Dizin tanımlanırken bir sorun oluştu lütfen dizini tekrar girip deneyiniz!')

            else:
                pass

    def file_system_root_path_reseter(self):
        self.file_system_view.setRootIndex(self.main_rootpath)
        self.file_system_view.update()

if __name__=="__main__":
    sp = QApplication([])
    sw = mainUİ()
    sw.show()
    _s.exit(sp.exec_())
