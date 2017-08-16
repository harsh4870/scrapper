from bs4 import BeautifulSoup
import requests
import os,sys
import urllib
import re

#Enter your search URL here (Remove the placeholder first). Get this from just searching like normal on 4walled.cc and copying the URL.
url = "http://www.wallpaperswide.com"
#Enter your download path here (This will download to a new folder, wallpapers, in the directory this script is ran from)
path = "girls//"
#Pages of wallpapers to download (30 per page)
limit = 30

resultsurl = url.replace("/sarch.php", "/result.php") + "/girls-desktop-wallpapers/page/"
if not os.path.exists(path): os.makedirs(path)
print resultsurl


for i in range(0, limit):
    pages = i * 1
    imagepageurl = resultsurl + str(pages)
    print imagepageurl
    r = requests.get(imagepageurl)
    print r
    html = r.text
    
    soup = BeautifulSoup(html)    
    
    for tag in soup.find_all("img"):
        thumburl = tag['src']
        #print thumburl
        realurl1 = thumburl.replace("/thumbs", "/download")
        print realurl1
        realurl = realurl1.replace("-t1", "-wallpaper-1920x1080")
        print realurl
        
        try:
            r = requests.get(realurl)
            r.raise_for_status()            
        except:
            realurl = realurl.replace(".jpg")
            
        
        fr = requests.get(realurl)
        #filepath = path + realurl
        #with open(filepath, 'wb') as writer:
            #writer.write(fr.content)
        #fr.close()
        #print "Downloading to " + filepath
        
        imageFile = open(os.path.join('girls', os.path.basename(realurl)), 'ab')
        for chunk in fr.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
