from pyfiglet import Figlet
from colorama import init, Fore, Style
import time

from utils.utils import clearConsole

init(autoreset=True)

# --------- Conversiones Longitud ---------

def lengthConversion():
    while True:
        try:
            clearConsole()
            lengthBanner = Figlet(font='standard')
            print("="*45)
            print(lengthBanner.renderText('LENGTH'))
            print("="*45)
            print("\n")
            print(Fore.YELLOW + "(1)" + Style.RESET_ALL + " Kilometers → Meters")
            print(Fore.YELLOW + "(2)" + Style.RESET_ALL + " Meters → Kilometers")
            print("")
            print(Fore.YELLOW + "(3)" + Style.RESET_ALL + " Kilometers → Miles")
            print(Fore.YELLOW + "(4)" + Style.RESET_ALL + " Miles → Kilometers")
            print("")
            print(Fore.YELLOW + "(5)" + Style.RESET_ALL + " Meters → Feet")
            print(Fore.YELLOW + "(6)" + Style.RESET_ALL + " Feet → Meters")
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

            if choice == 1: # km → m
                result = value*1000
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} km = {result} m")

            elif choice == 2: # m → km
                result = value/1000
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} = {result} km")

            elif choice == 3: # km → mi
                result = value*0.621371
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} km = {result} mi")
            
            elif choice == 4: # mi → km
                result = value*1.60934
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} mi = {result} km")

            elif choice == 5: # m → ft
                result = value*3.28084
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} m = {result} ft")

            elif choice == 6: # ft → m
                result = value*0.3048
                print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"{value} ft = {result} m")
                
            else:
                print(Fore.RED + "\n[!] Option out of range" + Style.RESET_ALL)

            input("\n\nPress Enter to continue...")


        except KeyboardInterrupt:
            print(Fore.RED + "\n\n[!] Returning to basic menu..." + Style.RESET_ALL)
            time.sleep(1)
            break