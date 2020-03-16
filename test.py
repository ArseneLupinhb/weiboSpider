from urllib.request import urlopen
import requests
from lxml import etree
from requests.adapters import HTTPAdapter
from tqdm import tqdm
from bs4 import BeautifulSoup

def get_html_text(url):
	try:
		r = requests.get(url, timeout=30)
		r.raise_for_status()
		r.encoding('utf-8')
		return r.text
	except:
		return ""

url = r'https://weibo.cn/5571549493/follow'

content =  get_html_text(url)
print(content)

r = requests.get(url, timeout=30)
content = r.text