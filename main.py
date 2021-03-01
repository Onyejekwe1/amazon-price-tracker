import requests
from bs4 import BeautifulSoup as bsoup
import lxml
import smtplib

BUY_PRICE = 2500

product_url = "https://www.amazon.com/OMEN-Generation-i9-10900K-Processor-GT13-0093/dp/B08HR91FHT?ref_=ast_sto_dp&th=1"

response = requests.get(f"{product_url}", headers={"Accept-Language": "en-US,en;q=0.9",
                                                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}).text

soup = bsoup(response, "lxml")

price = soup.find(name="span", id="priceblock_ourprice",
                  class_="a-size-medium a-color-price priceBlockBuyingPriceString")

actual_price = float(price.get_text().split("$", 1)[1].replace(',', ''))

if actual_price < BUY_PRICE:
    message = f"OMEN 30L Gaming Desktop PC is now {price}"

    with smtplib.SMTP("YOUR_SMTP_ADDRESS", port=587) as connection:
        connection.starttls()
        result = connection.login("YOUR_EMAIL", "YOUR_PASSWORD")
        connection.sendmail(
            from_addr="YOUR_EMAIL",
            to_addrs="YOUR_EMAIL",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{product_url}"
        )

