import requests
import subprocess #commandline
from selenium import webdriver
import os
import time


def download_file(url, local_filename=None):

    #from: https://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py

    if local_filename is None:
        local_filename = url.split('/')[-1]

    if os.path.exists(local_filename):
        return local_filename

    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename


driver = webdriver.Chrome()
driver.get('https://www.pinterest.co.kr/search/pins/?q=chris%20van%20allsburg&rs=typed&term_meta[]=chris%7Ctyped&term_meta[]=van%7Ctyped&term_meta[]=allsburg%7Ctyped')

for x in range(0, 10):
    time.sleep(3)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

images = driver.find_elements_by_css_selector('img')

for i, image in enumerate(images):
	#print image.get_attribute('src')
	url = image.get_attribute('src')
	savedname = 'pinterest/' + str(i) + '.jpg'
	download_file(url, savedname)

subprocess.call(['convert', 'pinterest/*.jpg', '-resize', '300x300', 'chrisvanallsburg.gif'])
