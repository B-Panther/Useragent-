import requests

def run_script(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            exec(response.text)
        else:
            print(f"Failed to fetch script from {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Select a script to run:")
    print("1. ANDROID FBAN")
    print("2. IPHONE FBIOS")
    print("3. ANDROID DALVIK")
    print("4. ANDROID DAVIK ORCA")
    print("5. ANDROID ORCA")

    try:
        choice = int(input("Enter your choice (1-5): "))
        if 1 <= choice <= 5:
            script_urls = [
                "https://raw.githubusercontent.com/B-Panther/Useragent-/main/FBANUA.py",
                "https://raw.githubusercontent.com/your_username/repository/IPUA.py",
                "https://raw.githubusercontent.com/your_username/repository/dalvik.py",
                "https://raw.githubusercontent.com/your_username/repository/dalorc.py",
                "https://raw.githubusercontent.com/your_username/repository/orca_andua.py",
            ]
            run_script(script_urls[choice - 1])
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
