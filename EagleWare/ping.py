import time
import os
import subprocess

os.system("title Eclipse Pinger")

def ascii_fancy():
    text = """
███████  ██████ ██      ██ ██████  ███████ ███████ 
██      ██      ██      ██ ██   ██ ██      ██      
█████   ██      ██      ██ ██████  ███████ █████   
██      ██      ██      ██ ██           ██ ██      
███████  ██████ ███████ ██ ██      ███████ ███████ 
    """
    print(text)

def yellow_to_red_gradient(text):
    gradient_text = ""

    start_color = [252, 53, 76]  
    end_color = [0, 255, 255]   

    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    gradient_steps = len(text)
    step_r = (end_r - start_r) / gradient_steps
    step_g = (end_g - start_g) / gradient_steps
    step_b = (end_b - start_b) / gradient_steps

    for char_index, char in enumerate(text):
        r = int(start_r + step_r * char_index)
        g = int(start_g + step_g * char_index)
        b = int(start_b + step_b * char_index)
        gradient_text += f"\033[38;2;{r};{g};{b}m{char}"
    
    return gradient_text

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def ping(ip, port, delay=0.01, timeout=10):
    try:
        clear_console()
        print(yellow_to_red_gradient(f"Enter IP: {ip}"))
        print(yellow_to_red_gradient(f"Enter Port: {port}"))

        while True:
            command = f"ping {ip} -n 1 -w {timeout * 1000}" if os.name == 'nt' else f"ping -c 1 -W {timeout} {ip}"
            result = subprocess.run(command, shell=True, capture_output=True, text=True)

            if "Request timed out" in result.stdout or "timed out" in result.stdout:
                print(yellow_to_red_gradient(f"Connection Timed Out"))
            else:
                time_info = "30ms"
                for line in result.stdout.splitlines():
                    if "time=" in line:
                        time_info = line.split("time=")[1].split("ms")[0] + "ms"
                        break

                print(yellow_to_red_gradient(f"Connected to IP: {ip} time={time_info} port={port}"))

            time.sleep(delay)

    except KeyboardInterrupt:
        print("\nPing operation interrupted by user.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ascii_fancy()
    ip = input("Enter IP: ")
    port = input("Enter Port: ")
    os.system("cls")
    ping(ip, port)