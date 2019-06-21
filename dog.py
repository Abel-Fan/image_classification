import requests
from lxml import etree

def uploadImg(kw):
    url = "http://soso.huitu.com/search?kw=%s"%kw
    filedir = 'dog/dog%s.jpg' if kw=='狗狗' else 'cat/cat%s.jpg'
    res = requests.get(url)

    select = '//*[@id="img-list-outer"]/div[1]/div[1]/div/a/img'

    html = etree.HTML(res.content)
    res = html.xpath('//div[@class="seozone"]/a/img/@src')

    print(res)
    index = 1
    def upload(url):
        nonlocal index
        filename = filedir%index
        with open(filename,'wb') as f:
            data = requests.get(url)
            f.write(data.content)
            index+=1
        print(filename)
    for url in res:
        upload(url)

uploadImg('猫')
