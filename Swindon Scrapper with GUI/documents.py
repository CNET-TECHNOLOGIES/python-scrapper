from selenium import webdriver
import pandas as pd
import csv
from selenium.webdriver.common.by import By
from time import sleep

tempmonths = ["Feb 22", "Jan 22", "Dec 21", "Nov 21", "Oct 21", "Sep 21", "Aug 21", "Jul 21", "Jun 21", "May 21",
              "Apr 21", "Mar 21"]


class Documents:

    def scrape_documents_validated(temp_months, mainpath):
        try:
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            args = ["hide_console", ]
            driver = webdriver.Chrome(options=options, service_args=args)

            for month in temp_months:
                try:
                    month = month.lower().replace(" ", "")
                    path = "/".join([mainpath, month, "validated"])

                    df = pd.read_csv("/".join([path, f"validated_{month}keys.csv"]))
                    data = []
                    fields = []

                    for key, ref in df.values:
                        print(f"{key},{ref} -->, {month} --> validated")
                        link = f"https://pa1.swindon.gov.uk/publicaccess/applicationDetails.do?keyVal={key}&activeTab=documents"
                        driver.get(link)
                        driver.maximize_window()

                        tr_th = driver.find_elements(By.XPATH, "//*[@id='Documents']/tbody/tr[1]/th")
                        tr_td = driver.find_elements(By.XPATH, "//*[@id='Documents']/tbody/tr")

                        for i in tr_th:
                            if i.text.strip() not in fields:
                                fields.append(i.text.strip())

                        fields[0] = "Ref No"
                        for i in tr_td:
                            temp = []
                            try:
                                tds = i.find_elements(By.TAG_NAME, "td")
                                for td in tds:
                                    try:
                                        temp.append(td.find_element(By.TAG_NAME, "a").get_attribute("href"))
                                    except:
                                        temp.append(td.text.strip())
                                temp[0] = ref

                                if temp:
                                    q = {fields: temp for fields, temp in zip(fields, temp)}
                                    data.append(q)
                            except:
                                continue

                        print(len(tr_th))
                    with open("/".join([path, f"validated_documents_{month}.csv"]), 'w', encoding='UTF8', newline='') as f:
                        writer = csv.DictWriter(f, fieldnames=fields)

                        writer.writeheader()

                        writer.writerows(data)
                        sleep(1)
                except Exception as e:
                    print(e)
                    continue

            driver.quit()
        except Exception as e:
            print(e)

    def scrape_documents_decided(temp_months, mainpath):
        try:
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            args = ["hide_console", ]
            driver = webdriver.Chrome(options=options, service_args=args)

            for month in temp_months:
                try:
                    month = month.lower().replace(" ", "")
                    path = "/".join([mainpath, month, "decided"])

                    df = pd.read_csv("/".join([path, f"decided_{month}keys.csv"]))
                    data = []
                    fields = []
                    for key, ref in df.values:
                        print(f"{key},{ref} -->, {month} --> Decided")
                        link = f"https://pa1.swindon.gov.uk/publicaccess/applicationDetails.do?keyVal={key}&activeTab=documents"
                        driver.get(link)
                        driver.maximize_window()

                        tr_th = driver.find_elements(By.XPATH, "//*[@id='Documents']/tbody/tr[1]/th")
                        tr_td = driver.find_elements(By.XPATH, "//*[@id='Documents']/tbody/tr")

                        fields = [i.text.strip() for i in tr_th]
                        fields[0] = "Ref No"
                        for i in tr_td:
                            temp = []
                            try:
                                tds = i.find_elements(By.TAG_NAME, "td")
                                for td in tds:
                                    try:
                                        temp.append(td.find_element(By.TAG_NAME, "a").get_attribute("href"))
                                    except:
                                        temp.append(td.text.strip())
                                temp[0] = ref

                                if temp:
                                    q = {fields: temp for fields, temp in zip(fields, temp)}
                                    data.append(q)
                            except:
                                continue

                        print(len(tr_th))
                    with open("/".join([path, f"decided_documents_{month}.csv"]), 'w',
                              encoding='UTF8', newline='') as f:
                        writer = csv.DictWriter(f, fieldnames=fields)

                        writer.writeheader()

                        writer.writerows(data)
                        sleep(1)
                except Exception as e:
                    print(e)
                    continue

            driver.quit()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    Documents()
