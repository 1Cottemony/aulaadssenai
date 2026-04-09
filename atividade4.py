import qrcode
qr = qrcode.QRCode(version=1, box_size=10, border=5)
data = "https://youtu.be/dQw4w9WgXcQ?list=RDdQw4w9WgXcQ"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

img.save("imagem.png")