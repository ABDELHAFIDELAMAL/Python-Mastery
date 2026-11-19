import qrcode

data = "fsan.ump.ac.ma"

img = qrcode.make(data)

img.save("newqr.png")

print("QR code généré avec succès !")