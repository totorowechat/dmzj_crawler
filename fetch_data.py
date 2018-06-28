import re
import bs4
import requests
import jsbeautifier.unpackers.packer as packer


def get_comic_chapters_url(index_url):
    '''
    获取漫画的目录中的每一章节的url连接
    并返回一个字典类型k：漫画名 v：章节链接
    '''
    url_list = []
    chapter_lists = []
    # use requests to get the chapters
    rsp = requests.get(index_url)
    soup = bs4.BeautifulSoup(rsp.text, 'lxml')
    # 找到漫画标题 并创建目录
    title =soup.title.string.split('-')[0]
    # fina all urls of chapters 
    comics_lists = soup.find('div', 'cartoon_online_border').find_all('a')

    for part in comics_lists:
        url_list.append(part['href'])
        chapter_lists.append(part.string)

    print('total chapters: ' + str(len(url_list)))

    Comics = dict(name=title, urls=url_list, title=chapter_lists)
    return Comics

def get_image_info_sync(Comics):
    ''' 
    returm a list of image urls
    '''
    image_urls = []
    for chapter in Comics['urls']:
        # print(chapter)
        rsp = requests.get('https://manhua.dmzj.com' + chapter)

        soup = bs4.BeautifulSoup(rsp.text, 'lxml')
        eval_content = get_eval_content(soup)
        # print(eval_content)
        image_urls.append(decode(eval_content))

    return image_urls
def get_eval_content(soup):
    '''
    get eval from soup
    '''
    #get content include eval()
    eval_content = re.search('eval(.+)', soup.script.string).group(0)
    return eval_content

def decode(eval_content):
    '''
    decode content in eval() return the list of image urls
    '''
    unpack = packer.unpack(eval_content)
    unpack = unpack.replace("""\\""", '')
    image_urls = re.search('\[.+\]', unpack).group(0)[1:-1]
    image_urls = image_urls.split(',')
    image_urls = [image_url[1:-1] for image_url in image_urls]

    return image_urls
 
