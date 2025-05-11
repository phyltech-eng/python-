import qrcode
data = 'follow me on github'



qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color='purple', back_color='white')
img.save('C:/Users/hp/Desktop/desktop/python/qrcode.png')

