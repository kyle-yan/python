import random
import urllib.request

def download_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)  #把来自url的图片存储为full_name
download_image('http://www.baidu.com/img/baidu_jgylogo3.gif')
