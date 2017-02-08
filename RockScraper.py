from lxml import html
import requests
import urllib.request
import httplib2
import string

#
#Requires lxml, requests, and httplib2 (pip install ...)
#

# This version written with consideration for image pages only

#Helper functions
def noPunctuation(str):
	trans = str.maketrans('','',string.punctuation)
	return str.translate(trans)

startPage = int(input('start page: '))
endPage = int(input('end page: '))
imgPath = '/users/ben/pictures/rock/'#input('image path: ')

print('\n')

h = httplib2.Http()

for pageNumber in range(startPage, endPage+1):
	
	#Check if the page exists
	resp = h.request('http://www.rockefeller100.org/items/show/'+str(pageNumber), 'HEAD')
	if int(resp[0]['status']) == 200:
		
		#Metadata collection
		fields = {'tags':None, 'title':None, 'description':None, 'creator':None, 'source':None, 'date':None, 'rights':None, 'format':None, 'language':None, 'type':None, 'identifier':None, 'spatial_coverage':None}

		page = requests.get('http://www.rockefeller100.org/items/show/'+str(pageNumber))
		tree = html.fromstring(page.content)

		fields['tags'] = tree.xpath('//div[@id="item-metadata"]/dl/dd/a[@reg="tag"]/text()')
		fields['title'] = tree.xpath('//div[@id="item-metadata"]/dl/dd[@class="metadata-definition metadata-Title"]/text()')
		fields['description'] = tree.xpath('//div[@id="item-metadata"]/dl/dd[@class="metadata-definition metadata-Description"]/text()')
		fields['creator'] = tree.xpath('//div[@id="item-metadata"]/dl/dd[@class="metadata-definition metadata-Creator"]/text()')
		fields['source'] = tree.xpath('//div[@id="item-metadata"]/dl/dd[@class="metadata-definition metadata-Source"]/text()')
		fields['date'] = tree.xpath('//div[@id="item-metadata"]/dl/dd[@class="metadata-definition metadata-Date"]/text()')
		fields['rights'] = tree.xpath('//div[@id="item-metadata"]/dl/dd[@class="metadata-definition metadata-Rights"]/text()')
		fields['format'] = tree.xpath('//div[@id="item-metadata"]/dl/dd[@class="metadata-definition metadata-Format"]/text()')
		fields['language'] = tree.xpath('//div[@id="item-metadata"]/dl/dd[@class="metadata-definition metadata-Language"]/text()')
		fields['type'] = tree.xpath('//div[@id="item-metadata"]/dl/dd[@class="metadata-definition metadata-Type"]/text()')
		fields['identifier'] = tree.xpath('//div[@id="item-metadata"]/dl/dd[@class="metadata-definition metadata-Identifier"]/text()')
		fields['spatial_coverage'] = tree.xpath('//div[@id="item-metadata"]/dl/dd[@class="metadata-definition metadata-Spatial Coverage"]/text()')
		
		#Metadata formatting
		for key in fields:
			fields[key] = str(fields[key]).strip(" ] [ ' ")
			fields[key] = str(fields[key]).replace("'","")
			fields[key] = str(fields[key]).replace("\\n","")
			while "  " in str(fields[key]):
				fields[key] = str(fields[key]).replace("  "," ")
		
		#Determine file name for large image
		lgImgFileName = "".join((noPunctuation(str(fields['identifier']+fields['title']))+'.jpg').split())
		
		#Large image collection
		lgImgURL = str(tree.xpath('//div[@class="item-file image-jpeg"]/a/@href')).strip(" [ ] ' ")
		urllib.request.urlretrieve(lgImgURL, imgPath+lgImgFileName)
		print('write: '+lgImgFileName)
		
		#Determine file name for thumbnail
		smImgFileName = "".join((noPunctuation(str(fields['identifier']+fields['title']))+'-thumb.jpg').split())
		
		#Thumbnail collection
		smImgURL = lgImgURL.replace('original','square_thumbnails')
		urllib.request.urlretrieve(smImgURL, imgPath+smImgFileName)
		print('write: '+smImgFileName)
		
	
