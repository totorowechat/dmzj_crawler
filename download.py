import os
import requests
from utils import mkdir

headers = {
    'referer': 'https://manhua.dmzj.com'
}

def download_sync(image_urls, dirname):
    mkdir(dirname)
    for image_url in image_urls:
        
def SavePic(filename, url):
    '''
    通过requests库
    将抓取到的图片保存到本地
    '''
    # could add async here 
    # add referer
    content = requests.get(url, headers = headers).content
    # content = requests.get(url).content
    with open(filename, 'wb') as f:
        f.write(content)

def main():
    # SavePic_sel('https://manhua.dmzj.com/heishihuidcnlnr/15180.shtml')
    SavePic('1.jpg', 'https://images.dmzj.com/m/%E5%A6%B9%E6%8E%A7%E5%93%A5%E5%93%A5%E4%B8%8E%E5%85%84%E6%8E%A7%E5%A6%B9%E5%A6%B9%E5%8F%98%E8%AF%9A%E5%AE%9E/01%E6%9C%A8%E5%8A%9BX%E5%89%8D%E7%BA%BF%E4%BD%9C%E6%88%98%E5%9F%BA%E5%9C%B0/%E5%89%8D%E7%BA%BF%E4%BD%9C%E6%88%98%E5%9F%BA%E5%9C%B03.jpg')
    SavePic('2.jpg', 'https://images.dmzj.com/m/%E5%A6%B9%E6%8E%A7%E5%93%A5%E5%93%A5%E4%B8%8E%E5%85%84%E6%8E%A7%E5%A6%B9%E5%A6%B9%E5%8F%98%E8%AF%9A%E5%AE%9E/01%E6%9C%A8%E5%8A%9BX%E5%89%8D%E7%BA%BF%E4%BD%9C%E6%88%98%E5%9F%BA%E5%9C%B0/%E7%BB%85%E5%A3%ABACG.jpg')

if __name__ == '__main__':
    main()