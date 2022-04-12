import os
from urllib import response
import requests
from bs4 import BeautifulSoup
from time import sleep
from notify_run import Notify 

# Headers and cookies from a real requests so I don't trigger any bot heuristics. Might need to update these.
cookies = {
    '_sp_krux': 'true',
    '_sp_enable_dfp_personalized_ads': 'true',
    '_sp_v1_uid': '1:617:376a2caf-18fa-4bd5-9f0e-6769dfe37dab',
    '_sp_v1_data': '2:293384:1638804189:0:537:0:537:0:0:_:-1',
    '_sp_v1_ss': '1:H4sIAAAAAAAAAItWqo5RKimOUbKKRmbkgRgGtbE6MUqpIGZeaU4OkF0CVlBdi1tCSQe7gaRaEaOUmZdZAmQZmhlbmpsZGRgZ47GVDHfGAgAjO3HT-gAAAA%3D%3D',
    '_sp_v1_opt': '1:login|true:last_id|11:',
    '_sp_v1_consent': '1!1:1:1:0:0:0',
    '_sp_v1_csv': 'null',
    '_sp_v1_lt': '1:',
    'consentUUID': 'aa21e3d6-e2d3-407b-9b38-cc521bba33c8_2_3_4_5',
    'euconsent-v2': 'CPV-MQAPV-MQAAGABCENCGCgAP_AAFPAAApAGdgBxThEQCFAAGBIQoEAAIAUQAAEACAAAAAAAQIBAACAIAQCAAEAAACABAACAAAAAAABAABEAAAAAAAAAAAQABGAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAACEAAAiAgAAAIAAAAAgZ3AggAUABYAEgAKgAXAA4ACAAEgAMgAaQBEAEUAJgATwAxABzAEIAJgAUoA2QB-gEIAIiARYAkQBWQDFAH2AP2AmQBbIC8wGMgM7APGQAgAmALzEQAQBshIAIAfgoAcABQAEgCEAFZAP2AtkBjIaACANkVACACYAvMdABAD8PADAAKAAkAVkA_YDGQGdjgAQALQBCEQAYBWQD9gM7JgAwCsgH7AYySABABUAEIUgAgB-KgAwCsgH7AYyUABgAtACoAIQAAA.YAAAAAAAAAAA',
    'md': 'th',
    'footer_gallery_visited': '96547746,96897968,96902849,96917081,96726182,96723958,96652133,96140736,96351448,96069090,95594377,94874255,95748104,95843465,96629171,96581288,95650773,96418782,95506663,96374824,96379384,95926314,96291335,96189042,96294412,94534145,96096336,96209661,96270566,94279086,95852939,96198867,96244307,96216261,96184692,96053662,96144340,96176465,96183272,96172860,96033510,96002491,96104710,95418269,95897297,95893768,95815111,95641476,95958062,96067101',
    'toricmp_store_data': '0',
    'toricmp_marketing': '0',
    'toricmp_analytics': '0',
    'toricmp_personalisation': '0',
    'toricmp_vendor_pulse': '0',
    'toricmp_vendor_hotjar': '1',
    'toricmp_vendor_abtasty': '1',
    'toricmp_vendor_facebook': '1',
    'toricmp_vendor_gtm': '1',
    'toricmp_vendor_gar': '1',
    'toricmp_purpose3': '1',
    'toricmp_purpose4': '1',
    'toricmp_purpose6': '1',
    'cis-jwe': 'eyJpc3N1ZWRBdCI6IjIwMjItMDItMDJUMjM6NDY6MzBaIiwiZW5jIjoiQTEyOENCQy1IUzI1NiIsImFsZyI6ImRpciIsImtpZCI6IjIifQ..TOLrqY2Oa5-EdmcGhbqPHg.rQURXOdj5OWbmrf8kibGY7FxDBrU-ibeM_EjRcSLd6tPfH8A9QRIe39oYNKwz0mhAdR0XjR_ECn4Ry5-vFZrEGBZP1Tu6TMIYXqB3OK4V3PnoThQ-rKICOTF1OYAe9g39fERqw_xWxE61bU2w6YadhxEQwx-vp8_ZcOxtX6vsNJS1tg8vEG3dznbtZDirOao1bzujgWYBtWUKqvWBZlkmA.gXrafoy7aT-4RkKzuUt5jg',
    '_pulse2data': 'e75e435e-a951-4903-b7b1-de382e37c28d%2Cv%2C%2C1650466496497%2CeyJpc3N1ZWRBdCI6IjIwMjItMDItMDJUMjM6NDY6MzBaIiwiZW5jIjoiQTEyOENCQy1IUzI1NiIsImFsZyI6ImRpciIsImtpZCI6IjIifQ..AQa_iFFziUytsfIOcxPalQ.ZzEqR7XgYapcfRxEU5_vE1ZLmgPR2dPjZtyQMciD6itT5ocQi_GnEwywWJYm2NSNUfKmW7jpniNnnNOpNI0eeP6Dd-oqOkzVwPfixHiN30K3zKuQkC63k6chWu5ILGozO9UFgwNteb8pk8f1_6PVVK52ZZaYAe-QhliONEkqHdxV61Cq49-9ECJ4tPOzROpHTD41iUQMP8IFH2j1kWQ0PA.YPYDi8jcbeO212z61cE2dg%2C%2C0%2Ctrue%2C%2CeyJraWQiOiIyIiwiYWxnIjoiSFMyNTYifQ..r4vrpPmPYQF3_bbZq-ZoOMUeax3XuRnxXuhqBmsqiYY',
    'stat_counter': '1',
    '_pulsesession': '%5B%22sdrn%3Aschibsted%3Asession%3A139918e3-25c7-4109-b77c-737f394c31fb%22%2C1650465596499%2C1650465620070%5D',
    'saSimpleLoginShown': '1',
    'sq': 'q=ilmastointilaite&cg=0&w=1&st=s&st=k&st=u&st=h&st=g&ca=18&l=0&md=th',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.tori.fi/koko_suomi?q=ilmastointilaite&cg=0&w=3',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Cache-Control': 'max-age=0',

}

