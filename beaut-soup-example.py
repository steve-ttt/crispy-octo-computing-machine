#!/usr/bin/python
from BeautifulSoup import BeautifulSoup
import urllib2
import os
import re

site= "http://anon-ib.co/azn/index.html"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(site,headers=hdr)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page)
subdir = 'images'
links = soup.findAll('img', {'class': 'post-image'})

try:
    os.stat(subdir)
except:
    os.mkdir(subdir)

def getLinks():
    """
    just pull the links with this code :
    """
    for x in soup.findAll('img'):
        try:
            dl = "http://anon-ib.co" +str(x['src'])
            fn = str(x['src'])
            print dl
            print fn.split('/')[3]
            reqget = urllib2.Request(dl, headers=hdr)
            imgfile = urllib2.urlopen(reqget)
            output = open(str(subdir) +'/' +str(fn.split('/')[3]),'wb')    
            output.write(imgfile.read()) 
            output.close()
        except urllib2.URLError, e:
            print e


def getImages():
    """
    get the full size images
    """
    for i in soup.findAll('a', href=True):
        try:
            link = i['href']
            if re.match('\\/azn\\/src', str(link)) :
                print(str(link))
                dl = "http://anon-ib.co" +str(link)
                reqget = urllib2.Request(dl, headers=hdr)
                imgfile = urllib2.urlopen(reqget)
                output = open(str(subdir) +'/' +str(link.split('/')[3]),'wb')    
                output.write(imgfile.read()) 
                output.close()
        except urllib2.URLError, e:
            print e


if __name__ == "__main__":
    getImages()
    
