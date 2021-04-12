from pywebcopy import save_webpage

url = 'https://www.urbanoutfitters.com/shop/converse-chuck-taylor-all-star-canvas-platform-high-top-sneaker?category=SEARCHRESULTS&color=015&searchparams=q%3Dsneaker&type=REGULAR&quantity=1'
download_folder = '.'    

kwargs = {'bypass_robots': True, 'project_name': 'recognisable-name'}

save_webpage(url, download_folder, **kwargs)
