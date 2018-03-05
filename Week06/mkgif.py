
import requests
import subprocess #commandline
import os
from bs4 import BeautifulSoup
import sys

def download_file(url, local_filename=None):

    #from: https://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py

    if local_filename is None:
        local_filename = url.split('/')[-1]

    if os.path.exists(local_filename):
        return local_filename

    if not url.startswith('http'):
        url = 'http:' + url

    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename


def get_images(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.select('img')
    for i, image in enumerate(images):
        img_url = image.get('src')
        savedname = 'frames/' + str(i) + '.jpg'
        try: 
            filename = download_file(img_url, savedname)
        except Exception as e:
            print e
            continue
    subprocess.call(['convert', 'frames/*.jpg', '-resize', '300x300', 'coolgif.gif'])

#get_images("http://foxnews.com")
#get_images(sys.argv[1])
get_images('https://www.pinterest.co.kr/search/pins/?q=chris%20van%20allsburg&rs=typed&term_meta[]=chris%7Ctyped&term_meta[]=van%7Ctyped&term_meta[]=allsburg%7Ctyped')