import os


class Start:

    def Banner():
        os.system('cls')
        from data import banner

    def start():
        Start.Banner()  
        from dumper.dumper import Dumper_Manager
        Dumper_Manager()

Start.start()