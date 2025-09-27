from pyfiglet import Figlet
from colorama import init, Fore, Style
import time

from utils.utils import clearConsole
from formulas.space import spaceFormulas

init(autoreset=True)

# --------- Menú Calculadora de Fórmulas ---------

def formulasMenu():
    while True:
        try:
            clearConsole()
            formulasCalcBanner = Figlet(font='standard')
            print("="*45)
            print(formulasCalcBanner.renderText('FORMULAS'))
            print("="*45)
            print("\n")
            print(Fore.YELLOW + "(1)" + Style.RESET_ALL + " Space")
            print("")
            print(Fore.YELLOW + "(0)" + Style.RESET_ALL + " Back to main\n")
            
            choice = input(Fore.MAGENTA + "\n>> " + Style.RESET_ALL + "Select your desired option: ")
            if not choice.isdigit():
                print(Fore.RED + "\n[!] Enter a valid option" + Style.RESET_ALL)
                continue

            choice = int(choice)

            if choice == 1:
                spaceFormulas()

            elif choice == 0:
                break
            
            else:
                print(Fore.RED + "\n[!] Option out of range" + Style.RESET_ALL)

        except KeyboardInterrupt:
            print(Fore.RED + "\n\n[!] Returning to main menu...\n" + Style.RESET_ALL)
            time.sleep(1)
            break