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

def check_system_datas():
    return _psu.cpu_stats()


def check_network_datas():
    return _psu.net_io_counters(pernic=False,nowrap=True)
     

class system_side():
    def system_monitor():
        _o.system('cls')

        bar = '|'
        max_bar_count = 64

        while True:
            cpu_statistic_datas_1 = check_system_datas()

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
            t2 = str(int(cpu_statistic_datas_2[1]))[len(t2l) - 1]
            t3 = str(int(cpu_statistic_datas_2[3]))[len(t3l) - 1]

            #print(t1,   t2,
            updated_bars_context_switches = bar*int(t1)
            spaces_context_switches = ' '*int(max_bar_count - int(t1l))
            updated_bars_interrupts = bar*int(t2)
            spaces_interrupts = ' '*int(max_bar_count - int(t2))
                                        
            updated_syscall_bars = bar*int(t3)
            spaces_syscall = ' '*int(max_bar_count - int(t3))
            print(Fore.RED,f'\033[1;0Hcpu kullanımı: {cpu_percent_datas}           [{updated_bars_cpu_percent}{spaces_cpu_percent}]')
            print('\033[2;0H----'*20)
            print(Fore.GREEN,f'\033[3;0HBağlam anahtarları: {cpu_statistic_datas_2[0] - cpu_statistic_datas_1[0] }    [{updated_bars_context_switches}{spaces_context_switches}]')
            print('\033[4;0H----'*20)
            print(Fore.BLUE,f'\033[5;0HKesintiler: {cpu_statistic_datas_2[1] - cpu_statistic_datas_1[1]}            [{updated_bars_interrupts}{spaces_interrupts}]')
            print('\033[6;0H----'*20)
            print(Fore.YELLOW,f'\033[7;0HHafif kesintiler: {cpu_statistic_datas_2[2]}          [{updated_bars_cpu_percent}{spaces_cpu_percent}]')
            print('\033[8;0H----'*20)
            print(Fore.RED,f'\033[9;0HSistem çağrıları: {cpu_statistic_datas_2[3] - cpu_statistic_datas_1[3]}      [{updated_syscall_bars}{spaces_syscall}]')
            print('\033[10;0H----'*20)
            print(Fore.GREEN,f'\033[11;0HMantıksal CPU Sayısı: {logical_cpu_count_datas}')
            print('\033[12;0H----'*20)
            print(Fore.CYAN,f'\033[13;0HFiziksel CPU Sayısı: {unlogical_cpu_count_datas}')
            print()
            print()
            print('DURDURMAK İÇİN [SPACE]',end='\r')

            if _kb.is_pressed('space'):
                print(Fore.LIGHTRED_EX,'\b\n\ndurduruldu')
                _ts(2)
                print(Fore.BLUE,Style.DIM)
                _o.system('cls')
                mainUİ()
                break
    

