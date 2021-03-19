import requests

def main():
    print("hello world")
    r = requests.get("http://icanhazip.com/")
    print(r.status_code)
    print(r.text)