from .__version__ import __version__, __author__, ascii_art
from .download import dmzj_crawler

def show_welcome():
    print(ascii_art)
    print('Downloader version {version}'.format(version=__version__))
    print('Homepage: https://github.com/totorowechat/dmzj_crawler')
    print('Author: ' + __author__)
    print()

def input_manga_url():

    url = None
    while not url:

        # todo - check url validation
        url = input('Index page url of target comic: ')
    print() 
    return url

    



def main():
    show_welcome()
    url = input_manga_url()
    # url = 'https://manhua.dmzj.com/wudengfendehuajia/'
    app = dmzj_crawler(url)
    app.get_comic_chapters_url()
    app.get_images_s()

