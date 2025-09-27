from pyfiglet import Figlet
from colorama import init, Fore, Style
import time

from utils.utils import clearConsole

init(autoreset=True)

# --------- Conversiones Tiempo ---------

def timeConversion():
    while True:
        try:
            clearConsole()
            timeBanner = Figlet(font="standard")
            print("="*45)
            print(timeBanner.renderText('TIME'))
            print("="*45)
            print("\n")
            print(Fore.YELLOW + "(1)" + Style.RESET_ALL + " Seconds → Minutes")
            print(Fore.YELLOW + "(2)" + Style.RESET_ALL + " Minutes → Seconds")
            print("")
            print(Fore.YELLOW + "(3)" + Style.RESET_ALL + " Minutes → Hours")
            print(Fore.YELLOW + "(4)" + Style.RESET_ALL + " Hours → Minutes")
            print("")
            print(Fore.YELLOW + "(5)" + Style.RESET_ALL + " Hours → Days")
            print(Fore.YELLOW + "(6)" + Style.RESET_ALL + " Days → Hours")
            print("")
            print(Fore.YELLOW + "(0)" + Style.RESET_ALL + " Back to Basic Menu")

            choice = input(Fore.MAGENTA + "\n>> " + Style.RESET_ALL + "Select your desired option: ")
            if not choice.isdigit():
                print(Fore.RED + "\n[!] Enter a valid option" + Style.RESET_ALL)
                input("\n\nPress Enter to try again...")
                continue

            choice = int(choice)

            if choice == 0:
                break

            value = input(Fore.MAGENTA + "\n>> " + Style.RESET_ALL + "Enter a value to convert: ")
            try:
                value = float(value)
            except ValueError:
                print(Fore.RED + "\n[!] Invalid value" + Style.RESET_ALL)
                input("\n\nPress Enter to try again...")
                continue

            if choice == 1: # seg → min
                result = value/60
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} sec = {result} min")

            elif choice == 2: # min → seg
                result = value*60
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} min = {result} sec")

            elif choice == 3: # min → hrs
                result = value/60
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} min = {result} hrs")

            elif choice == 4: # hrs → min
                result = value*60
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} hrs = {result} min")

            elif choice == 5: # hrs → day/s
                result = value/24
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} hrs = {result} day/s")

            elif choice == 6: # day/s → hrs
                result = value*24
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} day/s = {result} hrs")

            else:
                print(Fore.RED + "\n[!] Option out of range" + Style.RESET_ALL)

            input("\n\nPress Enter to continue...")

        except KeyboardInterrupt:
            print(Fore.RED + "\n\n[!] Returning to basic menu..." + Style.RESET_ALL)
            time.sleep(1)
            break