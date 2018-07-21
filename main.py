from manga_pre import mkdir, SavePic, SavePic_sel,get_url_from_cli
from utils import decode_packed_codes
import version
import requests
import bs4
import re
import urllib
import json



def get_comic_chapters_url(index_url, cpath='./'):
    '''
    获取漫画的目录中的每一章节的url连接
    并返回一个字典类型k：漫画名 v：章节链接
    '''
    url_list = []

    # open manga page

    rsp = requests.get(index_url)
    soup = bs4.BeautifulSoup(rsp.text, 'lxml')
    # 找到漫画标题 并创建目录

    title = soup.title.string.split('-')[0]
    
    mkdir(cpath + title)

    comics_lists = soup.find('div', 'cartoon_online_border').find_all('a')

    # 寻找、正文等
    for part in comics_lists:
        url_list.append(part['href'])

    print('total chapters: ' + str(len(url_list)))

    Comics = dict(name=title, urls=url_list)
    return Comics


def get_pic_sync(Comics, cpath='./'):
    '''
    get a dict Comics includes all links which link to every chapters
    
    '''
    comic_list = Comics['urls']
    basedir = Comics['name']

    base_url = 'https://manhua.dmzj.com'
    for url in comic_list:
        manga_page = 0


        rsp =requests.get(base_url + url)


        # thanks for dev-techmoe https://github.com/dev-techmoe/python-dcdownloader 
        # inspire me with the decode
        title = re.search(r'<title>.+</title>', rsp.text).group()[7:-8].split('-')[0]

        jspacker_string = re.search(r'(eval\(.+\))', rsp.text).group()
        jspacker_string = decode_packed_codes(jspacker_string)
        image_list = re.search(r'(\[.+\])', jspacker_string).group()
        image_list = urllib.parse.unquote(image_list).replace('\\', '')
        image_list = json.loads(image_list)
        # # 创建章节目录
        dirname = cpath + basedir + '/' + title
        mkdir(dirname)
        print('dirname: {}'.format(dirname))

        # download manga
        for image_url in image_list:
            filename = dirname + '/' + str(manga_page) + '.jpg'
            pic_url = 'https:' + '//images.dmzj.com/' + image_url
            print(pic_url)
            SavePic(filename, pic_url)
            print(basedir + str(manga_page) + 'Pic saved')
            manga_page += 1


def main():
    version.show_welcome()
    manga_url = get_url_from_cli()
    Comics = get_comic_chapters_url(manga_url, '~/Pictures/')
    get_pic_sync(Comics,'~/Pictures/')

if __name__ == '__main__':
    main()