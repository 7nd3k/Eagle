from pyfiglet import Figlet
from colorama import init, Fore, Style
import time

from utils.utils import clearConsole

init(autoreset=True)

# --------- Conversiones Longitud ---------

def areaConversion():
    while True:
        try:
            clearConsole()
            areaBanner = Figlet(font="standard")
            print("="*45)
            print(areaBanner.renderText('AREA'))
            print("="*45)
            print("\n")
            print(Fore.YELLOW + "(1)" + Style.RESET_ALL + " Square meters → Square centimeters")
            print(Fore.YELLOW + "(2)" + Style.RESET_ALL + " Square centimeters → Square meters")
            print("")
            print(Fore.YELLOW + "(3)" + Style.RESET_ALL + " Square meters → Square kilometers")
            print(Fore.YELLOW + "(4)" + Style.RESET_ALL + " Square kilometers → Square meters")
            print("")
            print(Fore.YELLOW + "(5)" + Style.RESET_ALL + " Square meters → Hectares")
            print(Fore.YELLOW + "(6)" + Style.RESET_ALL + " Hectares → Square meters")
            print("")
            print(Fore.YELLOW + "(7)" + Style.RESET_ALL + " Square kilometers → Hectares")
            print(Fore.YELLOW + "(8)" + Style.RESET_ALL + " Hectares → Square kilometers")
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

            if choice == 1: # m² → cm²
                result = value*10000
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} m² = {result} cm²")

            elif choice == 2: # cm² → m²
                result = value/10000
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} cm² = {result} m²")

            elif choice == 3: # m² → km²
                result = value/1_000_000
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} m² = {result} km²")

            elif choice == 4: # km² → m²
                result = value*1_000_000
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} km² = {result} m²")

            elif choice == 5: # m² → ha
                result = value/10_000
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} m² = {result} ha")

            elif choice == 6: # ha → m²
                result = value*10_000
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} ha = {result} m²")

            elif choice == 7: # km² → ha
                result = value*100
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} km² = {result} ha")

            elif choice == 8: # ha → km²
                result = value/100
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} ha = {result} km²")

            else:
                print(Fore.RED + "\n[!] Option out of range" + Style.RESET_ALL)

            input("\n\nPress Enter to continue...")

        except KeyboardInterrupt:
            print(Fore.RED + "\n\n[!] Returning to basic menu..." + Style.RESET_ALL)
            time.sleep(1)
            break