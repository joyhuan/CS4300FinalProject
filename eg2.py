from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time 

browser = webdriver.Safari()

browser.get('https://www.urbanoutfitters.com/shop/converse-chuck-taylor-all-star-canvas-platform-high-top-sneaker?category=SEARCHRESULTS&color=015&searchparams=q%3Dsneaker&type=REGULAR&quantity=1')

# save_me = ActionChains(br).key_down(Keys.CONTROL)\
#          .key_down('s').key_up(Keys.CONTROL).key_up('s')
# save_me.perform()

Actions action= new Actions(driver)
action.contextClick(productLink).sendKeys(Keys.ARROW_DOWN).sendKeys(Keys.ARROW_DOWN).sendKeys(Keys.RETURN).build().perform();

html = browser.page_source
time.sleep(2)
fileToWrite = open("py_source.html", "w")
fileToWrite.write(html)
browser.close()