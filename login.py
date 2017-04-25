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
  
  username.fill('benjaminjenkins1')
  password.fill('')
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
  type = browser.find_by_xpath('//*[id="_15_type1_INSTANCE_rxlz"]')
  description = browser.find_by_xpath('//*[id="_15_Description_INSTANCE_qmcj"]')
  creator = browser.find_by_xpath('//*[id="_15_Creator_INSTANCE_fnml"]')
  source = browser.find_by_xpath('//*[id="_15_Source_INSTANCE_wdej"]')
  date = browser.find_by_xpath('//*[id="_15_date_INSTANCE_txzf"]')
  rights = browser.find_by_xpath('//*[id="_15_Rights_INSTANCE_bavx"]')
  fomat = browser.find_by_xpath('//*[id="_15_Format_INSTANCE_iadt"]')
  extent = browser.find_by_xpath('//*[id="_15_Extent_INSTANCE_zkvz"]')
  language = browser.find_by_xpath('//*[id="_15_Language_INSTANCE_gmeu"]')
  identifier = browser.find_by_xpath('//*[id="_15_Identifier_INSTANCE_tlea"]')
  spatial_coverage = browser.find_by_xpath('//*[id="_15_Spatial_Coverage_INSTANCE_zlzz"]')
  citation = browser.find_by_xpath('//*[id="_15_Citation_INSTANCE_dnmr"]')
  
  
  
  
  
  
  input("press enter...")
  
    