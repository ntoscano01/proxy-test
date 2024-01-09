# -*- coding: utf-8 -*-

import requests

with open ("valid-proxies.txt", "r") as f:
    proxies = f.read().split("\n")

sites_to_check = ["https://books.toscrape.com/",
                 "https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html",
                 "https://books.toscrape.com/catalogue/category/books/history_32/index.html"]

counter = 0

for site in sites_to_check:
    try:
        print(f"Using the proxy: {proxies[counter]}")
        res = requests.get(site, proxies={"http": proxy[counter], "https": proxy[counter]})

        print(res.status_code)
        print(res.status_code)

    except:
        print("failed")
        
    finally:
        counter += 1
        counter % len(proxies)

