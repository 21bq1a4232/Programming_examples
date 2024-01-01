import matplotlib as mp
import pyqrcode
import png
from pyqrcode import QRCode
p="www.youtube.com"
url=pyqrcode.create(p)
url.svg("myqr.svg",scale=8)
url.png('myqr.png',scale=6)
mp.plot(url)
mp.show()