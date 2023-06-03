import qrcode

url = 'https://bskyvision.com'
qrcode_img = qrcode.make(url)
qrcode_img.save('./my_qrcode.png')