import qrcode

def qr_generate(url):
    """returns qrcode of provided url"""

    qr = qrcode.make(url) #creates qrcode 
    qr.save('qrcode.png') #saves image
    qr.show() # displays image in OS image manager.
    qr = qr.get_image() #renders image in ipynb
    return qr
   



