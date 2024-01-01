import pyqrcode
import png
from pyqrcode import QRCode
s = input("enter the link to open a website : ")
url = pyqrcode.create(s)
url.svg("myqr.svg", scale = 8)
url.png('pranav47.png', scale = 6)
url.show()