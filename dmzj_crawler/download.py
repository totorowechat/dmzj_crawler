# -*- coding: utf-8 -*-
"""
    download 
"""
from .utils import decode_packed_codes, mkdir, download_image,get_url_from_cli, \
    config_parser, integrity_check, lack_print

import requests
import bs4
import re
import urllib
import json
import os


class dmzj_crawler(object):
    """
    download manga in dmzj
    """

    def __init__(self, url, config_path='./_config.yml'):
        # print(os.environ.get)
        self.config = config_parser(config_path)
        self.url = url
        self.title = ''
        self.chapters = {}

    def config_check(self):
        pass

    def get_comic_chapters_url(self):
        '''
        get manga's chapter names and urls.
        '''

        resp = requests.get(self.url)
        soup = bs4.BeautifulSoup(resp.text, 'lxml')
        self.title = soup.title.string.split('-')[0]

        # mkdir(self.config['path'] + title)

        comics_lists = soup.find('div', 'cartoon_online_border').find_all('a')

        for part in comics_lists:
            self.chapters[part.string] = part['href']

        print('The number of chapters: ' + str(len(self.chapters)))

    def get_images_s(self):
        '''
        download image synchornize 
        '''
        if (self.config['path'] == None):
            self.config['path'] = './'
        mkdir(self.config['path'] + self.title)

        basedir = self.config['path'] + self.title
        base_url = 'https://manhua.dmzj.com'

        # current chapter
        if self.config['mode'] == 'update':
            chapters = integrity_check(basedir, self.chapters)
            chapters = lack_print(chapters)


        for chapter in chapters:
            manga_page = 0

            resp = requests.get(base_url + self.chapters[chapter])

            # thanks for dev-techmoe https://github.com/dev-techmoe/python-dcdownloader
            # help me with the decode

            # title = re.search(r'<title>.+</title>', resp.text).group()[7:-8].split('-')[0]

            jspacker_string = re.search(r'(eval\(.+\))', resp.text).group()
            jspacker_string = decode_packed_codes(jspacker_string)
            image_list = re.search(r'(\[.+\])', jspacker_string).group()
            image_list = urllib.parse.unquote(image_list).replace('\\', '')
            image_list = json.loads(image_list)
            # # 创建章节目录
            dirname = basedir + '/' + chapter
            mkdir(dirname)

            print('dirname: {}'.format(dirname))

            # download manga
            for image_url in image_list:
                filename = dirname + '/' + str(manga_page) + '.jpg'
                pic_url = 'https:' + '//images.dmzj.com/' + image_url
                # print(pic_url)
                download_image(filename, pic_url)
                # print(basedir + str(manga_page) + 'Pic saved')
                manga_page += 1