def network_monitor():
                _o.system('cls')
                network_bar = '|'
                max_network_bar_count = 64

                while True:
                    network_x = check_network_datas()

                    _ts(0.2)
                    
                    network_y = _psu.net_io_counters(pernic=False,nowrap=True)

                    datas = [
                        int(str(int(str(network_y[0])) - int(str(network_x[0])))[0:1]),
                        int(str(int(str(network_y[1])) - int(str(network_x[1])))[0:1]),
                        int(str(int(str(network_y[2])) - int(str(network_x[2])))[0:1]),
                        int(str(int(str(network_y[3])) - int(str(network_x[3])))[0:1]) 
                    ]

                    network_bar_f_1 = network_bar * datas[0]*2
                    network_bar_f_2 = network_bar * datas[1]*2
                    network_bar_f_3 = network_bar * datas[2]*2
                    network_bar_f_4 = network_bar * datas[3]*2
                    network_bar_f_5 = network_bar * network_y[4]*2
                    network_bar_f_6 = network_bar * network_y[5]*2
                    network_bar_f_7 = network_bar * network_y[6]*2
                    network_bar_f_8 = network_bar * network_y[7]*2


                    netwok_bar_f_space_1 = ' ' * int(max_network_bar_count - datas[0]) 
                    netwok_bar_f_space_2 = ' ' * int(max_network_bar_count - datas[1]) 
                    netwok_bar_f_space_3 = ' ' * int(max_network_bar_count - datas[2]) 
                    netwok_bar_f_space_4 = ' ' * int(max_network_bar_count - datas[3]) 
                    netwok_bar_f_space_5 = ' ' * int(max_network_bar_count - network_y[4]) 
                    netwok_bar_f_space_6 = ' ' * int(max_network_bar_count - network_y[5]) 
                    netwok_bar_f_space_7 = ' ' * int(max_network_bar_count - network_y[6]) 
                    netwok_bar_f_space_8 = ' ' * int(max_network_bar_count - network_y[7]) 

                    
                    print(Fore.LIGHTRED_EX,Style.BRIGHT,f'\033[1;0HAğ Hızı: {network_y[0] - network_x[0]}                 [{network_bar_f_1}{netwok_bar_f_space_1}')
                    print('\033[2;0H----'*20)
                    print(Fore.LIGHTGREEN_EX,Style.BRIGHT,f'\033[3;0HAğ kullanımı: {network_y[1] - network_x[1]}            [{network_bar_f_2}{netwok_bar_f_space_2}')
                    print('\033[4;0H----'*20)
                    print(Fore.LIGHTBLUE_EX,Style.BRIGHT,f'\033[5;0HPaket gönderildi: {network_y[2] - network_x[2]}        [{network_bar_f_3}{netwok_bar_f_space_3}')
                    print('\033[6;0H----'*20)
                    print(Fore.LIGHTYELLOW_EX,Style.BRIGHT,f'\033[7;0HPaket alındı: {network_y[3] - network_x[3]}            [{network_bar_f_4}{netwok_bar_f_space_4}')
                    print('\033[8;0H----'*20)
                    print(Fore.LIGHTCYAN_EX,Style.BRIGHT,f'\033[9;0HHatalı paketler[Alıcı]: {network_y[4] - network_x[4]}  [{network_bar_f_5}{netwok_bar_f_space_5}')
                    print('\033[10;0H----'*20)
                    print(Fore.LIGHTGREEN_EX,Style.BRIGHT,f'\033[11;0HHatalı paketler[Verici]: {network_y[5] - network_x[5]} [{network_bar_f_6}{netwok_bar_f_space_6}')
                    print('\033[12;0H----'*20)
                    print(Fore.LIGHTBLUE_EX,Style.BRIGHT,f'\033[13;0HAğdan kopan cihazlar: {network_y[6] - network_x[6]}    [{network_bar_f_7}{netwok_bar_f_space_7}')
                    print('\033[14;0H----'*20)
                    print(Fore.LIGHTYELLOW_EX,Style.BRIGHT,f'\033[15;0HAğa bağlanan cihazlar:: {network_y[7] - network_x[7]}  [{network_bar_f_8}{netwok_bar_f_space_8}')
                    print()
                    print()
                    print('DURDURMAK İÇİN [SPACE]',end='\r')

                    
                    if _kb.is_pressed('space'):
                        print(Fore.LIGHTRED_EX,'\b\n\ndurduruldu')
                        _ts(2)
                        print(Fore.BLUE,Style.DIM)
                        _o.system('cls')
                        mainUİ()
                        break

