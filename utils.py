import os

def mkdir(path):
    '''
    防止目录存在
    '''
    if not os.path.exists(path):
        os.mkdir(path)
 
if __name__ == '__main__':
    content = get_eval_content(soup)
    decode_content = decode(content)
    print(decode_content)
