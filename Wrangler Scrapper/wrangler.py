from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep
import csv
from lxml import html
import requests


def main():
    url = "https://www.wrangler.in/men/bottomwear/jeans.html?gclid=CjwKCAiAjoeRBhAJEiwAYY3nDHYvJjglcO3Hm2n3zy2aNIQdDP9CEmXDLOXZd8rrvEOGaq855COmlxoCOvAQAvD_BwE&utm_campaign=Brand&utm_content=Text&utm_medium=CPC&utm_source=Search&utm_term=Sales"

    driver = webdriver.Chrome()
    driver.get(url)

    # try:
    #     driver.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']").click()
    # except:
    #     pass

    sleep(2)

    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        sleep(2)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    links_objects = driver.find_elements(By.XPATH, "//*[@class='product-item-info']/div/strong/a")

    actions = ActionChains(driver)

    data = []

    sr_no = 1

    brandname = "WRANGLER"
    print(f"Brand => {brandname}")

    country = "INDIA"
    print(f"Country => {country}")

    p_type = "MJ"
    print(f"Type => {p_type}")

    links = [i.get_attribute("href") for i in links_objects]

    driver.quit()

    try:

        for link in links:
            print(f"Product => {link}")

            with requests.get(link) as response:
                doc = html.fromstring(response.content)

                image_url = doc.xpath("//div[@class='gallery-placeholder _block-content-loading']//img/@src")[0]

                print(f"Image => {image_url}")

                product_title = doc.xpath("//*[@id='html-body']/div[2]/div[3]/div/ul/li[last()]/strong")[0].text

                print(f"Product Title => {product_title}")

                prices = doc.xpath("//span[@class='price']")

                price_local = int(prices[0].text.replace("₹", "").replace(",", ""))

                print(f"Price Local => {price_local}")

                if len(prices) > 1:
                    original_price = int(prices[1].text.replace("₹", "").replace(",", ""))
                    discount = original_price - price_local
                    print(f"Discount => {discount}")

                else:
                    discount = ""

                local = "INR"

                price_usd = ""

                description = doc.xpath("//*[@id='description']/div/div")[0].text
                print(f"Description => {description}")

                q = {
                    "Serial No.": sr_no,
                    "Brandname": brandname,
                    "Country": country,
                    "PRODUCT URL": link,
                    "Type": p_type,
                    "IMAGE URL": image_url,
                    "TITLE OF PRODUCT": product_title,
                    "PRICE Local": price_local,
                    "Local": local,
                    "Discount": discount,
                    "Price USD": price_usd,
                    "Description": description
                }

                data.append(q)

                sr_no += 1

                print("------***********************************------")

    finally:

        fields = ["Serial No.", "Brandname", "Country", "PRODUCT URL", "Type", "IMAGE URL", "TITLE OF PRODUCT",
                  "PRICE Local", "Local", "Discount", "Price USD", "Description"]

        with open("wrangle1r.csv", 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fields)

            writer.writeheader()

            writer.writerows(data)

        print("Excel generated")


if __name__ == '__main__':
    main()
    # //div[@class='section-info-single-product-plp']
