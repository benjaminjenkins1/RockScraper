from lxml import html
from copy import deepcopy
import requests
import urllib.request
import httplib2
import string
import json
import os
import random
from splinter import Browser
import pyperclip

#Helper functions
def noPunctuation(str):
  trans = str.maketrans('','',string.punctuation)
  return str.translate(trans)

url = str(input('url: '))

h = httplib2.Http()

resp = h.request(url, 'HEAD')

if int(resp[0]['status']) == 200:
  page = requests.get(url)
  tree = html.fromstring(page.content)
  
  #first, grab the images with unique names - store in imagenames list
  images = tree.xpath('//div[@class="sidebar_post"]//img')
  imagenames = []
  for image in images:
    name = random.randint(1000000000,9999999999)
    imagenames.append(name)
    urllib.request.urlretrieve(image.get('src'), "c:\\Users\\maristuser\\Downloads\\" + str(name) + ".jpg")
  
  #then, grab the title, creator, and date - store in metadata list, a list of dictionaries
  metadataformat = {'title': '', 'creator':'', 'date':''}
  metadata = []
  titles = tree.xpath('//div[@class="sidbar_post_text_title"]')
  creators = tree.xpath('//div[@class="sidebar_post_text_creator"]')
  dates = tree.xpath('//div[@class="sidebar_post_text_date"]')
  for i in range(0, len(titles)):
    data = deepcopy(metadataformat)
    if titles[i].text:
      data['title'] = titles[i].text
    if creators[i].text:
      data['creator'] = creators[i].text
    if dates[i].text:
      data['date'] = dates[i].text
    metadata.append(data)
    
print('upload the images before continuing')
input('press enter...')
    
with Browser("chrome") as browser:
  url = 'https://rockefeller.geminiodyssey.org/web/guest/login'
  browser.visit(url)
  
  print('log in and navigate to the input page')
  print(str(len(metadata)) + ' elements')
  input("press enter...")
  
  print('filling title fields')
  
  titleinputs = browser.find_by_xpath('//*[contains(@id, "_15_Title_INSTANCE_")]')
  
  print(metadata)
  
  for i in range(0, len(metadata)):
    thistitle = str(metadata[i]['title']+' '+metadata[i]['creator']+' '+metadata[i]['date'])
    titleinputs[i].fill(thistitle)
  
  print('moving to image names')
  
  for i in range(0, len(imagenames)):
    pyperclip.copy(str(imagenames[i]))
    input('image name ' + str(i+1) + ' : ' + str(imagenames[i]) + ' copied to clipboard, press enter to copy the next image name...')
  
  print('end of image names')
  input('press enter to exit...')
  input('are you sure?')