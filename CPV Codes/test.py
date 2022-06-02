import requests
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd


def main():
    url = "https://www.bipsolutions.com/news-and-resources/cpv-codes/"

    driver = webdriver.Chrome()

    df = pd.read_csv("divisionids.csv", converters={'Div_id': lambda x: str(x)})

    driver.get(url)

    data = []
    for div in df.values:
        driver.find_element(By.ID, "searchtext").clear()

        driver.find_element(By.ID, "searchtext").send_keys(div)

        div_id = driver.find_element(By.XPATH, "//*[@id='treeview']/ul/li")

        try:
            print(div_id.text)
            div_ = div_id.text.replace(" ", "").split(":")[0]
            name = div_id.text.split(":")[1].strip()
            q = {
                "Product_name": name,
                "Div_id": div_,
                "Group_id": "",
                "Class_id": "",
                "Cat_id": ""

            }
            data.append(q)
            div_id.click()
            # time.sleep(1)
            try:
                group_ids = driver.find_elements(By.XPATH, '//*[@id="treeview"]/ul/ul/li/a')
                for i in range(1, len(group_ids) + 1):
                    temp = f'//*[@id="treeview"]/ul/ul/li[{i}]/a'
                    g_text = driver.find_element(By.XPATH, temp)
                    print(g_text.text)

                    g_excel = g_text.text.replace(" ", "").split(":")[0]
                    name_g = g_text.text.split(":")[1].strip()
                    q = {
                        "Product_name": name_g,
                        "Div_id": div_,
                        "Group_id": g_excel,
                        "Class_id": "",
                        "Cat_id": ""

                    }
                    data.append(q)

                    g_text.click()
                    # time.sleep(1)

                    try:
                        class_id = driver.find_elements(By.XPATH, '//*[@id="treeview"]/ul/ul/ul/li/a')
                        for j in range(1, len(class_id) + 1):
                            temp_c = f'//*[@id="treeview"]/ul/ul/ul/li[{j}]/a'
                            c_text = driver.find_element(By.XPATH, temp_c)
                            print(c_text.text)

                            c_excel = c_text.text.replace(" ", "").split(":")[0]
                            name_c = c_text.text.split(":")[1].strip()
                            q = {
                                "Product_name": name_c,
                                "Div_id": div_,
                                "Group_id": g_excel,
                                "Class_id": c_excel,
                                "Cat_id": ""

                            }
                            data.append(q)

                            c_text.click()
                            # time.sleep(1)

                            try:
                                cat_id = driver.find_elements(By.XPATH,
                                                              '//*[@id="treeview"]/ul/ul/ul/ul/li/a')
                                for x in range(1, len(cat_id) + 1):
                                    temp_cat = f'//*[@id="treeview"]/ul/ul/ul/ul/li[{x}]/a'
                                    cat_text = driver.find_element(By.XPATH, temp_cat)
                                    print(cat_text.text)

                                    cat_excel = cat_text.text.replace(" ", "").split(":")[0]
                                    name_cat = cat_text.text.split(":")[1].strip()
                                    q = {
                                        "Product_name": name_cat,
                                        "Div_id": div_,
                                        "Group_id": g_excel,
                                        "Class_id": c_excel,
                                        "Cat_id": cat_excel

                                    }
                                    data.append(q)

                                    cat_text.click()
                                    # time.sleep(1)

                                    try:
                                        child_cat_id = driver.find_elements(By.XPATH,
                                                                            '//*[@id="treeview"]/ul/ul/ul/ul/ul/li/a')
                                        for y in range(1, len(child_cat_id) + 1):
                                            temp_child = f'//*[@id="treeview"]/ul/ul/ul/ul/ul/li[{y}]/a'
                                            child = driver.find_element(By.XPATH, temp_child)
                                            print(child.text)

                                            child_excel = child.text.replace(" ", "").split(":")[0]
                                            name_child = child.text.split(":")[1].strip()
                                            q = {
                                                "Product_name": name_child,
                                                "Div_id": div_,
                                                "Group_id": g_excel,
                                                "Class_id": c_excel,
                                                "Cat_id": child_excel

                                            }
                                            data.append(q)

                                    except Exception as e:
                                        print(e)
                                        continue

                                    finally:
                                        c_temp = driver.find_element(By.XPATH, temp_c)
                                        c_temp.click()

                            except Exception as e:
                                print(e)
                                continue

                            finally:
                                t_text = driver.find_element(By.XPATH, temp)
                                t_text.click()

                    except Exception as e:
                        print(e)

                    finally:
                        t_text = driver.find_element(By.XPATH,  "//*[@id='treeview']/ul/li")
                        t_text.click()

            except Exception as e:
                print(e)
                continue

        except Exception as e:
            print(e)


    fields = ["Product_name", "Div_id", "Group_id", "Class_id", "Cat_id"]

    with open("finalresult.csv", 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields)

        writer.writeheader()

        writer.writerows(data)

    driver.quit()


if __name__ == '__main__':
    main()

# class_id = driver.find_elements(By.CLASS_NAME, "cpv-click")
# cat_id = driver.find_elements(By.CLASS_NAME, "cpv-click")