params = {
    'q': 'ilmastointilaite',
    'cg': '0',
    'w': '1',
    'st': [
        's',
        'k',
        'u',
        'h',
        'g',
    ],
    'ca': '18',
    'l': '0',
    'md': 'th',
}

LOWER_PRICE = 80
UPPER_PRICE = 250
QUERY = "trinitron"
CATEGORY_URL = "https://www.tori.fi/uusimaa?q={}&cg=3010&w=1&st=s&st=g&c=0&ca=18&l=0&f=p&md=th"

def main():
    parsed = []
    notify = Notify() 
    while(True):
        
        #print(os.environ["PATH"])
        res = fetch(QUERY)
        products = parse(res)
        for product in products:
            name, price, url = product
            # Use URL as a key in the product array
            if url not in parsed:
                parsed.append(url)
                if LOWER_PRICE < price < UPPER_PRICE:
                    # push message with notify.run service for new listings                    
                    notify.send("{}: {} --- {}".format(name, str(price), url))

        print(parsed)
        sleep(60.0)


def fetch(query):
    try:
        return requests.get(CATEGORY_URL.format(query), headers=headers, cookies=cookies).text
    except:
        print("error fetching data")

def parse(response):
    result = []
    #print(response)
    try:
        soup = BeautifulSoup(response, 'html.parser')
        items = soup.find_all("a", class_="item_row_flex")
        for item in items:
            title = item.find("div", class_="li-title").contents[0]
            price = int(item.find("p", class_="list_price").contents[0].replace(" ", "")[:-1])
            url = item["href"]
            print("{}: {} --- {}".format(title, str(price), url))
            result.append((title, price, url))
        print(result)
        return result
    except:
        print("parse error")
        return []

def notify(msg):
    print("Notify: " + msg)

if __name__ == "__main__":
    main()
