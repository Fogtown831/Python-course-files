
#working on
#makes an image tansparent, not sure if this works
from PIL import Image


def convertImage():
    img = Image.open("csumb logo.jpg")
    img = img.convert("RGBA")

    datas = img.getdata()

    newData = []

    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save("pixQRcode.png", "PNG")
    print("Successful")

convertImage()

#I tried using another similar code to make the image transparent but both seemed not to work
from PIL import Image

image = Image.open('csumb logo.jpg')
image = image.convert('RGBA')
print(image.mode)



newImage = []
for item in image.getdata():
    if item[:3] == (255, 255, 255):
        newImage.append((255, 255, 255, 0))
    else:
        newImage.append(item)

image.putdata(newImage)


image.save('output.png')
print(image.mode, image.size)


#I tried creating a new qrcode with the transparent image but did not work
import qrcode
from PIL import Image

logo_link = "pixQRcode.png"
logo = Image.open(logo_link)


basewidth = 100 #earlier it was 197
wpercent = basewidth/float(logo.size[0])
hsize = int(logo.size[1]*float(wpercent))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

QRcode = qrcode.QRCode(
    error_correction = qrcode.constants.ERROR_CORRECT_H
)

url = "https://www.youtube.com/watch?v=ax_rdEd0e4w"

QRcode.add_data(url)

QRimg = QRcode.make_image(
    fill_color = 'green', back_color = 'black').convert('RGB')

QRimg.paste(logo, (175, 175))
QRimg.save("M3A2QRcode.png")
img = Image.open("M3A2QRcode.png")
img.show()

#using other code
import qrcode
from PIL import Image

logo_link = "output.png"
logo = Image.open(logo_link)


basewidth = 100 #earlier it was 197

wpercent = basewidth/float(logo.size[0])
hsize = int(logo.size[1]*float(wpercent))

logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

QRcode = qrcode.QRCode(
    error_correction = qrcode.constants.ERROR_CORRECT_H
)

url = "https://www.youtube.com/watch?v=ax_rdEd0e4w"

QRcode.add_data(url)

QRimg = QRcode.make_image(
    fill_color = 'green', back_color = 'black').convert('RGB')

QRimg.paste(logo, (175, 175))
QRimg.save("M3A2QRcode.png")
img = Image.open("M3A2QRcode.png")
img.show()

#correct answer ttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt

import qrcode
from PIL import Image

#making it transparent
image = Image.open('csumb logo.jpg')
image1 = image.convert('RGBA')
image2 = image1.getdata()

newdata = []
for item in image2():
    if item[:3] == (255, 255, 255):
        newdata.append((255, 255, 255, 0))
    else:
        newdata.append(item)

image.putdata(newdata)
image.save('output.png')

#qr one starts
logo_link = "csumb logo.jpg"
logo = Image.open(logo_link)


basewidth = 100 #earlier it was 197

wpercent = basewidth/float(logo.size[0])
hsize = int(logo.size[1]*float(wpercent))

logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

#qr code set-up
QRcode = qrcode.QRCode(
    error_correction = qrcode.constants.ERROR_CORRECT_H
)

url = "https://www.youtube.com/watch?v=ax_rdEd0e4w"
QRcode.add_data(url)
QRimg = QRcode.make_image(
    fill_color = 'green', back_color = 'black').convert('RGB')

diff = (QRimg.size[0]-logo.size[0])//2, (QRimg.size[1]-logo.size[1])//2
QRimg.paste(logo, diff, logo)
QRimg.save("mynewQRcode.png")
img = Image.open("mynewQRcode.png")
img.show()