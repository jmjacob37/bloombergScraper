import requests
from bs4 import BeautifulSoup

URL = 'https://www.bloomberg.com/profile/company/MSFT:US'
from fake_useragent import UserAgent
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
ua=UserAgent(verify_ssl=False)
hdr = {'User-Agent': ua.random,
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}
source = requests.get(URL,headers=hdr)

soup = BeautifulSoup(source.content, features="html.parser")
# print(soup)
company_name = soup.find('h1', class_= 'companyName__9bd88132').text

company_description = soup.find('div', class_ = 'description__ce057c5c').text

company_sector = soup.find('div', class_ = 'infoTableItemValue__e188b0cb').text

company_industry = soup.find('div', class_= 'infoTableItemValue__e188b0cb').text

print('Company Name: '+company_name)
print()
print('Company description: '+company_description)
print()
print('Company sector: '+company_sector)