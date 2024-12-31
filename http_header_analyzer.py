import requests

def analyze_http_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        return headers
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    target_url = input("Enter the target URL: ")
    headers = analyze_http_headers(target_url)

    if headers:
        print(f"Headers for {target_url}:")
        for header, value in headers.items():
            print(f"{header}: {value}")
    else:
        print("Failed to retrieve headers.")
