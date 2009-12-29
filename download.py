import os, time, urllib, urllib2
from xml.dom.minidom import parse, parseString

flickr_key = '1cc3376fd68b814c4de14baa7e9a3f11'
photoset_id = 72157622183512186
api = 'http://api.flickr.com/services/rest/?method=flickr.photosets.getPhotos&api_key=%s&photoset_id=%s' % (flickr_key, photoset_id)
path = "%s" % photoset_id

def getapi():
	
	if not os.path.isdir(path):
		print 'creating new directory'
		
	xml = parseString(urllib2.urlopen(api).read())
	photos = xml.getElementsByTagName('photo')
	
	j = 1
	
	for dom in photos:
		
		url = 'http://farm%s.static.flickr.com/%s/%s_%s_b.jpg' % (dom.attributes['farm'].value, dom.attributes['server'].value, dom.attributes['id'].value, dom.attributes['secret'].value)
		local = '%s/%.4d_%s_%s_b.jpg' % (path, j, dom.attributes['id'].value, dom.attributes['secret'].value)
		
		if os.path.isfile(local) == False:
			image = urllib.URLopener().retrieve(url, local)
			print 'downloaded', local
			time.sleep(0.5)
		else:
			print 'exists    ', local
		
		j += 1
		
if __name__ == "__main__":
	getapi()
