import qrcode
from base64 import b64encode

qrcode_txt='?re=NME1208243S4&rr=XAXX010101000&tt=0000000118.000000&id=89D3210C-188F-4C7F-B818-445B8F655AF5'
qr = qrcode.QRCode(version=4, error_correction=qrcode.constants.ERROR_CORRECT_Q, box_size=10, border=4)
qr.add_data(qrcode_txt)
qr.make()
img=qr.make_image()
print b64encode(img_data.read())
