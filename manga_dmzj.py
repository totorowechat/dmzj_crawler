from mange_pre import mkdir, SavePic, SavePic_sel
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_experimental_option("prefs", {
    "profile.managed_default_content_settings.images":2,
})

def get_TOF(index_url):
    '''
    获取漫画的目录中的每一章节的url连接
    并返回一个字典类型k：漫画名 v：章节链接
    '''
    url_list = []

    # 模拟浏览器并打开网页
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(index_url)
    browser.implicitly_wait(3)

    # 找到漫画标题 并创建目录
    title = browser.title.split('-')[0]
    mkdir(title)

    # 找到漫画章节，注意，漫画可能会有多种篇章
    # 例如番外，正文，短片等等
    comics_lists = browser.find_elements_by_class_name('cartoon_online_border')
    # 寻找、正文等
    for part in comics_lists:
        # 找到包裹链接的links
        links = part.find_elements_by_tag_name('a')

        # 找到每个单独的章节链接
        for link in links:
            url_list.append(link.get_attribute('href'))
            

    # 关闭浏览器
    browser.quit()

    Comics = dict(name=title, urls=url_list)

    return Comics


def get_pic(Comics):
    comic_list = Comics['urls']
    basedir = Comics['name']

    browser = webdriver.Chrome(chrome_options=chrome_options)
    for url in comic_list:
        manga_page = 0
        browser.get(url)
        browser.implicitly_wait(3)

        # 创建章节目录
        dirname = basedir + '/' + browser.title.split('-')[0]
        mkdir(dirname)
        print('dirname: {}'.format(dirname))
        # 找到该漫画一共有多少页
        option_tags = browser.find_elements_by_tag_name('option')
        
        # download manga
        for tag in option_tags:
            filename = dirname + '/' + str(manga_page) + '.jpg'
            pic_url = 'https:' + tag.get_attribute('value')
            print(pic_url)
            SavePic(filename, pic_url)
            print('Pic saved')
            manga_page += 1

        # pageNum = len(browser.find_elements_by_tag_name('option'))

        # for i in range(pageNum):
        #     pic_url = browser.find_element_by_id('center_box').find_element_by_tag_name('img').get_attribute('src')
        #     
        #     browser.get(pic_url)
        #     browser.save_screenshot(filename)
        #     print(url + '#@page=' + str(i))
        #     browser.get(url + '#@page=' + str(i+2))
        #     # 
        #     # 点击下一页的按钮，加载下一张图
        #     # nextpage.click()
def main():
    manga_url = 'https://manhua.dmzj.com/heishihuidcnlnr/'
    Comics = get_TOF(manga_url)
    get_pic(Comics)

if __name__ == '__main__':
    main()