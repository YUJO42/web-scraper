# solution

import os
import requests


def restart():
    answer = str(input("Do you want to start over? y/n ")).lower()
    if answer == "y" or answer == "n":
        if answer == "n":
            print("k. bye!")
            return
        elif answer == "y":
            main()
    else:
        print("That's not a valid answer")
        restart()


def main():
    os.system('clear')
    print("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check. (separated by comma)")
    urls = str(input()).lower().split(",")
    for url in urls:
        url = url.strip()
        if "." not in url:
            print(url, "is not a valid URL.")
        else:
            if "http" not in url:
                url = f"http://{url}"
            try:
                request = requests.get(url)
                if request.status_code == 200:
                    print(url, "is up!")
                else:
                    print(url, "is down!")
            except:
                print(url, "is down!")
    restart()


main()

# @@@@@@@@@@@@@@@@@@ my code @@@@@@@@@@@@@@@
# import requests
# import os
# from urllib.request import urlopen
# from urllib.error import URLError, HTTPError

# print("Welcome to IsitDown.py")
# print("Please write a URL or URLs you want to check. (seprated by coma)")

# urls = input().split(",")

# for x in urls:
#     url_clean = x.strip()
#     if ("http://" not in url_clean):
#         url_clean = "http://" + url_clean
#     if (".com" not in url_clean):
#         print(url_clean, "is not valid url")
#         break
#     try:
#         res = urlopen(url_clean)
#         print(url_clean.lower(), "is up!")
#     except:
#         print(url_clean.lower(), "is down!")

# while (True):
#     print("Do you want to start over? y/n ", end="")
#     answer = input()
#     if (answer != "y" and answer != "n"):
#         print("That`s not a valid answer")
#         continue
#     if (answer == "n"):
#         print("OK, bye!!")
#         break
#     if (answer == "y"):
#         os.system('clear')  # if your OS is MAC, please change clear => CLS
#     print("Please write a URL or URLs you want to check. (seprated by coma)")
#     urls = input().split(",")
#     for x in urls:
#         url_clean = x.strip()
#         if ("http://" not in url_clean):
#             url_clean = "http://" + url_clean
#         if (".com" not in url_clean):
#             print(url_clean, "is not valid url")
#             break
#         try:
#             res = urlopen(url_clean)
#             print(url_clean.lower(), "is up!")
#         except:
#             print(url_clean.lower(), "is down!")
