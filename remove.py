from rembg import remove
from PIL import Image
intq="pranav.jpg"
out1='out.png'
input=Image.open(intq)
out=remove(input)
out.save(out1)
out.show()