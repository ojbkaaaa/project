import requests
from bs4 import BeautifulSoup 

#首先我们写好抓取网页的函数
def get_html(url):
	try:
		r = requests.get(url,timeout=30)
		r.raise_for_status()
		r.encodeing = r.apparent_endconding
		return r.text
	except:
		return 'error'
