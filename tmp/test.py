# ------------------------------------------------------------------
import sys
import numpy

import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

# ------------------------------------------------------------------
def draw_text_at_center(img, text,text1,text2):
    draw = PIL.ImageDraw.Draw(img)
    font_ttf = "tmp\ipaexg.ttf"

    height_font = img.size[1]//8
    # txt_height = draw.font.getsize(text)[1]


    draw.font = PIL.ImageFont.truetype(font_ttf, height_font)



    # pos = (img_size - txt_size) / 2
    margin=30
    draw.text((0,0), text, (0, 0, 255))
    draw.text((0,height_font+margin), text1, (0, 0, 255))
    draw.text((0,height_font*2+margin*2), text2, (0, 0, 255))


# ------------------------------------------------------------------
img = PIL.Image.new("RGB", (400, 300),color=(255,255,255))
text = "○○学校"
text1 = "CO2濃度は5000PPMです"
text2 = "Powerd by 密チェッカー"

draw_text_at_center(img, text,text1,text2)
img.show()
filename = "out01.png"
# img.save(filename)
# img.show()
sys.stderr.write("*** 終了 ***\n")