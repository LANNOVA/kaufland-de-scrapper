#mind donating SRAVstudios
#BTC - bc1q5kmqqynratseyh7v0n8q58rn7p5xejuemmc4px

#USDT(ETH) - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

#USDT(SOLANA) - 4MjmiAwiQT1cqb5fSpvdsKCabZAKxopcMsTqem9gWBqB

#USDT(POLYGON) - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

#ETH - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

import requests
import json

HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
tos = input('what to search? ')
url = 'https://api.cloud.kaufland.de/search/v4/results/?requestType=initial-load&pageType=search&searchValue=' + tos
kaufland = requests.get(url, headers=HEADERS)
#no description
kauflanddetails = json.loads(kaufland.text)
count = 0
items = len(kauflanddetails['products'])
while(count < items):
    print(count)
    items = len(kauflanddetails['products'])
    producttitle = kauflanddetails['products'][count]['title']
    rating = kauflanddetails['products'][count]['ratings']['average']
    price = kauflanddetails['products'][count]['price']['current']
    buylink = kauflanddetails['products'][count]['link']['url']
    delivery = kauflanddetails['products'][count]['delivery']['timePhrase']
    ean = kauflanddetails['products'][count]['ean']
    manufacturer = kauflanddetails['products'][count]['manufacturer']['title']
    print(producttitle)
    print(rating)
    print(price)
    print(buylink)
    print(delivery)
    print(ean)
    print(manufacturer)
    print('')
    count += 1

#mind donating SRAVstudios
#BTC - bc1q5kmqqynratseyh7v0n8q58rn7p5xejuemmc4px

#USDT(ETH) - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

#USDT(SOLANA) - 4MjmiAwiQT1cqb5fSpvdsKCabZAKxopcMsTqem9gWBqB

#USDT(POLYGON) - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

#ETH - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572
