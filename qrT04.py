import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.moduledrawers.pil import CircleModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from qrcode.image.styles.colormasks import VerticalGradiantColorMask
from qrcode.image.styles.colormasks import SolidFillColorMask
from qrcode.image.styles.colormasks import ImageColorMask
from PIL import Image, ImageDraw


def style_eyes(img):
    img_size = img.size[0]
    box_size = img.box_size
    print('Image Size = ', img_size)
    print('Box Size = ', box_size)
    #border_size = (img_size/box_size - 33 ) /2
    #border_size = (img_size/box_size - 33 ) /2
    border_size = (img_size/box_size - 33 ) 
    quiet_zone = box_size * border_size
    eye_size = 7 * box_size
    quiet_eye_size = eye_size + quiet_zone
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle((quiet_zone, quiet_zone,quiet_eye_size,quiet_eye_size), fill=255)
    draw.rectangle((img_size-quiet_eye_size, quiet_zone, img_size-quiet_zone, quiet_eye_size), fill=255)
    draw.rectangle((quiet_zone, img_size-quiet_eye_size, quiet_eye_size, img_size-quiet_zone), fill=255)
    return mask

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

qr.add_data('https://www.cefp.gob.mx/publicaciones/infografias/2025/dpie/infdpie0302025.pdf')

img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
img_3 = qr.make_image(image_factory=StyledPilImage, embeded_image_path="cd-cefp-logo.png")
img_4 = qr.make_image(image_factory=StyledPilImage, color_mask=VerticalGradiantColorMask(), module_drawer=CircleModuleDrawer(), embeded_image_path="cd-cefp-logo.png" ) 
#img_5 = qr.make_image(image_factory=StyledPilImage, color_mask=ImageColorMask(), module_drawer=CircleModuleDrawer(), embeded_image_path="cd-cefp-logo.png" )
img_6 = qr.make_image( image_factory=StyledPilImage, 
                        #module_drawer = SolidFillColorMask( front_color="red" ),
                        eye_drawer=CircleModuleDrawer(),
                        module_drawer=CircleModuleDrawer( front_color="#336600" ), 
                        embeded_image_path="cd-cefp-logo.png" ) 
img_7 = qr.make_image( image_factory=StyledPilImage,
                        #module_drawer=SolidFillColorMask(front_color='green'),
                        #module_drawer=CircleModuleDrawer( center_color=(92,184,0) ),
                        module_drawer=CircleModuleDrawer( center_color=(200,255,150) ),
                        #eye_drawer=RoundedModuleDrawer( color=(200,255,150) ),
                        #eye_drawer=RoundedModuleDrawer( radius_ratio= 45 ),
                        eye_drawer=RoundedModuleDrawer(),
                        #( radius_ratio= 1 ),
                        color_mask=RadialGradiantColorMask(back_color=(255,255,255), edge_color=(200,255,150), center_color=(51,102,0) ),
                        embeded_image_path="cd-cefp-logo.png")

img_9_eyes = qr.make_image(image_factory=StyledPilImage,
                        eye_drawer=RoundedModuleDrawer(), color_mask=SolidFillColorMask(back_color=(255, 255, 255), front_color=(255, 110, 0))
                        #color_mask=SolidFillColorMask(back_color=(255, 255, 255), front_color=(199 , 8 ,8 ) )
                        )


qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
img_8 = qr.make_image( image_factory=StyledPilImage,
                        #module_drawer=SolidFillColorMask(front_color='green'),
                        #module_drawer=CircleModuleDrawer( center_color=(92,184,0) ),
                        module_drawer=CircleModuleDrawer( center_color=(200,255,150) ),
                        #eye_drawer=RoundedModuleDrawer( center_color=(200,255,150) ),
                        color_mask=RadialGradiantColorMask(back_color=(255,255,255), edge_color=(200,255,150), center_color=(51,102,0) )                        
                        #embeded_image_path="cd-cefp-logo.png"
                        )
mask = style_eyes( img_9_eyes )
im = Image.open("img7d.png")
#img_ok = Image.composite( img_9_eyes, img_7, mask )
img_ok = Image.composite( im, img_7, mask )

img_1.save('img1.png')
img_2.save('img2.png')
img_3.save('img3.png')
img_4.save('img4.png')
#img_5.save('img5.png')
img_6.save('img6.png')
img_7.save('img7.png')
img_8.save('img8.png')
img_9_eyes.save('img9.png')
mask.save('mask.png')
img_ok.save('img_ok.png')


