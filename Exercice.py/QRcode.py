import qrcode
from PIL import Image

data = ""

qr = qrcode.QRCode(version=1, box_size=10,border=1)
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill_color="black", back_color="white")
image.save("qrcode.jpg")
image.open("qrcode.jpg")
