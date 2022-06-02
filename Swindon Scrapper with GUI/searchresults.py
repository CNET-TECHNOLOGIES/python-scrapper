from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import csv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import urlparse
from os import makedirs
from time import sleep


def keys_insert(k, path, month):
    try:
        fields = ["keys", "Ref No"]
        with open("/".join([path, f"{month}keys.csv"]), 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fields)

            writer.writeheader()

            writer.writerows(k)
    except Exception as e:
        print(e)


class SearchResults:

    def fetch_results_validated(temp_month, mainpath):
        try:
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            args = ["hide_console", ]
            driver = webdriver.Chrome(options=options, service_args=args)

            for month in temp_month:
                try:
                    driver.maximize_window()
                    driver.get("https://pa1.swindon.gov.uk/publicaccess/search.do?action=monthlyList")

                    validated_select = Select(driver.find_element(By.ID, "month"))

                    print(f"----------In Validated = {month}-------------")
                    validated_select.select_by_value(month)
                    driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[3]/div/form/fieldset/div[5]/input[2]").click()

                    validated_select1 = Select(driver.find_element(By.ID, "resultsPerPage"))
                    validated_select1.select_by_value("100")
                    driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[3]/div[2]/form/input[4]").click()

                    data = []
                    k = []

                    while 1:

                        results = driver.find_elements(By.CLASS_NAME, "searchresult")

                        for element in results:
                            # title
                            link = element.find_element(By.TAG_NAME, "a")
                            title = link.text
                            link = link.get_attribute('href')
                            key = urlparse(link).query.split("&")[0].split("=")[1]

                            # address
                            add = element.find_element(By.CLASS_NAME, "address").text

                            # metaInfo
                            meta = element.find_element(By.CLASS_NAME, "metaInfo").text
                            meta = meta.split('|')
                            meta = [i.split(':') for i in meta]

                            print(link, "\t", key)
                            ke = {
                                "keys": key,
                                "Ref No": meta[0][1].strip()
                            }

                            q = {
                                "Title": title,
                                "Address": add,
                                "Ref No": meta[0][1].strip(),
                                "Received Date": meta[1][1].strip(),
                                "Validated Date": meta[2][1].strip(),
                                "Status": meta[3][1].strip()
                            }
                            data.append(q)
                            k.append(ke)

                        try:
                            wait = WebDriverWait(driver, 10)
                            n = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "next")))
                            n.click()
                        except:
                            break

                    fields = ["Title", "Address", "Ref No", "Received Date", "Validated Date", "Status"]
                    month = month.replace(" ", "").lower()
                    path = "/".join([mainpath, month, "validated"])

                    try:
                        makedirs(path)
                    except:
                        pass

                    month = "_".join(["validated", month])
                    with open("/".join([path, month + ".csv"]), 'w', encoding='UTF8', newline='') as f:
                        writer = csv.DictWriter(f, fieldnames=fields)

                        writer.writeheader()

                        writer.writerows(data)
                    keys_insert(k, path, month)
                    print(len(data))
                    sleep(1)
                except Exception as e:
                    print(e)
                    continue
            driver.quit()
        except Exception as e:
            print(e)

    def fetch_results_decided(temp_month, mainpath):
        try:
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            args = ["hide_console", ]
            driver = webdriver.Chrome(options=options, service_args=args)

            for month in temp_month:
                try:
                    driver.get("https://pa1.swindon.gov.uk/publicaccess/search.do?action=monthlyList")
                    driver.maximize_window()

                    decided_select = Select(driver.find_element(By.ID, "month"))

                    # select month
                    print(f"----------In Decided = {month}-------------")
                    decided_select.select_by_value(month)

                    # select Decided this month
                    driver.find_element(By.ID, "dateDecided").click()

                    # click search
                    driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[3]/div/form/fieldset/div[5]/input[2]").click()

                    # Selecting maximum results per page
                    decided_select1 = Select(driver.find_element(By.ID, "resultsPerPage"))
                    decided_select1.select_by_value("100")
                    driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[3]/div[2]/form/input[4]").click()

                    data = []
                    k = []

                    while 1:

                        results = driver.find_elements(By.CLASS_NAME, "searchresult")

                        for element in results:
                            # title
                            link = element.find_element(By.TAG_NAME, "a")
                            title = link.text
                            link = link.get_attribute('href')
                            key = urlparse(link).query.split("&")[0].split("=")[1]

                            # address
                            add = element.find_element(By.CLASS_NAME, "address").text

                            # metaInfo
                            meta = element.find_element(By.CLASS_NAME, "metaInfo").text
                            meta = meta.split('|')
                            meta = [i.split(':') for i in meta]

                            print(link, "\t", key)
                            ke = {
                                "keys": key,
                                "Ref No": meta[0][1].strip()
                            }

                            q = {
                                "Title": title,
                                "Address": add,
                                "Ref No": meta[0][1].strip(),
                                "Received Date": meta[1][1].strip(),
                                "Validated Date": meta[2][1].strip(),
                                "Status": meta[3][1].strip()
                            }
                            data.append(q)
                            k.append(ke)

                        try:
                            wait = WebDriverWait(driver, 10)
                            n = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "next")))
                            n.click()
                        except:
                            break

                    fields = ["Title", "Address", "Ref No", "Received Date", "Validated Date", "Status"]
                    month = month.replace(" ", "").lower()
                    path = "/".join([mainpath, month, "decided"])

                    try:
                        makedirs(path)
                    except:
                        pass
                    month = "_".join(["decided", month])
                    with open("/".join([path, month + ".csv"]), 'w', encoding='UTF8', newline='') as f:
                        writer = csv.DictWriter(f, fieldnames=fields)

                        writer.writeheader()

                        writer.writerows(data)
                    keys_insert(k, path, month)
                    print(len(data))
                    sleep(1)
                except Exception as e:
                    print(e)
                    continue
            driver.quit()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    SearchResults()
