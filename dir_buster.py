import requests
from requests.exceptions import RequestException

def brute_force_directories(url, wordlist_file):
    with open(wordlist_file, 'r') as f:
        for line in f.readlines():
            directory = line.strip()
            full_url = f"{url}/{directory}"
            try:
                response = requests.get(full_url)
                if response.status_code == 200:
                    print(f"Found: {full_url}")
            except RequestException as e:
                print(f"Error: {e}")
                continue

if __name__ == "__main__":
    url = input("Enter the target URL: ")
    wordlist_file = input("Enter path to the wordlist: ")
    brute_force_directories(url, wordlist_file)
