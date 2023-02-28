# install library name == qrcode image
''' it install this things=== pypng ,qr code , six , pillow , django, image '''
import qrcode

qr = qrcode.QRCode(
       version =1 ,
       box_size = 10,
       border=4
    )
a = input(" Enter a site name a , web ")
qr.add_data(a)
qr.make(fit=True)
img = qr.make_image(fill_color="black" , back_color="white")
    
c = input("Input File name with .png ")
img.save(c)


''' check always how to use lib check on internet '''
 

