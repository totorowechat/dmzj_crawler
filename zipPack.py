import os

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
def main():

    comic_path = get_url_from_cli() 
    save_path = comic_path + '_'
    zipPack(save_path, comic_path)
    # list_dir(comic_path)
if __name__ == '__main__':
    main()