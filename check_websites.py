import requests

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"[✔] {url} is UP")
        else:
            print(f"[!] {url} returned status code {response.status_code}")
    except requests.RequestException:
        print(f"[✘] {url} is DOWN or unreachable")

def main():
    try:
        with open("websites.txt", "r") as file:
            urls = [line.strip() for line in file if line.strip()]
            print("Checking websites...\n")
            for url in urls:
                check_website(url)
    except FileNotFoundError:
        print("Error: websites.txt file not found!")

if __name__ == "__main__":
    main()
