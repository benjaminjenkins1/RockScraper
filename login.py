from splinter import Browser

#REQUIRES SPLINTER AND CHROME WEBDRIVER

with Browser("chrome") as browser:
  url = "http://10.13.9.53:8080/web/guest/login"
  browser.visit(url)
  input("press enter...")
  
  browser.visit(url)
  username = browser.find_by_id("_58_login")
  password = browser.find_by_id("_58_password")
  button = browser.find_by_text(" Sign In ")
  
  username.fill('benjamin.jenkins1@marist.edu')
  password.fill()
  button.click()
  
  url = "http://10.13.9.53:8080/digital-library-listing;"
  browser.visit(url)
  
  script = browser.find_link_by_partial_href("javascript:Liferay")
  script = script["href"].replace("javascript:","")
  browser.execute_script(script)
  
  title = browser.find_by_xpath('//*[@id="_15_title__en__US"]')
  thumbnail = browser.find_by_xpath('//*[@id="_15_imagethumbnail_INSTANCE_tdlu"]')
  PDFPreview = browser.find_by_xpath('//*[@id="_15_pdfPreviewImage_INSTANCE_rjmp"]')
  fileURL = browser.find_by_xpath('//*[@id="_15_FileURL_INSTANCE_ljue"]')
  type = browser.find_by_xpath('')
  
  input("press enter...")
  
    