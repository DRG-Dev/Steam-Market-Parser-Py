import requests
from bs4 import BeautifulSoup
import json

def get_first_items():
    headers ={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"
    }

    url = "https://steamcommunity.com/market/search?q=&category_252490_itemclass%5B0%5D=any&appid=252490#p44_popular_desc"
    r = requests.get(url = url, headers= headers)
    soup = BeautifulSoup(r.text,"html.parser")
    skin_cards = soup.findAll("div", {"class":"market_listing_row market_recent_listing_row market_listing_searchresult"})
    skins_dict ={}
    for skin in skin_cards:
        skin_Title = skin.find("span", class_="market_listing_item_name").text.strip()
        skin_Cost = skin.find("span", class_="normal_price").text.strip()
        skin_image_url = skin.find("img", class_="market_listing_item_img").get("src")

        skin_Id = skin_image_url.split("/")[-2]
        print(f"{skin_Title} | {skin_Cost} | {skin_image_url}")

        skins_dict[skin_Id] = {
            "skin_Title": skin_Title,
             "skin_Cost": skin_Cost,
            "skin_image_url": skin_image_url
        }




    with open("Skins_info","w") as file:
        json.dump(skins_dict, file, indent= 4, ensure_ascii=False)


def main():
    get_first_items()

if __name__ == '__main__':
    main()