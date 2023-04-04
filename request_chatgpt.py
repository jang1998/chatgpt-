import requests
from bs4 import BeautifulSoup
import base64

url = "https://fofa.info/result?qbase64=dGl0bGU9IkNoYXRHUFQgV2ViIg%3D%3D"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# 获取所有class为"hsxa-host"的字符串
hsxa_host_list = []
for item in soup.select(".hsxa-host"):
    hsxa_host_list.append(item.text.strip())

print(hsxa_host_list)
