import random

def semp_core():
    text = """
 █████   ██████  ███████ ███    ██ ████████      ██████  ██████  ██████  ███████  dev mode 
██   ██ ██       ██      ████   ██    ██        ██      ██    ██ ██   ██ ██       v1.0.0.1
███████ ██   ███ █████   ██ ██  ██    ██        ██      ██    ██ ██████  █████    report bugs.
██   ██ ██    ██ ██      ██  ██ ██    ██        ██      ██    ██ ██   ██ ██      
██   ██  ██████  ███████ ██   ████    ██         ██████  ██████  ██   ██ ███████ 
    """

    text2 = """
Script Project: Generate User Agents
Made by VinNotSepuh
[!] Use this code if you are a developer or want to re-new the use agents

USER AGENT COUNT IS 100, CHANGE THE AMOUNT VIA CODE EDITOR IF NEEDED (LOCATION MARKED)
    """

    print(text)
    print(text2)

semp_core()

print("")
print("")
print("")
print("")

def generate_user_agent():
    browsers = ['Firefox/115.0', 'Chrome/115.0.0.0', 'Safari/537.36']
    platforms = ['Windows NT 10.0; Win64; x64', 'Macintosh; Intel Mac OS X 10_15_7', 'X11; Ubuntu; Linux x86_64']

    browser = random.choice(browsers)
    platform = random.choice(platforms)

    user_agent = f"Mozilla/5.0 ({platform}) AppleWebKit/537.36 (KHTML, like Gecko) {browser} Safari/537.36"

    return user_agent

def generate_user_agents(count):
    return [generate_user_agent() for _ in range(count)]

def save_user_agents_to_file(user_agents, filename):
    with open(filename, 'w') as file:
        for agent in user_agents:
            file.write(agent + '\n')
if __name__ == "__main__":
    num_agents = 100 # edit this number if you need more user agents
    user_agents = generate_user_agents(num_agents)
    save_user_agents_to_file(user_agents, 'user_agents.txt')
    print(f"{num_agents} Saved to user_agents.txt.")
    print("")
input("Press enter to continue..")