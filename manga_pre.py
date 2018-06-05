import os
import requests
from selenium import webdriver
headers = {
    'referer': 'https://manhua.dmzj.com'
}

def mkdir(path):
    '''
    防止目录存在
    '''
    if not os.path.exists(path):
        os.mkdir(path)


def SavePic(filename, url):
    '''
    通过requests库
    将抓取到的图片保存到本地
    '''
    # add referer
    content = requests.get(url, headers = headers).content
    # content = requests.get(url).content
    with open(filename, 'wb') as f:
        f.write(content)

def SavePic_sel(url):
    '''
    通过selenium download manga
    '''
    browser = webdriver.Chrome()
    browser.get(url)
    browser.implicitly_wait(3)

    print(browser.title.split('-')[0])

    
    print(pic_url)
    pageNum = len(browser.find_elements_by_tag_name('option'))

    browser.quit()

def main():
    # SavePic_sel('https://manhua.dmzj.com/heishihuidcnlnr/15180.shtml')
    SavePic('test.jpg', r'https://images.dmzj.com/h/%E9%BB%91%E7%A4%BE%E4%BC%9A%E7%9A%84%E8%B6%85%E8%83%BD%E5%8A%9B%E5%A5%B3%E5%84%BF/%E7%AC%AC01%E8%AF%9D/015.jpg')

if __name__ == '__main__':
    main()