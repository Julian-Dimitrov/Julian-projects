from bs4 import BeautifulSoup
import requests
import re
from time import sleep
import datetime
import matplotlib.pyplot as plt


def price():
    html_text = requests.get("https://bg.fuelo.net/gasstation/id/55069?lang=bg").text
    soup = BeautifulSoup(html_text, 'html.parser')
    fuels = str(soup.find_all("span", itemprop="price"))

    diesel = float(re.findall(r"[-+]?(?:\d*\.\d+|\d+)", fuels)[3])

    return diesel


def visualize():
    with open("fuel_pr.txt", "r") as f:
        prices = eval(f.read())

    days = list(prices.keys())
    day = [datetime.datetime.strptime(i, '%m %d %H:%M:%S') for i in days]

    price = list(prices.values())

    fig, ax = plt.subplots()
    ax.plot(day, price, label='"daily" fuel prices', color="g")
    plt.title(price[-1])
    plt.legend()
    plt.savefig(r'C:\Users\julia\OneDrive\Desktop\CenaGorivo.png')


while True:
    pr = price()

    with open("fuel_pr.txt", "r+") as f:
        prices = eval(f.read())

        prices[datetime.datetime.now().strftime("%m %d %H:%M:%S")] = pr
        f.seek(0)
        f.truncate()
        f.write(str(prices))

    visualize()

    sleep(60*60*2)
