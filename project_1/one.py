import requests
from bs4 import BeautifulSoup 

#首先我们写好抓取网页的函数
def get_html(url):
	try:
		r = requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding = 'utf-8'
		print('one')
		return r.text
	except:
		return 'error'

def get_content(url):
	comments = []
	html = get_html(url)
	soup = BeautifulSoup(html,'lxml')
	litags = soup.find_all('li',attrs={'class':' j_thread_list clearfix'})
	print(litags)
	for li in litags:
		comment = {}
		try:
			comment['title']= li.find('a',attrs={'class':'j_th_tit'}).text.strip()
			comments.append(comment)
#			print(commit['title'])
		except:
			print('出了问题')
	return comments

def Out2File(dict):
	with open('/project/TTBT.txt','a+') as f:
		for comment in dict:
			f.write('标题：{} \n'.format(comment['title']))
		print('当前页面抓取完毕')

def main(base_url,deep):
	url_list = []
	for i in range(0,deep):
		url_list.append(base_url +'&pn=' +str(50 * i))
	print('所有的网页已经下载到本地，开始筛选数据')
	for url in url_list:
		content = get_content(url)
		Out2File(content)
	print('所有信息保存完毕')

base_url = 'http://tieba.baidu.com/f?ie=utf-8&kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&fr=search&red_tag=b2202460334'
	
deep = 3

if __name__ == '__main__':
	main(base_url,deep)











