
import requests
import os
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

print("Welcome to IsitDown.py")
print("Please write a URL or URLs you want to check. (seprated by coma)")

urls = input().split(",")

for x in urls:
    url_clean = x.strip()
    if ("http://" not in url_clean):
        url_clean = "http://" + url_clean
    if (".com" not in url_clean):
        print(url_clean, "is not valid url")
        break
    try:
        res = urlopen(url_clean)
        print(url_clean.lower(), "is up!")
    except:
        print(url_clean.lower(), "is down!")

while (True):
    print("Do you want to start over? y/n ", end="")
    answer = input()
    if (answer != "y" and answer != "n"):
        print("That`s not a valid answer")
        continue
    if (answer == "n"):
        print("OK, bye!!")
        break
    if (answer == "y"):
        os.system('clear')  # if your OS is MAC, please change clear => CLS
    print("Please write a URL or URLs you want to check. (seprated by coma)")
    urls = input().split(",")
    for x in urls:
        url_clean = x.strip()
        if ("http://" not in url_clean):
            url_clean = "http://" + url_clean
        if (".com" not in url_clean):
            print(url_clean, "is not valid url")
            break
        try:
            res = urlopen(url_clean)
            print(url_clean.lower(), "is up!")
        except:
            print(url_clean.lower(), "is down!")
