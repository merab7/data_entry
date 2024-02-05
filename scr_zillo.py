import requests
from bs4 import BeautifulSoup

zillo_test_url =" https://appbrewery.github.io/Zillow-Clone/"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(zillo_test_url, headers=header)
DATA_FROM_ZILLO = response.text
soup = BeautifulSoup(DATA_FROM_ZILLO, "html.parser")
links = soup.select(".StyledPropertyCardDataWrapper a")
addresses = soup.select(".StyledPropertyCardDataWrapper address")
prices = soup.select(".PropertyCardWrapper span")



class Data_zillo:
    def __init__(self) -> None:
        self.data_dict = {}


    def get_data(self):
        self.lis_addresses = [x.get_text().replace(" | ", " ").strip() for x in addresses]
        self.lis_links = [x["href"] for x in links]
        self.lis_prices = [x.get_text().replace("/mo", "") for x in prices]
        self.data_dict = {idx: [address, price, link] for idx, (address, price, link) in enumerate(zip(self.lis_addresses, self.lis_prices, self.lis_links))}
        