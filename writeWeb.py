# import urllib.request, urllib.error, urllib.parse

# url = "https://www.urbanoutfitters.com/shop/converse-chuck-taylor-all-star-canvas-platform-high-top-sneaker?category=SEARCHRESULTS&color=015&searchparams=q%3Dsneaker&type=REGULAR&quantity=1"

# # url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

# response = urllib.request.urlopen(url)
# webContent = response.read()

# f = open('web_results/product.html', 'wb')
# f.write(webContent)
# f.close

from pywebcopy import save_webpage

url = 'https://www.urbanoutfitters.com/shop/converse-chuck-taylor-all-star-canvas-platform-high-top-sneaker?category=SEARCHRESULTS&color=015&searchparams=q%3Dsneaker&type=REGULAR&quantity=1'
download_folder = 'web_results/product.html'    

kwargs = {'bypass_robots': True, 'project_name': 'recognisable-name'}

save_webpage(url, download_folder, **kwargs)
