from pyfiglet import Figlet
from colorama import init, Fore, Style

from utils.utils import clearConsole

from menus.basic_menu import basicMenu
from menus.formulas_menu import formulasMenu

init(autoreset=True)

# --------- Banner del menú main ---------

def mainBanner():
    nameFiglet = Figlet(font='speed')
    print("="*45)
    print(nameFiglet.renderText('EAGLE'))
    print("="*45)
    print("7nd3k, 2025")
    print("="*45)

# --------- Selección del menú principal ---------

def mainSelection():
    while True:
        try:
            clearConsole()
            mainBanner()
            print("\n")
            print(Fore.YELLOW + "(1)" + Style.RESET_ALL + " Basic Magnitudes")
            print("")
            print(Fore.YELLOW + "(2)" + Style.RESET_ALL + " Physical Magnitudes (Coming Soon)")
            print("")
            print(Fore.YELLOW + "(3)" + Style.RESET_ALL + " Electromagnetic & Light (Coming Soon)")
            print("")
            print(Fore.YELLOW + "(4)" + Style.RESET_ALL + " Scientific & Special (Coming Soon)")
            print("")
            print(Fore.YELLOW + "(5)" + Style.RESET_ALL + " Formulas Calculator")
            print("")
            print(Fore.YELLOW + "(0)" + Style.RESET_ALL + " Exit")
            print("\n")
            
            choice = input(Fore.MAGENTA + "\n>> " + Style.RESET_ALL + "Select your desired option: ")
            if not choice.isdigit():
                print(Fore.RED + "\n[!] Enter a valid option" + Style.RESET_ALL)
                input("\n\nPress Enter to try again...")
                continue

            choice = int(choice)
            
            if choice == 1:
                basicMenu()

            elif choice == 2:
                pass

            elif choice == 3:
                pass

            elif choice == 4:
                pass
            
            elif choice == 5:
                formulasMenu()

            elif choice == 0:
                print(Fore.RED + "\n[!] Exiting..." + Style.RESET_ALL)
                break

        except KeyboardInterrupt:
            print(Fore.RED + "\n\n[!] Execution interrupted, exiting...\n" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    mainSelection()