from pyfiglet import Figlet
from colorama import init, Fore, Style
import time

from utils.utils import clearConsole

init(autoreset=True)

# --------- Fórmulas Espaciales ---------

# Constante Gravitacional
G = 6.67430e-11

# Función para escribir en notación científica
def parseScientific(user_input):
    try:
        user_input = user_input.replace(',', '.')
        if '*10e' in user_input:
            base, exp = user_input.split('*10e')
            return float(base) * 10**float(exp)
        else:
            return float(user_input)
    except Exception:
        raise ValueError(Fore.RED + "\n[!] Invalid scientific format. Use like 1,1*10e24 (e stands for raised to)" + Style.RESET_ALL)
    
# Función para obtener outputs en notación científica
def formatScientific(value):
    s = "{:.3e}".format(value)
    base, exp = s.split("e")
    return f"{base}*10e{int(exp)}"

# Función cálculo
def spaceFormulas():
    while True:
        try:
            clearConsole()
            spaceBanner = Figlet(font='standard')
            print("="*45)
            print(spaceBanner.renderText('SPACE'))
            print("="*45)
            print("\n")
            print(Fore.YELLOW + "(1)" + Style.RESET_ALL + " Gravity (g = GM / r²)")
            print("")
            print(Fore.YELLOW + "(2)" + Style.RESET_ALL + " Escape Velocity (ve = √(2GM / r))")
            print("")
            print(Fore.YELLOW + "(0)" + Style.RESET_ALL + " Back to Formulas Menu")

            choice = input(Fore.MAGENTA + "\n>> " + Style.RESET_ALL + "Select your desired option: ")
            if not choice.isdigit():
                print(Fore.RED + "\n[!] Enter a valid option" + Style.RESET_ALL)
                input("\n\nPress Enter to try again...")
                continue

            choice = int(choice)

            if choice == 0:
                break

            elif choice == 1:
                while True:
                    clearConsole()
                    print("="*45)
                    gravityBanner = Figlet(font='standard')
                    print(gravityBanner.renderText('GRAVITY'))
                    print("="*45)
                    print("\n")
                    print(Fore.YELLOW + "(1)" + Style.RESET_ALL + " Calculate Gravity [g] (need M, r)")
                    print("")
                    print(Fore.YELLOW + "(2)" + Style.RESET_ALL + " Calculate Mass [M] (need g, r)")
                    print("")
                    print(Fore.YELLOW + "(3)" + Style.RESET_ALL + " Calculate Radius [r] (need g, M)")
                    print("")
                    print(Fore.YELLOW + "(0)" + Style.RESET_ALL + " Back to Space Menu\n")

                    subchoice = input(Fore.MAGENTA + "\n>> " + Style.RESET_ALL + "Select your desired option: ")

                    if not subchoice.isdigit():
                        print(Fore.RED + "\n[!] Enter a valid option" + Style.RESET_ALL)
                        input("\n\nPress Enter to try again...")
                        continue

                    subchoice = int(subchoice)

                    if subchoice == 0:
                        break

                    try:

                        if subchoice == 1: # Calcular Gravedad
                            M = parseScientific(input(Fore.MAGENTA + "\n>>" + Style.RESET_ALL + " Enter Mass (kg) [e.g., 5,97*10e24]: "))
                            r = parseScientific(input(Fore.MAGENTA + "\n>>" + Style.RESET_ALL + " Enter Radius (m) [e.g., 6,371*10e6]: "))
                            g = G * M / (r**2)
                            print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"Gravity [g] = {formatScientific(g)} m/s²")

                        elif subchoice == 2: # Calcular Masa
                            g = parseScientific(input(Fore.MAGENTA + "\n>>" + Style.RESET_ALL + " Enter Gravity (m/s²): "))
                            r = parseScientific(input(Fore.MAGENTA + "\n>>" + Style.RESET_ALL + " Enter Radius (m) [e.g., 6,371*10e6]: "))
                            M = g * (r**2) / G
                            print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"Mass [M] = {formatScientific(M)} kg")
                        
                        elif subchoice == 3: # Calcular Radio
                            g = parseScientific(input(Fore.MAGENTA + "\n>>" + Style.RESET_ALL + " Enter Gravity (m/s²): "))
                            M = parseScientific(input(Fore.MAGENTA + "\n>>" + Style.RESET_ALL + " Enter Mass (kg) [e.g., 5,97*10e24]: "))
                            r = (G * M / g)**0.5
                            print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"Radius [r] = {formatScientific(r)} m")

                        else:
                            print(Fore.RED + "\n[!] Option out of range" + Style.RESET_ALL)
                        
                        input("\n\nPress Enter to continue...")

                    except KeyboardInterrupt:
                        print(Fore.RED + "\n\n[!] Returning to basic menu..." + Style.RESET_ALL)
                        time.sleep(1)
                        break

            elif choice == 2:
                try:
                    M = parseScientific(input(Fore.MAGENTA + "\n>>" + Style.RESET_ALL + " Enter Mass (kg) [e.g., 5,97*10e24]: "))
                    r = parseScientific(input(Fore.MAGENTA + "\n>>" + Style.RESET_ALL + " Enter Radius (m) [e.g., 6,371*10e6]: "))
                    ve = (2 * G * M / r)**0.5
                    print(Fore.GREEN + "\n[-]", Style.RESET_ALL, f"Escape Velocity [ve] = {formatScientific(ve)} m/s")
                except ValueError:
                    print(Fore.RED + "\n[!] Invalid scientific format. Use like 1,1*10e24 (e stands for raised to)" + Style.RESET_ALL)

            elif choice == 0:
                break
            
            else:
                print(Fore.RED + "\n[!] Option out of range" + Style.RESET_ALL)

            input("\nPress Enter to continue...")

        
        except KeyboardInterrupt:
            print(Fore.RED + "\n\n[!] Returning to formulas menu..." + Style.RESET_ALL)
            time.sleep(1)
            break