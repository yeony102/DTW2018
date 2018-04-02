import requests
from bs4 import BeautifulSoup
import sys

#import random

def get_horoscope(s):

	signs = ["ARIES", "TAURUS", "GEMINI", "CANCER", "LEO", "VIRGO", "LIBRA", "SCORPIO", "SAGITTARIUS", "CAPRICORN", "AQUARIUS", "PISCES"]

	sign = signs.index(s) + 1

	url = 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=' + str(sign)
	# print url

	# html = requests.get('https://www.horoscope.com/us/horoscopes/career/horoscope-career-daily-today.aspx?sign=9').text
	html = requests.get(url).text
	soup = BeautifulSoup(html, 'html.parser')
	f = soup.select('.horoscope-content p')[0].text
	return f

# ipt = sys.argv[1].upper()
# result = get_horoscope(ipt)
# print result
# fortune = get_horoscope()
# print fortune