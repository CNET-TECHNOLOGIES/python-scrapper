from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv
import re
import requests
from bs4 import BeautifulSoup


def main():

    data = []
    url = "https://www.facebook.com/search/pages?q=salon%20manchester"

    driver = webdriver.Chrome()

    driver.get(url)
    sleep(2)

    driver.find_element(By.XPATH, "//input[@id='email']").send_keys("newfackid007@gmail.com")

    driver.find_element(By.XPATH, "//input[@id='pass']").send_keys("AUTOdownload@123")

    driver.find_element(By.XPATH, "//button[@id='loginbutton']").click()
    sleep(3)

    driver.get(url)

    headers = {"user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"}

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:

        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        sleep(2)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height

    links = driver.find_elements(By.XPATH, "//div[@class='hpfvmrgz g5gj957u buofh1pr rj1gh0hx o8rfisnq']//a")

    for link in links:

        href = link.get_attribute("href")

        l = href

        if re.search("/$", href):
            href = href + "about"
        else:
            if "profile.php?" in href:
                href = href + "&sk=about"
            else:
                href = href + "/about"

        print("-----------------------------------------")
        print(href)


        try:
            o = f"window.open('{href}', 'new_window')"
            driver.execute_script(o)
            sleep(2)

            driver.switch_to.window(driver.window_handles[1])
            sleep(1)

            datas = driver.find_elements(By.XPATH, "//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh jq4qci2q a3bd9o3v b1v8xokw py34i1dx']/a")
            mail = None
            try:
                phone = driver.find_elements(By.XPATH, "//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh jq4qci2q a3bd9o3v b1v8xokw oo9gr5id']")
                phone = phone[-1].text
                if (("+" not in phone) and (not phone.strip().isdigit())) or ("people" in phone):
                    phone = ""
            except:
                try:
                    phone = driver.find_element(By.XPATH, "//ul[@class='bi6gxh9e']/li//span").text
                    if (("+" not in phone) and (not phone.strip().isdigit())) or ("people" in phone):
                        phone = ""
                except:
                    phone = ''

            print("Phone > ", phone)

            try:
                website = datas[0].get_attribute("href")
                if "http" not in website:
                    if "mailto:" in website:
                        mail = website
                    website = ""
            except:
                try:
                    website = driver.find_element(By.XPATH, "//ul[@class='bi6gxh9e']//a").get_attribute("href")
                    if "http" not in website:
                        if "mailto:" in website:
                            mail = website
                        website = ""
                except:
                    website = ""

            print("Website > ", website)

            try:
                mail = datas[1].get_attribute("href")
                if "mailto:" not in mail:
                    mail = ""
            except:
                try:
                    if not mail:
                        mail = driver.find_elements(By.XPATH, "//ul[@class='bi6gxh9e']/li/div/div/div[1]/span")[0].text
                        if "@gmail" not in mail:
                            mail = driver.find_elements(By.XPATH, "//ul[@class='bi6gxh9e']/li/div/div/div[1]/span")[1].text
                            if "@gmail" not in mail:
                                mail = ""
                except:
                    if not mail:
                        mail = ""

            print("Mail > ", mail)

            try:
                about = driver.find_element(By.XPATH, "//div[@class='kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql']").text
            except:
                about = ""

            print("About > ", about)

            q = {
                "Page Link": l,
                "Phone": phone,
                "Website": website,
                "Email": mail,
                "About": about
            }

            data.append(q)

            driver.close()

            driver.switch_to.window(driver.window_handles[0])
            sleep(1)

        except Exception as e:
            print(e)
            continue

    fields = ["Page Link", "Phone", "Website", "Email", "About"]

    with open("fbpages.csv", 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields)

        writer.writeheader()

        writer.writerows(data)

    print("****************************************")
    print(f"Excel Completed")

    print(f"Total links {len(links)}")

    driver.quit()


if __name__ == '__main__':
    main()