if __name__ == '__main__':
    rsp = requests.get('https://manhua.dmzj.com/meikonggegeyuxiongkongmeimeibianchengshi/65925.shtml#@page=1/')
    soup = bs4.BeautifulSoup(rsp.text, 'lxml')

    # content = get_eval_content(soup)
    content = """eval(function(p,a,c,k,e,d){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--){d[e(c)]=k[c]||e(c)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('N I=I=\'["m\\/%0%c%e%a%d%k%0%j%i%0%j%i%h%y%d%0%r%x%a%d%k%0%c%e%0%c%e%0%w%g%u%z%C%0%H%A\\/G%a%b%E%0%B%F%0%o%p%l%f%n%h%s%b%a%t%g%0%q%f%0%b%D\\/1.v","m\\/%0%c%e%a%d%k%0%j%i%0%j%i%h%y%d%0%r%x%a%d%k%0%c%e%0%c%e%0%w%g%u%z%C%0%H%A\\/G%a%b%E%0%B%F%0%o%p%l%f%n%h%s%b%a%t%g%0%q%f%0%b%D\\/2.v","m\\/%0%c%e%a%d%k%0%j%i%0%j%i%h%y%d%0%r%x%a%d%k%0%c%e%0%c%e%0%w%g%u%z%C%0%H%A\\/G%a%b%E%0%B%F%0%o%p%l%f%n%h%s%b%a%t%g%0%q%f%0%b%D\\/3.v","m\\/%0%c%e%a%d%k%0%j%i%0%j%i%h%y%d%0%r%x%a%d%k%0%c%e%0%c%e%0%w%g%u%z%C%0%H%A\\/G%a%b%E%0%B%F%0%o%p%l%f%n%h%s%b%a%t%g%0%q%f%0%b%D\\/4.v","m\\/%0%c%e%a%d%k%0%j%i%0%j%i%h%y%d%0%r%x%a%d%k%0%c%e%0%c%e%0%w%g%u%z%C%0%H%A\\/G%a%b%E%0%B%F%0%o%p%l%f%n%h%s%b%a%t%g%0%q%f%0%b%D\\/5.v","m\\/%0%c%e%a%d%k%0%j%i%0%j%i%h%y%d%0%r%x%a%d%k%0%c%e%0%c%e%0%w%g%u%z%C%0%H%A\\/G%a%b%E%0%B%F%0%o%p%l%f%n%h%s%b%a%t%g%0%q%f%0%b%D\\/6.v","m\\/%0%c%e%a%d%k%0%j%i%0%j%i%h%y%d%0%r%x%a%d%k%0%c%e%0%c%e%0%w%g%u%z%C%0%H%A\\/G%a%b%E%0%B%F%0%o%p%l%f%n%h%s%b%a%t%g%0%q%f%0%b%D\\/7.v","m\\/%0%c%e%a%d%k%0%j%i%0%j%i%h%y%d%0%r%x%a%d%k%0%c%e%0%c%e%0%w%g%u%z%C%0%H%A\\/G%a%b%E%0%B%F%0%o%p%l%f%n%h%s%b%a%t%g%0%q%f%0%b%D\\/8.v","m\\/%0%c%e%a%d%k%0%j%i%0%j%i%h%y%d%0%r%x%a%d%k%0%c%e%0%c%e%0%w%g%u%z%C%0%H%A\\/G%a%b%E%0%B%F%0%o%p%l%f%n%h%s%b%a%t%g%0%q%f%0%b%D\\/9.v","m\\/%0%c%e%a%d%k%0%j%i%0%j%i%h%y%d%0%r%x%a%d%k%0%c%e%0%c%e%0%w%g%u%z%C%0%H%A\\/G%a%b%E%0%B%F%0%o%p%l%f%n%h%s%b%a%t%g%0%q%f%0%b%D\\/M.v","m\\/%0%c%e%a%d%k%0%j%i%0%j%i%h%y%d%0%r%x%a%d%k%0%c%e%0%c%e%0%w%g%u%z%C%0%H%A\\/G%a%b%E%0%B%F%0%o%p%l%f%n%h%s%b%a%t%g%0%q%f%0%b%D\\/P.v","m\\/%0%c%e%a%d%k%0%j%i%0%j%i%h%y%d%0%r%x%a%d%k%0%c%e%0%c%e%0%w%g%u%z%C%0%H%A\\/G%a%b%E%0%B%F%0%o%p%l%f%n%h%s%b%a%t%g%0%q%f%0%b%D\\/L.v","m\\/%0%c%e%a%d%k%0%j%i%0%j%i%h%y%d%0%r%x%a%d%k%0%c%e%0%c%e%0%w%g%u%z%C%0%H%A\\/G%a%b%E%0%B%F%0%o%p%l%f%n%h%s%b%a%t%g%0%q%f%0%b%D\\/J.v","m\\/%0%c%e%a%d%k%0%j%i%0%j%i%h%y%d%0%r%x%a%d%k%0%c%e%0%c%e%0%w%g%u%z%C%0%H%A\\/G%a%b%E%0%B%F%0%o%p%l%f%n%h%s%b%a%t%g%0%q%f%0%b%D\\/K.v","m\\/%0%c%e%a%d%k%0%j%i%0%j%i%h%y%d%0%r%x%a%d%k%0%c%e%0%c%e%0%w%g%u%z%C%0%H%A\\/G%a%b%E%0%B%F%0%o%p%l%f%n%h%s%b%a%t%g%0%q%f%0%b%D\\/O.v","m\\/%0%c%e%a%d%k%0%j%i%0%j%i%h%y%d%0%r%x%a%d%k%0%c%e%0%c%e%0%w%g%u%z%C%0%H%A\\/G%a%b%E%0%B%F%0%o%p%l%f%n%h%s%b%a%t%g%0%q%f%0%b%D\\/S.v","m\\/%0%c%e%a%d%k%0%j%i%0%j%i%h%y%d%0%r%x%a%d%k%0%c%e%0%c%e%0%w%g%u%z%C%0%H%A\\/G%a%b%E%0%B%F%0%o%p%l%f%n%h%s%b%a%t%g%0%q%f%0%b%D\\/V.v","m\\/%0%c%e%a%d%k%0%j%i%0%j%i%h%y%d%0%r%x%a%d%k%0%c%e%0%c%e%0%w%g%u%z%C%0%H%A\\/G%a%b%E%0%B%F%0%o%p%l%f%n%h%s%b%a%t%g%0%q%f%0%b%D\\/X.v","m\\/%0%c%e%a%d%k%0%j%i%0%j%i%h%y%d%0%r%x%a%d%k%0%c%e%0%c%e%0%w%g%u%z%C%0%H%A\\/G%a%b%E%0%B%F%0%o%p%l%f%n%h%s%b%a%t%g%0%q%f%0%b%D\\/W.v","m\\/%0%c%e%a%d%k%0%j%i%0%j%i%h%y%d%0%r%x%a%d%k%0%c%e%0%c%e%0%w%g%u%z%C%0%H%A\\/G%a%b%E%0%B%F%0%o%p%l%f%n%h%s%b%a%t%g%0%q%f%0%b%D\\/%0%o%p%l%f%n%h%s%b%a%t%g%0%q%f%0%b%T.v","m\\/%0%c%e%a%d%k%0%j%i%0%j%i%h%y%d%0%r%x%a%d%k%0%c%e%0%c%e%0%w%g%u%z%C%0%H%A\\/G%a%b%E%0%B%F%0%o%p%l%f%n%h%s%b%a%t%g%0%q%f%0%b%D\\/%l%U%r%0%R%Q.v"]\';',60,60,'E5||||||||||E6|9C|A6|8E|B9|BA|98|E4|A5|93|A7|E7||BF|89|8D|9F|85|BD|88|E8|jpg|8F|84|B8|AF|9E|8A|9A|B0|A8|9BX|02|AE|pages|13|14|12|10|var|15|11|ABACG|A3|16|B03|BB|17|0099|18'.split('|'),0,{}))"""
    # # s = """eval(function(p,a,c,k,e,d){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--){d[e(c)]=k[c]||e(c)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('V H=H=\'["m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/1.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/3.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/4.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/5.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/6.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/7.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/8.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/9.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/10.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/11.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/12.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/13.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/14.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/15.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/16.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/17.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/18.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/19.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/Q.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/P.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/S.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/T.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/U.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/M.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/J.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/I.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/K.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/L.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/O.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/N.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/R.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/1b.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/1g.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/1h.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/1i.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/1k.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/1j.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/1f.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/1d.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/W.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/Y.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/X.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%1e.v","m\\/%0%c%d%2%b%h%0%j%i%0%j%i%g%w%b%0%r%y%2%b%h%0%c%d%0%c%d%0%t%f%u%x%C%0%z%F\\/G%2%a%D%0%A%B%0%n%l%k%e%o%g%q%a%2%p%f%0%s%e%0%a%E\\/%k%1a%r%0%1c%Z.v"]\';',62,83,'E5||E6||||||||9C|8E|A6|B9|BA|98|E4|A7|A5|93|E7|8D||89|BF|88|BD|85|9F|8F|E8|jpg|B8|AF|84|AE|8A|9BX|9A|A8|B0|9E|01|pages|27|26|28|29|25|31|30|21|20|32|22|23|24|var|41|0099|42|ABACG|||||||||||BB|33|A3|40|B03|39|34|35|36|38|37'.split('|'),0,{}))"""
    print(content)
    unpack = packer.unpack(content)
    # decode_content = decode(content)
    print(unpack)
   
    # Comics = get_comic_chapters_url('https://manhua.dmzj.com/wudengfendehuajia/')
    # print(Comics)
    # image_urls = get_image_info_sync(Comics)
    # print(image_urls)