def all_monitors():
                _o.system('cls')

                bar = '|'
                max_bar_count = 64

                while True:
                    cpu_statistic_datas_1 = check_system_datas()
                    network_x = check_network_datas()

                    cpu_percent_datas = _psu.cpu_percent(interval=0.2)
                    cpu_statistic_datas_2 = _psu.cpu_stats()

                    logical_cpu_count_datas,unlogical_cpu_count_datas = _psu.cpu_count(logical=True), _psu.cpu_count(logical=False) 
                    percpu_cpu_times,percpu_cpu_time_percents = _psu.cpu_times(percpu=True), _psu.cpu_times_percent(interval=0.1,percpu=True)

                    network_y = _psu.net_io_counters(pernic=False,nowrap=True)

                    updated_bars_cpu_percent = bar*int(cpu_percent_datas)
                    spaces_cpu_percent = ' '*int(max_bar_count - cpu_percent_datas)

                    t1l = str(int(cpu_statistic_datas_2[0]))
                    t2l = str(int(cpu_statistic_datas_2[1]))
                    t3l = str(int(cpu_statistic_datas_2[3]))

                    t1 = str(int(cpu_statistic_datas_2[0]))[len(t1l) - 1]
                    t2 = str(int(cpu_statistic_datas_2[1]))[len(t2l) - 1]
                    t3 = str(int(cpu_statistic_datas_2[3]))[len(t3l) - 1]

                    #print(t1,   t2,    t3)

                    updated_bars_context_switches = bar*int(t1)
                    spaces_context_switches = ' '*int(max_bar_count - int(t1))

                    updated_bars_interrupts = bar*int(t2)
                    spaces_interrupts = ' '*int(max_bar_count - int(t2))
                                                 
                    updated_syscall_bars = bar*int(t3)
                    spaces_syscall = ' '*int(max_bar_count - int(t3))

                    network_bar = '|'
                    max_network_bar_count = 64

                    datas = [
                            int(str(int(str(network_y[0])) - int(str(network_x[0])))[0:1]),
                            int(str(int(str(network_y[1])) - int(str(network_x[1])))[0:1]),
                            int(str(int(str(network_y[2])) - int(str(network_x[2])))[0:1]),
                            int(str(int(str(network_y[3])) - int(str(network_x[3])))[0:1]) 
                        ]

                    network_bar_f_1 = network_bar * datas[0]*2
                    network_bar_f_2 = network_bar * datas[1]*2
                    network_bar_f_3 = network_bar * datas[2]*2
                    network_bar_f_4 = network_bar * datas[3]*2
                    network_bar_f_5 = network_bar * network_y[4]*2
                    network_bar_f_6 = network_bar * network_y[5]*2
                    network_bar_f_7 = network_bar * network_y[6]*2
                    network_bar_f_8 = network_bar * network_y[7]*2


                    netwok_bar_f_space_1 = ' ' * int(max_network_bar_count - datas[0]) 
                    netwok_bar_f_space_2 = ' ' * int(max_network_bar_count - datas[1]) 
                    netwok_bar_f_space_3 = ' ' * int(max_network_bar_count - datas[2]) 
                    netwok_bar_f_space_4 = ' ' * int(max_network_bar_count - datas[3]) 
                    netwok_bar_f_space_5 = ' ' * int(max_network_bar_count - network_y[4]) 
                    netwok_bar_f_space_6 = ' ' * int(max_network_bar_count - network_y[5]) 
                    netwok_bar_f_space_7 = ' ' * int(max_network_bar_count - network_y[6]) 
                    netwok_bar_f_space_8 = ' ' * int(max_network_bar_count - network_y[7]) 

                    print()
                    print(f'\033[1;0H-----SİSTEM MONİTÖRÜ-----')
                    print()
                    print()
                    print(Fore.RED,f'\033[2;0Hcpu kullanımı: {cpu_percent_datas}           [{updated_bars_cpu_percent}{spaces_cpu_percent}]')
                    print('\033[3;0H----'*20)
                    print(Fore.GREEN,f'\033[4;0HBağlam anahtarları: {cpu_statistic_datas_2[0] - cpu_statistic_datas_1[0] }    [{updated_bars_context_switches}{spaces_context_switches}]')
                    print('\033[5;0H----'*20)
                    print(Fore.BLUE,f'\033[6;0HKesintiler: {cpu_statistic_datas_2[1] - cpu_statistic_datas_1[1]}            [{updated_bars_interrupts}{spaces_interrupts}]')
                    print('\033[7;0H----'*20)
                    print(Fore.YELLOW,f'\033[8;0HHafif kesintiler: {cpu_statistic_datas_2[2]}          [{updated_bars_cpu_percent}{spaces_cpu_percent}]')
                    print('\033[9;0H----'*20)
                    print(Fore.RED,f'\033[10;0HSistem çağrıları: {cpu_statistic_datas_2[3] - cpu_statistic_datas_1[3]}      [{updated_syscall_bars}{spaces_syscall}]')
                    print('\033[11;0H----'*20)
                    print(Fore.GREEN,f'\033[12;0HMantıksal CPU Sayısı: {logical_cpu_count_datas}')
                    print('\033[13;0H----'*20)
                    print(Fore.CYAN,f'\033[14;0HFiziksel CPU Sayısı: {unlogical_cpu_count_datas}')      
                    print()
                    print('-----Ağ MONİTÖRÜ-----')
                    print('\033[17;0H')                
                    print(Fore.LIGHTRED_EX,Style.BRIGHT,f'\033[18;0HByte gönderildi: {network_y[0] - network_x[0]}                 [{network_bar_f_1}{netwok_bar_f_space_1}')
                    print('\033[19;0H----'*20)
                    print(Fore.LIGHTGREEN_EX,Style.BRIGHT,f'\033[20;0HByte alındı: {network_y[1] - network_x[1]}            [{network_bar_f_2}{netwok_bar_f_space_2}')
                    print('\033[21;0H----'*20)
                    print(Fore.LIGHTBLUE_EX,Style.BRIGHT,f'\033[22;0HPaket gönderildi: {network_y[2] - network_x[2]}        [{network_bar_f_3}{netwok_bar_f_space_3}')
                    print('\033[23;0H----'*20)
                    print(Fore.LIGHTYELLOW_EX,Style.BRIGHT,f'\033[24;0HPaket alındı: {network_y[3] - network_x[3]}            [{network_bar_f_4}{netwok_bar_f_space_4}')
                    print('\033[25;0H----'*20)
                    print(Fore.LIGHTCYAN_EX,Style.BRIGHT,f'\033[26;0HHatalı paketler[Alıcı]: {network_y[4] - network_x[4]}  [{network_bar_f_5}{netwok_bar_f_space_5}')
                    print('\033[27;0H----'*20)
                    print(Fore.LIGHTGREEN_EX,Style.BRIGHT,f'\033[28;0HHatalı paketler[Verici]: {network_y[5] - network_x[5]} [{network_bar_f_6}{netwok_bar_f_space_6}')
                    print('\033[29;0H----'*20)
                    print(Fore.LIGHTBLUE_EX,Style.BRIGHT,f'\033[30;0HAğdan kopan cihazlar: {network_y[6] - network_x[6]}    [{network_bar_f_7}{netwok_bar_f_space_7}')
                    print('\033[31;0H----'*20)
                    print(Fore.LIGHTYELLOW_EX,Style.BRIGHT,f'\033[32;0HAğa bağlanan cihazlar:: {network_y[7] - network_x[7]}  [{network_bar_f_8}{netwok_bar_f_space_8}')
                    print()
                    print('DURDURMAK İÇİN [SPACE]',end='\r')

                    
                    if _kb.is_pressed('space'):
                        print(Fore.LIGHTRED_EX,'\b\n\ndurduruldu')
                        _ts(2)
                        print(Fore.BLUE,Style.DIM)
                        _o.system('cls')
                        mainUİ()
                        break
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
                system_side.system_monitor()
            
            elif int(user_choose) == 2:
                network_monitor()
            
            elif(int(user_choose) == 3):
                all_monitors()
                

mainUİ()    

