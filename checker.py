import requests
import os
import time
from colorama import Fore, init

init(autoreset=True)

API_URL = "https://discord.com/api/v10/invites/{}"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def check_vanity(vanity):
    url = API_URL.format(vanity)

    try:
        response = requests.get(url, headers=HEADERS, timeout=5)

        if response.status_code == 200:
            print(f"{Fore.RED}{vanity} → UNAVAILABLE")
        elif response.status_code == 404:
            print(f"{Fore.GREEN}{vanity} → AVAILABLE")
        elif response.status_code == 429:
            print(f"{Fore.YELLOW}RATE LIMITED... Waiting 5 seconds")
            time.sleep(5)
        else:
            print(f"{Fore.YELLOW}{vanity} → ERROR ({response.status_code})")

    except requests.exceptions.RequestException as e:
        print(f"{Fore.YELLOW}Connection error: {e}")

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        # 🔴 MORDE Başlık
        print(Fore.RED + "███╗   ███╗ ██████╗ ██████╗ ██████╗ ███████╗")
        print(Fore.RED + "████╗ ████║██╔═══██╗██╔══██╗██╔══██╗██╔════╝")
        print(Fore.RED + "██╔████╔██║██║   ██║██████╔╝██║  ██║█████╗  ")
        print(Fore.RED + "██║╚██╔╝██║██║   ██║██╔══██╗██║  ██║██╔══╝  ")
        print(Fore.RED + "██║ ╚═╝ ██║╚██████╔╝██║  ██║██████╔╝███████╗")
        print(Fore.RED + "╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝")
        print()

        print(Fore.CYAN + "=== Discord Vanity Checker ===\n")
        print("[1] Check vanity")
        print("[2] Exit")

        choice = input("\nChoice: ")

        if choice == "1":
            vanity = input("Enter vanity: ").strip()
            print("\nChecking...\n")
            check_vanity(vanity)
            input("\nPress Enter to continue...")
        elif choice == "2":
            break
        else:
            time.sleep(1)

if __name__ == "__main__":
    main()
