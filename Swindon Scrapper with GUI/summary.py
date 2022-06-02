from selenium import webdriver
import pandas as pd
import csv
from selenium.webdriver.common.by import By

tempmonths = ["Feb 22", "Jan 22", "Dec 21", "Nov 21", "Oct 21", "Sep 21", "Aug 21", "Jul 21", "Jun 21", "May 21",
              "Apr 21", "Mar 21"]


class Summary:

    def scrape_summary_validated(temp_month, mainpath):
        try:
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            args = ["hide_console", ]
            driver = webdriver.Chrome(options=options, service_args=args)

            for month in temp_month:
                try:
                    month = month.lower().replace(" ", "")
                    path = "/".join([mainpath, month, "validated"])

                    df = pd.read_csv("/".join([path, f"validated_{month}keys.csv"]), usecols=["keys"])
                    data = []
                    fields = []
                    for key in df.values:
                        q = {}
                        print(f"{key[0]}, -->, {month} --> validated")
                        link = f"https://pa1.swindon.gov.uk/publicaccess/applicationDetails.do?keyVal={key[0]}&activeTab=summary"
                        driver.get(link)
                        driver.maximize_window()

                        tr = driver.find_elements(By.XPATH, "/html/body/div/div/div[3]/div[3]/div[3]/table/tbody/tr")
                        for i in tr:
                            th = i.find_element(By.TAG_NAME, "th").text
                            td = i.find_element(By.TAG_NAME, "td").text
                            print(th, ":", td)
                            if th not in fields:
                                fields.append(th)
                            q[th] = td

                        print(len(tr))
                        data.append(q)

                    with open("/".join([path, f"validated_summary_{month}.csv"]), 'w', encoding='UTF8', newline='') as f:
                        writer = csv.DictWriter(f, fieldnames=fields)

                        writer.writeheader()

                        writer.writerows(data)

                except:
                    continue
            driver.quit()
        except Exception as e:
            print(e)

    def scrape_summary_decided(temp_month, mainpath):
        try:
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            args = ["hide_console", ]
            driver = webdriver.Chrome(options=options, service_args=args)

            for month in temp_month:
                try:
                    month = month.lower().replace(" ", "")
                    path = "/".join([mainpath, month, "decided"])

                    df = pd.read_csv("/".join([path, f"decided_{month}keys.csv"]), usecols=["keys"])
                    data = []
                    fields = []
                    for key in df.values:
                        q = {}
                        print(f"{key[0]}, -->, {month} --> decided")
                        link = f"https://pa1.swindon.gov.uk/publicaccess/applicationDetails.do?keyVal={key[0]}&activeTab=summary"
                        driver.get(link)
                        driver.maximize_window()

                        tr = driver.find_elements(By.XPATH, "/html/body/div/div/div[3]/div[3]/div[3]/table/tbody/tr")
                        for i in tr:
                            th = i.find_element(By.TAG_NAME, "th").text
                            td = i.find_element(By.TAG_NAME, "td").text
                            print(th, ":", td)
                            if th not in fields:
                                fields.append(th)
                            q[th] = td

                        print(len(tr))
                        data.append(q)

                    with open("/".join([path, f"decided_summary_{month}.csv"]), 'w', encoding='UTF8', newline='') as f:
                        writer = csv.DictWriter(f, fieldnames=fields)

                        writer.writeheader()

                        writer.writerows(data)

                except:
                    continue
            driver.quit()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    Summary()
