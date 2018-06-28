from manga_pre import mkdir, SavePic, SavePic_sel,get_url_from_cli
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import version
import requests
import bs4
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_experimental_option("prefs", {
    "profile.managed_default_content_settings.images":2,
})


def get_comic_chapters_url(index_url, cpath='./'):
    '''
    获取漫画的目录中的每一章节的url连接
    并返回一个字典类型k：漫画名 v：章节链接
    '''
    url_list = []

    # 模拟浏览器并打开网页
    # browser = webdriver.Chrome(chrome_options=chrome_options)
    # browser.get(index_url)
    # browser.implicitly_wait(3)

    # use requests to get the chapters
    rsp = requests.get(index_url)
    soup = bs4.BeautifulSoup(rsp.text, 'lxml')
    # 找到漫画标题 并创建目录
    
    # title =cpath + browser.title.split('-')[0]
    title =cpath + soup.title.string.split('-')[0]
    
    mkdir(title)

    # 找到漫画章节，注意，漫画可能会有多种篇章
    # 例如番外，正文，短片等等
    # comics_lists = browser.find_elements_by_class_name('cartoon_online_border')

    comics_lists = soup.find('div', 'cartoon_online_border').find_all('a')

    # 寻找、正文等
    for part in comics_lists:
        # # 找到包裹链接的links
        # links = part.find_elements_by_tag_name('a')

        # # 找到每个单独的章节链接
        # for link in links:

        #     url_list.append(link.get_attribute('href'))
        url_list.append(part['href'])

    print('total chapters: ' + str(len(url_list)))

    # # 关闭浏览器
    # browser.quit()
    Comics = dict(name=title, urls=url_list)
    return Comics


def get_pic_sync(Comics, cpath='./'):
    '''
    get a dict Comics includes all links which link to every chapters
    
    '''
    comic_list = Comics['urls']
    basedir = Comics['name']

    browser = webdriver.Chrome(chrome_options=chrome_options)
    for url in comic_list:
        manga_page = 0
        browser.get(url)
        browser.implicitly_wait(3)

        # 找到该漫画一共有多少页
        option_tags = browser.find_elements_by_tag_name('option')
        
        # 创建章节目录
        dirname = cpath + basedir + '/' + browser.title.split('-')[0]
        mkdir(dirname)
        print('dirname: {}'.format(dirname))

        # download manga
        for tag in option_tags:
            filename = dirname + '/' + str(manga_page) + '.jpg'
            pic_url = 'https:' + tag.get_attribute('value')
            print(pic_url)
            SavePic(filename, pic_url)
            print('Pic saved')
            manga_page += 1


def main():
    version.show_welcome()
    # manga_url = get_url_from_cli()
    manga_url = 'https://manhua.dmzj.com/wudengfendehuajia'
    Comics = get_comic_chapters_url(manga_url)
    # get_pic_sync(Comics)

if __name__ == '__main__':
    main()