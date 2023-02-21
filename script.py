import os
import re
import csv
from statistics import median
from datetime import datetime
import chromedriver_autoinstaller
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


now = datetime.now().strftime("%H-%M_on_%d-%m-%Y")

# convert csv to list of items to search for
with open('search_list.csv', newline='') as infile:
    search_list = [''.join(item) for item in list(csv.reader(infile))[1:]]

# country names with country website endings
country_dict = {"canada": "ca", "usa": "com", "italy": "it", "australia": "com.au",
                "austria": "au", "belgium": "be", "france": "fr", "germany": "de", "malaysia": "com.my",
                "netherlands": "nl", "philippines": "ph", "singapore": "com.sg", "spain": "com.es",
                "switzerland": "ch", "uk": "co.uk"}

# determine country to search in -- NOTE: the searches will be done using the languages inputted in the search_list.csv
country_key = input("What country do you want to search in? ").lower().strip()

# if country selected doesn't match the options, show the options and try again
while not country_dict.get(country_key):
    print(country_dict.keys())
    country_key = input("Above are the available countries. Please input the country to search in: ").lower().strip()

# create plain url with the country's code
plain_url = f"https://www.ebay.{country_dict[country_key]}/sch/i.html?LH_Complete=1&LH_Sold=1&_from=R40&_nkw=REPLACE&_ipg=120"

# create lists of item names and the URLs to search through
items = []
urls = []
for item in search_list:
    items.append(item)
    urls.append(plain_url.replace('REPLACE', item.replace(" ", "+")))

# check if correct chromedriver version is installed, otherwise install the correct version to this script's path
chromedriver_autoinstaller.install()

# connect to chromedriver and launch
srv = Service("\chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_argument('--headless')
op.add_argument('--disable-gpu')

# collect median prices and count of sales for each item
medianPrices = []
sales_count = []

with webdriver.Chrome(service=srv, options=op) as drv:
    for url in urls:
        # if url doesn't work, return invalid url message and go to next
        try:
            drv.get(url)
        except selenium.common.exceptions.InvalidArgumentException:
            print(f'This url is invalid: {url}')
            continue

        try:
            prices = drv.find_elements(By.CLASS_NAME, "s-item__price")
            prices.pop(0)
            prices_list = []        # collect list of all cleaned prices
            for price in prices:
                price = price.get_attribute("innerHTML").replace(",", ".")      # to account for european decimals
                if price.count('.') > 1 or "STRIKETHROUGH" in price:        # to remove inaccurate prices from list
                    continue
                price = float(re.sub(r'[^\d.]+', '', price))            # remove everything not a number or decimal
                prices_list.append(price)
            sales = int(len(prices_list))                           # num of sales
            middle = round(median(prices_list), 2)                  # median sale amount
        except:
            middle = "No prices found."
            sales = "No sales found."

        medianPrices.append(middle)
        sales_count.append(sales)

        print(f'Completed item {urls.index(url) + 1}')

item_data = zip(items, medianPrices, sales_count)

# create output csv with the data
with open(f'outputs\output_{now}.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Items", "Prices", "Sales Incl.", "",
                     f"Data is from {country_key.upper()} in their local currency and doesn't include shipping fees."])
    for row in item_data:
        writer.writerow(row)

os.startfile(f'output_{now}.csv')
