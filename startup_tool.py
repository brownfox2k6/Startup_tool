from getpass import getuser
from os.path import join
from colorama import init
from msvcrt import getch

init(wrap=True)

print("\033[96mEnter full path of source file:\033[0m")
file_path = input()
print("\033[96mEnter name of bat file:\033[0m")
bat_name = input()

bat_path = f"C:/Users/{getuser()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
with open(join(bat_path, bat_name), "w+") as bat_file:
    bat_file.write(f'start "" "{file_path}"')

print("\033[96mSuccess. Press any key to exit.\033[0m")
getch()
