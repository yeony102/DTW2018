import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def get_page(s):
	url = "https://www.urbandictionary.com/"
	response = requests.get(url, params={'page': s}, headers=headers)
	html = response.text
	soup = BeautifulSoup(html, "html.parser")
	titles = soup.select('a.word')

	output = []
	for title in titles:
		clean_title = title.text.strip().encode('utf-8')
		output.append(clean_title)

	return output

start = 655
while start < 656:
	results = get_page(start)
	for r in results:
		print r

	#time.sleep(0.5)	# it is another way to prevent being banned

	start = start + 1


# url = 'https://www.glassdoor.com/Job/new-york-jobs-SRCH_IL.0,8_IC1132348_IP" 2.htm'
# html = requests.get(url, headers=headers).text
# #print html
# soup = BeautifulSoup(html, "html.parser")

# titles = soup.select('a.jobLink')

# for title in titles:
# 	print title.text.strip().encode('utf-8')