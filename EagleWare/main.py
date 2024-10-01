import shutil
from colorama import init, Style
import sys
import ctypes
import win32console
import os
import datetime
import getpass
import pyautogui  
import tkinter as tk
from tkinter import messagebox

def show_warning():
    root = tk.Tk()
    root.withdraw()  
    messagebox.showwarning("dsc.gg/wearentdevs", "node commands.js to see commands :)")
    
show_warning()

os.system('cls' if os.name == 'nt' else 'clear')

win32console.SetConsoleTitle("EagleWare :3")  # cute

init(autoreset=True)

# Is this why you're worried?
# We did this because autoscaling wasn't working, it's not a virus <3
def simulate_key_presses():
    pyautogui.press('f11')          
    pyautogui.hotkey('ctrl', 'down') 
    pyautogui.press('f11')         

simulate_key_presses()

def apply_gradient(text, start_color, end_color):
    gradient_text = ""
    color_range = len(text)
    for i, char in enumerate(text):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * (i / color_range))
        g = int(start_color[1] + (end_color[1] - start_color[1]) * (i / color_range))
        b = int(start_color[2] + (end_color[2] - start_color[2]) * (i / color_range))
        gradient_text += f'\033[38;2;{r};{g};{b}m{char}'
    return gradient_text

def blue_green_gradient(text):
    start_color = (0, 0, 255)  
    end_color = (0, 255, 0)   
    return apply_gradient(text, start_color, end_color)

def get_welcome_message():
    now = datetime.datetime.now()
    hour = now.hour
    username = getpass.getuser()
    
    if 18 <= hour < 24 or 0 <= hour < 6:
        entrance_msg = "Good night"
    elif 6 <= hour < 12:
        entrance_msg = "Good morning"
    else:
        entrance_msg = "Good afternoon"
    
    return f"{entrance_msg}, logged in as {username}"

eagle_text = r"""
‎ 
    ______            __   _       __              
   / ____/___ _____ _/ /__| |     / /___ _________ 
  / __/ / __ `/ __ `/ / _ \ | /| / / __ `/ ___/ _ \
 / /___/ /_/ / /_/ / /  __/ |/ |/ / /_/ / /  /  __/
/_____/\__,_/\__, /_/\___/|__/|__/\__,_/_/   \___/ 
            /____/               VinNotSepuh Cyber Army 
"""

footer_text = r"""
╔════════════════════════════════════════════════════════════════╗
     Made by VinNotSepuh - dsc.gg/ddos-botnet - Version: V4.0.5    
╚════════════════════════════════════════════════════════════════╝
"""

ascii_art = r"""
‎ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣤⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⡿⠿⠿⠛⠛⠛⠛⠻⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣀⣤⡾⢿⣿⣿⠿⠟⠉⠉⠀⠀⣠⣴⣶⣖⠒⡤⠀⠠⢾⣿⣭⣭⣾⣛⣻⣿⣿⣿⣿⣯⣍⣛⡿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡴⠛⠉⢁⣀⠀⢤⡀⠹⣇⠀⠢⠂⠀⠤⣾⠹⣿⣷⣟⡴⠃⠀⣀⣼⣭⣟⠛⠯⠭⠼⠿⢿⣿⣿⣿⣿⣿⣯⣽⣻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⡟⠁⢀⠎⠁⠀⠀⠈⠉⠆⠻⣿⣶⣀⣀⠀⠈⠓⠶⠶⠋⢁⣰⣾⣿⣭⡷⢖⣚⣿⠂⠌⣛⣻⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠁⠀⠀⠀⠀⠀⠀⠐⠲⠶⢄⠈⢿⣿⣿⣿⣿⣿⣷⡾⠿⠿⢿⣿⣞⠳⠾⣷⣻⢿⣯⠽⠛⠛⠉⣹⣿⣿⣿⣿⣿⣿⣿⣿⣝⢦⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠀⠀⢀⡠⠖⠛⠛⠲⣄⡀⠑⠈⢿⣿⣿⣿⣿⣿⣿⣋⣩⠭⣒⣛⠭⡗⣶⠽⠛⠋⠉⠀⣀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀
⠸⡀⡠⠊⠉⠐⠲⢤⡂⢀⠀⠙⢦⡀⣀⠙⣿⣿⣿⣿⣿⣿⣷⣶⠁⣲⣮⣝⣺⠷⠆⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀
⠀⠑⠁⠀⠀⠀⠀⠀⠈⠓⠷⣤⣠⣙⠻⠀⢸⣿⣿⣿⣿⣿⣿⣦⣶⡞⠉⠀⠀⠀⠀⠀⠸⠿⠛⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢤⠤⠝⠲⢿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀⠴⠾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⠁⠄⠀⠘⢿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⡀⠀⠀⠀⣽⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⠀⠀⠀⠀⢹⣿⣿⣿⣷⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀
"""

def print_centered_text(text):
    terminal_size = shutil.get_terminal_size()
    term_width = terminal_size.columns

    lines = text.strip().split('\n')

    centered_lines = [line.center(term_width) for line in lines]

    for line in centered_lines:
        print(blue_green_gradient(line))

if __name__ == "__main__":
    print_centered_text(eagle_text)
    print()  
    print_centered_text(footer_text)
    print()
    print_centered_text(ascii_art)
    print()

    welcome_message = get_welcome_message()
    print_centered_text(welcome_message)
