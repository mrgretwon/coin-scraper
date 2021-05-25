import requests

from bs4 import BeautifulSoup as bs

from receivers import RECEIVERS


url = 'https://www.coingecko.com/en/coins/'
with open(r'last_coin.txt', 'r') as last_coin_file:
    lines = last_coin_file.readlines()
last_coin_id = int(lines[0])

new_last_coin_id = last_coin_id

message = ''

for id in range(last_coin_id + 1, last_coin_id + 10):
    page = requests.get(url + str(id))
    if page.status_code != 200:
        continue
    soup = bs(page.content, 'html.parser')
    if 'binance-coin-logo' in str(soup.find('span', class_='text-muted mr-2').find('img')):
        network = 'BSC'
    elif 'ethereum' in str(soup.find('span', class_='text-muted mr-2').find('img')):
        network = 'ETH'
    else:
        network = 'Other'
    try:
        coin = soup.find(
            'h1', class_='mr-md-3 mx-2 mb-md-0 text-3xl font-semibold').get_text(strip=True)
        message += f"<p>{coin}    -   {network}   -   {url + str(id)}<br></p>"
        new_last_coin_id = id
    except:
        continue

if message != '':
    from mail import send_email
    for receiver in RECEIVERS:
        send_email(receiver, message)

if new_last_coin_id != last_coin_id:
    with open(r'last_coin.txt', 'w') as last_coin_file:
        last_coin_file.write(str(new_last_coin_id))
