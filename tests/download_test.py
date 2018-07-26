from .boot import dmzj_crawler


def download_test():

    url = dmzj_crawler.cli.input_manga_url()
    app = dmzj_crawler.download.dmzj_crawler(url)
    app.get_comic_chapters_url()
    app.get_images_s()


a = input()
if type(a) == type(''):
    print(type(a))
