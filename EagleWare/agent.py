def semp_core():
    text = """
 █████   ██████  ███████ ███    ██ ████████      ██████  ██████  ██████  ███████  dev mode 
██   ██ ██       ██      ████   ██    ██        ██      ██    ██ ██   ██ ██       v1.0.0.1
███████ ██   ███ █████   ██ ██  ██    ██        ██      ██    ██ ██████  █████    report bugs.
██   ██ ██    ██ ██      ██  ██ ██    ██        ██      ██    ██ ██   ██ ██      
██   ██  ██████  ███████ ██   ████    ██         ██████  ██████  ██   ██ ███████ 
    """

    text2 = """
Script Project: Automatic sorting of User Agents
Made by VinNotSepuh
[!] Use this code if you are a developer or want to re-new the use agents
    """

    print(text)
    print(text2)

semp_core()

def read_user_agents(file_path):
    user_agents = []
    
    try:
        with open(file_path, 'r') as file:
            user_agents = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    
    return user_agents

def save_user_agents(user_agents, file_path):
    with open(file_path, 'w') as file:
        file.write("const userAgents = [\n")
        for agent in user_agents:
            file.write(f'    "{agent}",\n')
        file.write("];\n")

def main():
    input_file_path = input("Enter the path of the text file containing user agents (e.g., 'user_agents.txt'): ")
    user_agents = read_user_agents(input_file_path)
    
    if user_agents:
        output_file_path = input("Enter the path where you want to save the JavaScript file (e.g., 'user_agents.js'): ")
        save_user_agents(user_agents, output_file_path)
        print(f"User agents have been successfully saved to '{output_file_path}'.")
    else:
        print("No user agents were found or the file could not be read.")

if __name__ == "__main__":
    main()
