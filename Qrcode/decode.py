from pyzbar.pyzbar import decode
from PIL import Image

img= Image.open('C:/Users/hp/Desktop/desktop/python/qrcode.png')
result=decode(img)
print(result[0].data.decode('utf-8'))