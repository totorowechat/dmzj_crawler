import os

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
    comic_path = './黑社会的超能力女儿'
    save_path = './test'
    zipPack(save_path, comic_path)
    # list_dir(comic_path)
if __name__ == '__main__':
    main()