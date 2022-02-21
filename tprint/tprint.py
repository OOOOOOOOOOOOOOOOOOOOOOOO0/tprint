import sys, time, os
from colorama import Fore


class tprint:
    
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    CYAN = Fore.CYAN
    BLUE = Fore.BLUE
    WHITE = Fore.WHITE
    MAGENTA = Fore.MAGENTA
    BLACK = Fore.BLACK

    def __init__(self, colour, text, vel):
        for character in text + "\n":
            sys.stdout.write(f'{colour}{character}')
            sys.stdout.flush()
            time.sleep(1. / vel)
    
