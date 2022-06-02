import requests
import csv
import json
from bs4 import BeautifulSoup


def main():
    fetch_pin = "https://www.apartments.com/services/geography/search/"

    pincode = int(input("Enter Pincode :> "))

    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }

    t = "46289-arabia-st_indio-ca/"

    with requests.post(fetch_pin, json={"t": pincode, "l": [-89.755, 30.366]}, headers=header) as response:

        data = json.loads(response.content)

        city = data[0]["Address"]["City"].replace(" ", "-").lower()
        # print(city)

        state = data[0]["Address"]["State"].lower()
        # print(state)

        try:
            pin = data[0]["Address"]["PostalCode"].lower()

            link = "".join([city, "-", state, "-", pin, "/"])

        except:

            street = data[0]["Address"]["StreetName"].replace(" ", "-").lower()

            # print(":> ", street)

            if "drive" in street:
                street = street.replace("drive", "dr")
            elif "street" in street:
                street = street.replace("street", "st")

            link = "".join([street, "_", city, "-", state, "/"])

        # print(link)

        link = f"https://www.apartments.com/{link}"

        print("URL :> ", link)

        # scrape(link, pincode)


def scrape(url, pincode):

    dump = []

    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }

    with requests.get(url, headers=header) as resonse:
        soup = BeautifulSoup(resonse.content, "html.parser")

        data = soup.find("script", {"type": "application/ld+json"}).text.strip()

        data = json.loads(data)
        data = data["about"]

        for i in data:

            # print(i)

            url = i["url"]
            print("URL :> ", url)

            name = i["name"]
            print("Name :> ", name)

            img = i["image"]
            print("Image :> ", img)

            street = i["Address"]["streetAddress"]
            print("Street :> ", street)

            locality = i["Address"]["addressLocality"]
            print("Locality :> ", locality)

            region = i["Address"]["addressRegion"]
            print("Region :> ", region)

            postalcode = i["Address"]["postalCode"]
            print("Post Code :> ", postalcode)

            country = i["Address"]["addressCountry"]
            print("Country :> ", country)

            telephone = i["telephone"]
            print("Telephone :> ", telephone)

            q = {
                "URL": url,
                "Name": name,
                "Telephone": telephone,
                "Street": street,
                "Locality": locality,
                "Region": region,
                "Post code": postalcode,
                "Country": country,
                "Image URL": img
            }

            dump.append(q)

            print("-----------------------------")

        fields = ["URL", "Name", "Telephone", "Street", "Locality", "Region", "Post code", "Country", "Image URL"]

        with open("".join(["data/", "apartments_", str(pincode), ".csv"]), "w", encoding="UTF8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)

            writer.writeheader()

            writer.writerows(dump)

        print("Excel generated")



if __name__ == '__main__':
    main()
    # scrape("https://www.apartments.com/kansas-city-mo-64137/")
