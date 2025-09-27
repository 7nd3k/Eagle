from pyfiglet import Figlet
from colorama import init, Fore, Style
import time

from utils.utils import clearConsole

init(autoreset=True)

# --------- Conversiones Masa ---------

def massConversion():
    while True:
        try:
            clearConsole()
            massBanner = Figlet(font='standard')
            print("="*45)
            print(massBanner.renderText('MASS'))
            print("="*45)
            print("\n")
            print(Fore.YELLOW + "(1)" + Style.RESET_ALL + " Kilograms → Grams")
            print(Fore.YELLOW + "(2)" + Style.RESET_ALL + " Grams → Kilograms")
            print("")
            print(Fore.YELLOW + "(3)" + Style.RESET_ALL + " Kilograms → Pounds")
            print(Fore.YELLOW + "(4)" + Style.RESET_ALL + " Pounds → Kilograms")
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

            if choice == 1: # kg → g
                result = value*1000
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} kg = {result} g")

            elif choice == 2: # g → kg
                result = value/1000
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} g = {result} kg")

            elif choice == 3: # kg → lb
                result = value*2.20462
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} kg = {result} lb")

            elif choice == 4: # lb → kg
                result = value/2.20462
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} lb = {result} kg")

            else:
                print(Fore.RED + "\n[!] Option out of range" + Style.RESET_ALL)

            input("\n\nPress Enter to continue...")

        except KeyboardInterrupt:
            print(Fore.RED + "\n\n[!] Returning to basic menu..." + Style.RESET_ALL)
            time.sleep(1)
            break