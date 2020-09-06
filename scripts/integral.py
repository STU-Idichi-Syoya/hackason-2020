

I2="https://8f15f039d438.ngrok.io"+f"/static/i3.jpg"

I3="https://8f15f039d438.ngrok.io"+f"/static/i2.png"
import os
ROOT_URL=os.getenv("MYURL")

print(I2)
print(I3)
imgs=["i2.png","i4.jpg","i6.jpg","i5.jpg"]

import random,time
random.seed(int(time.time()))
def rand_img():
    uri=random.choice(imgs)
    return ROOT_URL+"/static/"+uri
