from lxml import html
import requests
import httplib2

#Scraper for pages on Rockefeller100.org

def getChildren(parent):
  print('<'+parent.tag+'>')
  print(parent.text)
  try:
    children = parent.getchildren()
    for child in children:
      getChildren(child)
  except:
    pass
  print('</'+parent.tag+'>')


#path = input('path: ')
url = input('url: ')

h = httplib2.Http()

while(not url == ''):
  resp = h.request(url, 'HEAD')
  if int(resp[0]['status']) == 200 :
    
    page = requests.get(url)
    tree = html.fromstring(page.content)
    
    content = tree.xpath('//div[@class="content"]')
    for item in content:
      getChildren(item)
    
    #images?
    
    
    url = input('url: ')
  else:
    print('server did not respond with status 200')