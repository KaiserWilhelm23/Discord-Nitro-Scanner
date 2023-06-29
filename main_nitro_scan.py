import secrets
import string
from colorama import Fore
import requests
import time
import webbrowser
import random

Fore.WHITE
check = None
 
url = "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt"

response = requests.get(url)
proxy_list = response.text.strip().split('\n')

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36'
]


def generate_random_code(length=16):
    """Generates a random alphanumeric code of the specified length."""
    characters = string.ascii_letters + string.digits
    code = ''.join(secrets.choice(characters) for _ in range(length))
    return code


def open_web_browser(var, code):
    if var == "n":
        return False
    if var == "y":
        webbrowser.open_new(f"https://discord.gift/{code}")


def rotate_user_agents():
    user_agent = random.choice(user_agents)
    headers = {'User-Agent': user_agent}
    return headers


def rotate_proxies():
    proxy = random.choice(proxy_list)
    proxies = {'http': proxy, 'https': proxy}
    return proxies


def is_valid_nitro_code(code, browser):
    # Loading the API
    web_header = rotate_user_agents()
    proxies = rotate_proxies()
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}"

    try:
        response = requests.get(url, headers=web_header, proxies=proxies)
    except Exception as e: 
        print(f"[{Fore.YELLOW}Proxy Error{Fore.WHITE}]  Error on {proxies}  (Ignore)")


    try:
        answer = response.status_code
    except Exception as e:
        print(f"[{Fore.YELLOW}Variable Error{Fore.WHITE}]  (Ignore)")
        answer = "No Code Available "

    # Logic to check status codes
    if answer == 429:
        print(f"[{Fore.RED}Rate Limited{Fore.WHITE}]  Code Unable to be checked. Attempting a User-Agent Header Rotation")
        rotate_user_agents()
    elif answer != 200:
        print(f"[{Fore.RED}Invalid{Fore.WHITE}]   https://discord.gift/{code}")
    elif answer == 200:
        print(f"[{Fore.GREEN}Valid{Fore.WHITE}]   https://discord.gift/{code}")
        open_web_browser(code, browser)
    

print("Welcome to the Discord Nitro Code Scanner V.1")


def main():
    # User Input (integer)
    user = int(input("How many codes would you like to generate (0=inf)? "))
    check = input("Would you like the program to check if the code is valid y/n (Scans are slow due to the use of Proxies)? ")
    browser = input("Would you like the program to open the web browser when a valid link is found y/n? ")

    # Checks Discord Nitro links forever until a Keyboard Interrupt
    if user == 0:
        # Code to inf check codes and or return them if check = n
        while True:
            time.sleep(0.7)
            try:
                random_code = generate_random_code()

                if check == "y":
                    is_valid_nitro_code(random_code, browser)
                else:
                    print(f"[{Fore.YELLOW}Not Checked{Fore.WHITE}]   https://discord.gift/{random_code}")

            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                main()
    # If user inputs anything but 0, it will check the specified number of links.
    else:
        for _ in range(user):
            random_code = generate_random_code()
            if check == "y":
                is_valid_nitro_code(random_code, browser)
            else:
                print(f"[{Fore.YELLOW}Not Checked{Fore.WHITE}]   https://discord.gift/{random_code}")

        main()


main()
