import requests
import sys
import re
import json


def main():
    # Take url from cli
    url = get_url()
    # Get res json
    res = get_res(url)
    print(json.dumps(res[0],indent=2))
    
    
    
    
# Regex url github
def check_url_github(url):
    pattern = r"^https?://api\.github\.com/users/.+/events$"
    match = re.search(pattern,url)
    if match:
        return url
    else:
        return False

# Get url from cli
def get_url():
    msg_error = "https://api.github.com/users/<username>/events"
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        sys.exit(f"Example: python main.py {msg_error}")
    
    url = sys.argv[1].strip()
    if check_url_github(url):
        return url
    else:
        sys.exit(f"Invalid url example: {msg_error}")

# Get response and transfrom json
def get_res(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    
    sys.exit(f"ERROR {res.status_code}")


def clean_data(activy_user:dict)-> str:
    ...
    
def check_event(type_event:str)-> str:
    list_events = []
if __name__ == "__main__":
    main()


