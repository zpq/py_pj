# print("hello!");
import sys
sys.path.append("..lib")
import re
import urllib

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getImg(html):
	reg = r'src="(.*?\.jpg)"'
	imreg = re.compile(reg)
	imglist = re.findall(imreg,html)
	x = 0
	for imgurl in imglist:
		urllib.urlretrieve(imgurl,'%s.jpg' % x)
		x+=1

html = getHtml("http://www.qq.com")
print getImg(html)