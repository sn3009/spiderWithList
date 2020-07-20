import re
import requests

from urllib import parse
from bs4 import BeautifulSoup

headers={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36',
    'Cookie':'did=web_d5b552ba309049d78a4750bc74369467; didv=1594196485000; clientid=3; client_key=65890b29; userId=1982451497; sid=e0fba17ab79a87c8dedbea39'
}

def craw(url):
    strhtml = requests.get(url, headers = headers);
    soup = BeautifulSoup(strhtml.content, 'html.parser')
    urls = ''
    for x in soup.find_all('a',href = re.compile('/fw/photo/')):
        value = re.findall(r'/fw/photo/[\w\W]*KUAISHOU', str(x))[0]
        #print(value.replace('&amp;','&'))
        urls += "https://c.kuaishou.com" + value.replace('&amp;','&') + ','
    return urls[0:-1]


def crawWithHtml(htmlFile):
    content = '';
    with open(htmlFile, 'r') as f:
        content = f.read()
    soup = BeautifulSoup(content, 'html.parser')
    urls = ''
    for x in soup.find_all('a',href = re.compile('/fw/photo/')):
        value = re.findall(r'href=\"(.+?)\"', str(x))[0]
        value = value.replace('href=\"', '')
        value = value.replace('\"', '')
        #print(value.replace('&amp;','&'))
        urls += "https://c.kuaishou.com" + value.replace('&amp;','&') + ','
    return urls[0:-1]

#craw("https://c.kuaishou.com/fw/user/liyifei88888?fid=1779600637&cc=share_copylink&followRefer=151&shareMethod=TOKEN&kpn=KUAISHOU&subBiz=PROFILE&shareId=209368522466&shareToken=X-3elzICBc5GX1w7_A&shareResourceType=PROFILE_OTHER&shareMode=APP&appType=21&shareObjectId=19420584&shareUrlOpened=0")