from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

br = webdriver.Safari()
br.get('https://www.urbanoutfitters.com/shop/converse-chuck-taylor-all-star-canvas-platform-high-top-sneaker?category=SEARCHRESULTS&color=015&searchparams=q%3Dsneaker&type=REGULAR&quantity=1')

save_me = ActionChains(br).key_down(Keys.CONTROL).key_down('s').key_up(Keys.CONTROL).key_up('s')
save_me.perform()
save_me = ActionChains(br).key_down(Keys.ENTER).key_up(Keys.ENTER) 
save_me.perform()