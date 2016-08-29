from BeautifulSoup import BeautifulSoup
import urllib2

site= "http://anon-ib.co/azn/index.html"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(site,headers=hdr)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page)

links = soup.findAll('img', {'class': 'post-image'})


for x in soup.findAll('img'):
    try:
        dl = "http://anon-ib.co" +str(x['src'])
        fn = str(x['src'])
        print dl
        print fn.split('/')[3]
        reqget = urllib2.Request(dl, headers=hdr)
        imgfile = urllib2.urlopen(reqget)
        output = open(fn.split('/')[3],'wb')    
        output.write(imgfile.read()) 
        output.close()
    except urllib2.URLError, e:
        print e
