from pyfiglet import Figlet
from colorama import init, Fore, Style
import time

from conversions.length import lengthConversion
from conversions.mass import massConversion
from conversions.time import timeConversion
from conversions.area import areaConversion

from utils.utils import clearConsole

init(autoreset=True)

# --------- Menú Magnitudes Básicas ---------

def basicMenu():
    while True:
        try:
            clearConsole()
            basicMagBanner = Figlet(font='standard')
            print("="*45)
            print(basicMagBanner.renderText('BASIC'))
            print("="*45)
            print("\n")
            print(Fore.YELLOW + "(1)" + Style.RESET_ALL + " Length")
            print("")
            print(Fore.YELLOW + "(2)" + Style.RESET_ALL + " Mass")
            print("")
            print(Fore.YELLOW + "(3)" + Style.RESET_ALL + " Time")
            print("")
            print(Fore.YELLOW + "(4)" + Style.RESET_ALL + " Area")
            print("")
            print(Fore.YELLOW + "(5)" + Style.RESET_ALL + " Volume (Coming Soon)")
            print("")
            print(Fore.YELLOW + "(0)" + Style.RESET_ALL + " Back to main\n")
            
            choice = input(Fore.MAGENTA + "\n>> " + Style.RESET_ALL + "Select your desired option: ")
            if not choice.isdigit():
                print(Fore.RED + "\n[!] Enter a valid option" + Style.RESET_ALL)
                continue

            choice = int(choice)

            if choice == 1:
                lengthConversion()
            elif choice == 2:
                massConversion()
            elif choice == 3:
                timeConversion()
            elif choice == 4:
                areaConversion()
            elif choice == 5:
                pass
            elif choice == 0:
                break
            
            else:
                print(Fore.RED + "\n[!] Option out of range" + Style.RESET_ALL)

        except KeyboardInterrupt:
            print(Fore.RED + "\n\n[!] Returning to main menu...\n" + Style.RESET_ALL)
            time.sleep(1)
            break