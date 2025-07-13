import sys as _s 
import os as _o
import psutil as _psu
from time import sleep as _ts
import curses
import colorama as _c
import tqdm as _tq
import keyboard as _kb
from colorama import Back,Fore,Style,Cursor

format = """
 ____            _
/ ___| _   _ ___| |_ ___ _ __ ___  
\___ \| | | / __| __/ _ \ '_ ` _ \       _        __                            _               _   ___ 
 ___) | |_| \__ \ ||  __/ | | | | |     (_)_ __  / _| ___  _ __ _ __ ___   __ _| |_ ___  _ __  / | / _ \ 
|____/ \__, |___/\__\___|_| |_| |_|     | | '_ \| |_ / _ \| '__| '_ ` _ \ / _` | __/ _ \| '__| | || | | |
                                        | | | | |  _| (_) | |  | | | | | | (_| | || (_) | |    | || |_| |
                                        |_|_| |_|_|  \___/|_|  |_| |_| |_|\__,_|\__\___/|_|    |_(_)___/
"""

class mainUİ:
    def __init__(self):
        super().__init__()
        _c.init()
        
        allows = ['cpu_acces','network_acces',]

        print(Fore.BLUE,Style.BRIGHT,format)
        input('\n\nHer şey neredeyse hazır! Şimdi sadece izinlerini kontrol edicez. Devam etmek için [ENTER]')
        
        for i in range(len(allows)):
            logical = [True, False]

            try:
                cpu_Acces_low, cpu_acces_med, cpu_acces_high = _psu.cpu_stats(),_psu.cpu_count(logical=logical[i]),_psu.cpu_times(percpu=logical[i])

            except Exception as cpu_acces_error:
                print(f'cpu bilgilerine erişilirken bir sorun meydana geldi!\n\nhata:{cpu_acces_error}')

            try:
                net_Acces_low, net_acces_med, net_acces_high = _psu.net_connections(kind='inet'),_psu.net_if_addrs(),_psu.net_if_stats()

            except Exception as network_acces_error:
                print(f'Ağ bilgilerine erişilirken bir sorun meydana geldi!\n\nhata:{network_acces_error}')

        print(Fore.GREEN,Style.DIM,'\b\nTüm testler geçildi sistem başlatılıyor...')
        _ts(1.5)
        _o.system('cls')
        
        print(Fore.GREEN,Style.DIM,'\b\b------------------------------\b\n1-CPU monitörü\n------------------------------\n2-Network monitörü\n------------------------------\n3-Tüm monitörler')
        
        user_choose = input('$>> ')

        if user_choose.isdigit():
            if int(user_choose) == 1:
                _o.system('cls')

                bar = '|'
                max_bar_count = 64

                cpu_statistic_datas_1 = _psu.cpu_stats()
                while True:
                    cpu_percent_datas = _psu.cpu_percent(interval=0.1)
                    cpu_statistic_datas_2 = _psu.cpu_stats()

                    logical_cpu_count_datas,unlogical_cpu_count_datas = _psu.cpu_count(logical=True), _psu.cpu_count(logical=False) 
                    percpu_cpu_times,percpu_cpu_time_percents = _psu.cpu_times(percpu=True), _psu.cpu_times_percent(interval=0.1,percpu=True)

                    updated_bars_cpu_percent = bar*int(cpu_percent_datas)
                    spaces_cpu_percent = ' '*int(max_bar_count - cpu_percent_datas)

                    t1l = str(int(cpu_statistic_datas_2[0]))
                    t2l = str(int(cpu_statistic_datas_2[1]))
                    t3l = str(int(cpu_statistic_datas_2[3]))

                    t1 = str(int(cpu_statistic_datas_2[0]))[len(t1l) - 1]
                    t2 = str(int(cpu_statistic_datas_2[0]))[len(t1l) - 1]
                    t3 = str(int(cpu_statistic_datas_2[0]))[len(t1l) - 1]

                    #print(t1,   t2,    t3)

                    updated_bars_context_switches = bar*int(t1)
                    spaces_context_switches = ' '*int(max_bar_count - int(t1))

                    updated_bars_interrupts = bar*int(t2)
                    spaces_interrupts = ' '*int(max_bar_count - int(t2))
                                                 
                    updated_syscall_bars = bar*int(t3)
                    spaces_syscall = ' '*int(max_bar_count - int(t3))

                    print(Fore.RED,f'\033[1;0Hcpu kullanımı: {cpu_percent_datas}           [{updated_bars_cpu_percent}{spaces_cpu_percent}]')
                    print(Fore.GREEN,f'\033[2;0HBağlam anahtarları: {cpu_statistic_datas_2[0] - cpu_statistic_datas_1[0] }    [{updated_bars_context_switches}{spaces_context_switches}]')
                    print(Fore.BLUE,f'\033[3;0HKesintiler: {cpu_statistic_datas_2[1] - cpu_statistic_datas_1[1]}            [{updated_bars_interrupts}{spaces_interrupts}]')
                    print(Fore.YELLOW,f'\033[4;0HHafif kesintiler: {cpu_statistic_datas_2[2]}          [{updated_bars_cpu_percent}{spaces_cpu_percent}]')
                    print(Fore.RED,f'\033[5;0HSistem çağrıları: {cpu_statistic_datas_2[3] - cpu_statistic_datas_1[3]}      [{updated_syscall_bars}{spaces_syscall}]')
                    print(Fore.GREEN,f'\033[6;0HMantıksal CPU Sayısı: {logical_cpu_count_datas}')
                    print(Fore.CYAN,f'\033[7;0HFiziksel CPU Sayısı: {unlogical_cpu_count_datas}')
                    print()
                    print('DURDURMAK İÇİN [SPACE]',end='\r')
                    
                    if _kb.is_pressed(57):
                        print(Fore.LIGHTRED_EX,'\bdurduruldu')
                        _ts(2)
                        print(Fore.BLUE,Style.DIM)
                        _o.system('cls')
                        mainUİ()
                        break
                        
                    


mainUİ()    

