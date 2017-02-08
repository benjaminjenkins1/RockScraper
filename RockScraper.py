from lxml import html
import requests
import urllib.request
import httplib2
import string
import json
import os

#
#Requires lxml, requests, and httplib2 (pip install ___)
#

# This version written with consideration for image pages only

#Helper functions
def noPunctuation(str):
  trans = str.maketrans('','',string.punctuation)
  return str.translate(trans)

startPage = int(input('start page: '))
endPage = int(input('end page: '))
path = input('path: ')
if not path.endswith('/'):
  path = path+'/'

print('\n')

h = httplib2.Http()

for pageNumber in range(startPage, endPage+1):
  
  resp = h.request('http://www.rockefeller100.org/items/show/'+str(pageNumber), 'HEAD')
  if int(resp[0]['status']) == 200 :
    
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
    if 'Image' in str(fields['type']):
      fields['identifier'] = tree.xpath('//div[@id="item-metadata"]/dl/dd[@class="metadata-definition metadata-Identifier"]/text()')
      fields['spatial_coverage'] = tree.xpath('//div[@id="item-metadata"]/dl/dd[@class="metadata-definition metadata-Spatial Coverage"]/text()')
      
      #Metadata formatting
      for key in fields:
        fields[key] = str(fields[key]).strip(" ] [ ' ")
        fields[key] = str(fields[key]).replace("'","")
        fields[key] = str(fields[key]).replace("\\n","")
        while "  " in str(fields[key]):
          fields[key] = str(fields[key]).replace("  "," ")
        fields[key] = str(fields[key]).strip()
      
      #Determine file name for large image
      lgImgFileName = "".join((noPunctuation(str(fields['identifier']+fields['title']))+'.jpg').split())
      
      #Determine file name for thumbnail
      smImgFileName = "".join((noPunctuation(str(fields['identifier']+fields['title']))+'-thumb.jpg').split())
      
      #Make clean write path
      writePath = path+str(fields['identifier']+'/')
      while " " in writePath:
        writePath = writePath.replace(" ","")
        
      #Make directory for files
      if not os.path.exists(writePath):
        os.mkdir(writePath)
      
      #Large image collection
      lgImgURL = str(tree.xpath('//div[@class="item-file image-jpeg"]/a/@href')).strip(" [ ] ' ")
      urllib.request.urlretrieve(lgImgURL, (writePath+lgImgFileName))
      print('write: '+lgImgFileName)
      
      #Thumbnail collection
      smImgURL = lgImgURL.replace('original','square_thumbnails')
      urllib.request.urlretrieve(smImgURL, (writePath+smImgFileName))
      print('write: '+smImgFileName)

      #Add file names to metadata
      fields['file_name'] = lgImgFileName
      fields['file_path'] = writePath+lgImgFileName
      fields['thumb_file_name'] = smImgFileName
      fields['thumb_file_path'] = writePath+smImgFileName
      
      #Dump metadata
      with open (writePath+fields['identifier']+'.json', 'w', encoding='utf-8') as f:
        json.dump(fields, f, ensure_ascii=False)
    else: print('page is not of type Image')
  else: print('page '+str(pageNumber)+' does not exist')
    
  
