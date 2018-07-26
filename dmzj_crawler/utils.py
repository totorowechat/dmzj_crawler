from yaml import load, dump
from zipfile import ZipFile

import re
import os
import requests
import json

headers = {'referer': 'https://manhua.dmzj.com'}


def mkdir(path):
    '''
    Prevent the existence of directories
    '''
    if not os.path.exists(path):
        os.mkdir(path)


def decode_packed_codes(code):
    '''
    decode the obfs code embed in html page
    '''

    def encode_base_n(num, n, table=None):
        FULL_TABLE = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if not table:
            table = FULL_TABLE[:n]

        if n > len(table):
            raise ValueError(
                'base %d exceeds table length %d' % (n, len(table)))

        if num == 0:
            return table[0]

        ret = ''
        while num:
            ret = table[num % n] + ret
            num = num // n
        return ret

    pattern = r"}\('(.+)',(\d+),(\d+),'([^']+)'\.split\('\|'\)"
    mobj = re.search(pattern, code)
    obfucasted_code, base, count, symbols = mobj.groups()
    base = int(base)
    count = int(count)
    symbols = symbols.split('|')
    symbol_table = {}

    while count:
        count -= 1
        base_n_count = encode_base_n(count, base)
        symbol_table[base_n_count] = symbols[count] or base_n_count

    return re.sub(r'\b(\w+)\b', lambda mobj: symbol_table[mobj.group(0)],
                  obfucasted_code)


def get_url_from_cli():
    '''
    get manga's location
    '''
    print()
    url = None
    while not url:

        # todo - check url validation
        url = input('Index location of target comic: ')
    print()
    return url


def zipPack(save_path, comic_path):
    '''
    to do:
    use the zipfile lib which build in the python lib
    '''
    files = [f for f in os.listdir(comic_path)]

    for f in files:
        print('{} start zipping'.format(f))
        query = '7z a "{}/{}.zip" "{}/{}"'.format(save_path, f, comic_path, f)
        os.system(query)
        # print(query)


def list_dir(path):
    files = [f for f in os.listdir(path)]
    for f in files:
        print(f)


def download_image(filename, url):
    '''
    通过requests库
    将抓取到的图片保存到本地
    '''
    # could add async here
    # add referer
    content = requests.get(url, headers=headers).content
    # content = requests.get(url).content
    with open(filename, 'wb') as f:
        f.write(content)


def config_parser(path):
    try:
        with open(path, 'r') as config:
            return (load(config))
    except:
        print("config file not exist")


def zip():
    pass


def integrity_check(path, chapters):
    exist_chapters = os.listdir(path)
    need_download = []
    for item in chapters:
        if item not in exist_chapters:
            need_download.append(item)

    return need_download


def lack_print(chapters):
    if not chapters:
        print("You have download all the chapters")
        return chapters
    else:
        print('Chapters Downloaded: ' +
              json.dumps(chapters, ensure_ascii=False))
        string = '''
            Please in the following format
            ["apple", "banana", "cherry"]
            !!! default means all !!!
            !!! you can just copy and paste what had print above !!!
            '''
        print(string)
        need_download = input('Which chapters you wanna download:')
        if need_download == '':
            need_download = chapters
        else:
            need_download = need_download.replace("'", '"')
            need_download = json.loads(need_download)

            while type(need_download) != type([]):
                print('Your input is wrong! Please input again.')
                need_download = input('Which chapters you wanna download:')
                if need_download == '':
                    need_download = chapters
                else:
                    need_download = need_download.replace("'", '"')
                    need_download = json.loads(need_download)

        return need_download


if __name__ == '__main__':
    '''
    for test
    '''
    dic = {'第一话': 'https://manhua.dmzj.com/dmpldrxj/19059.shtml'}

    print(len(dic))

    integrity_check('/home/lingao/Pictures/五等分的花嫁', dic)
    # exist_list = os.listdir('/home/lingao/Pictures/五等分的花嫁')
    # # s = "['123']"
    # print(type(exist_list), exist_list)
    # exist_list = exist_list.replace("'",'"')

    # # list = json.loads()
    # exist_list = json.loads(exist_list)
    # print(type(exist_list), exist_list)
    # # for i in list:
    # #     print(i)
