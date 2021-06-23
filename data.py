import requests
from bs4 import BeautifulSoup
import lxml

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
}

# Евро
url_eur = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&rlz=1C1SQJL_enRU883RU883&sxsrf=ALeKk02Vs6oik9_Zo8GIm24U7O_aIQMVHg%3A1624280798776&ei=3o7QYIjZLtOk3AP9662ACg&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&gs_lcp=Cgdnd3Mtd2l6EAMyCQgjECcQRhCCAjIFCAAQsQMyBQgAELEDMgUIABCxAzIFCAAQsQMyCAgAELEDEIMBMgIIADIFCAAQyQMyBQgAEJIDMgUIABCxAzoHCAAQRxCwAzoHCAAQsAMQQzoECCMQJzoGCAAQFhAeOgcIABCHAhAUOgQIABAKUMsOWNctYOk0aAFwAngBgAGDA4gBjhiSAQgzMi4xLjEuMZgBAKABAaoBB2d3cy13aXrIAQrAAQE&sclient=gws-wiz&ved=0ahUKEwiIwJrA5ajxAhVTEncKHf11C6AQ4dUDCA4&uact=5"
response_eur = requests.get(url_eur, headers=headers)
soup_eur = BeautifulSoup(response_eur.text, 'lxml')
EUR = soup_eur.find('span', attrs={'class': 'DFlfde SwHCTb'}).text
EUR = EUR.replace(',', '.')
EUR = float(EUR)


# Доллар США
url_usd = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&rlz=1C1SQJL_enRU883RU883&sxsrf=ALeKk004xEb2Cc1lP410fCnheNgqUbK0kg%3A1624281826289&ei=4pLQYLONEfCgrgS8qZ_IDQ&oq=%D0%BA%D1%83%D1%80%D1%81+ljkk&gs_lcp=Cgdnd3Mtd2l6EAEYATIHCAAQhwIQFDIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIHCAAQyQMQCjoHCCMQsAMQJzoHCAAQRxCwAzoHCAAQsAMQQ1DwrApY-7EKYP23CmgBcAJ4AYAB4QOIAfgFkgEFNC40LTGYAQCgAQGqAQdnd3Mtd2l6yAEKwAEB&sclient=gws-wiz"
response_usd = requests.get(url_usd, headers=headers)
soup_usd = BeautifulSoup(response_usd.text, 'lxml')
USD = soup_usd.find('span', attrs={'class': 'DFlfde SwHCTb'}).text
USD = USD.replace(',', '.')
USD = float(USD)


# Австралийский доллар
url_aud = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%B2%D1%81%D1%82%D1%80%D0%B0%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B3%D0%BE+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&rlz=1C1SQJL_enRU883RU883&sxsrf=ALeKk03RS9vmi0iUPWpg0zwpvnMH8RKPUQ%3A1624282321030&ei=0ZTQYPinAezFrgTJvImoDA&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%B2%D1%81%D1%82%D1%80%D0%B0%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B3%D0%BE+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCCMQsAMQJzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQsAMQQzIHCAAQsAMQQ1AAWABg5YsIaAFwAngAgAFpiAFpkgEDMC4xmAEAqgEHZ3dzLXdpesgBCsABAQ&sclient=gws-wiz'
response_aud = requests.get(url_aud, headers=headers)
soup_aud = BeautifulSoup(response_aud.text, 'lxml')
AUD = soup_aud.find('span', attrs={'class': 'DFlfde SwHCTb'}).text
AUD = AUD.replace(',', '.')
AUD = float(AUD)


# Китайский юань
url_cny = 'https://www.google.com/search?q=%D1%8E%D0%B0%D0%BD%D1%8C+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&rlz=1C1SQJL_enRU883RU883&sxsrf=ALeKk00popSBti3x_rai2pd5-ro9JPkODw%3A1624296016517&ei=UMrQYJuLH87XrgTttLDQAg&oq=.fym&gs_lcp=Cgdnd3Mtd2l6EAEYAzIECAAQQzIECAAQQzIHCAAQsQMQQzIHCAAQsQMQCjIECAAQQzIECAAQCjIHCAAQsQMQCjIECAAQQzIECAAQCjIECAAQQzoJCAAQsQMQChABOgUIABCxAzoJCC4QsQMQChABOgIIADoECCMQJzoGCAAQChABOggIABAKEAEQKlD3GljCJ2CBNmgAcAJ4AIABrwSIAYYHkgEFNC41LTGYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=gws-wiz'
response_cny = requests.get(url_cny, headers=headers)
soup_cny = BeautifulSoup(response_cny.text, 'lxml')
CNY = soup_cny.find('span', attrs={'class': 'DFlfde SwHCTb'}).text
CNY = CNY.replace(',', '.')
CNY = float(CNY)
