from sympy import im


id=0
id= "1BOtomkkayaW1bQiBcSlw2oXiYwKSS1zI"
id2="1KrsU0TyBDJFT4kpFLW-q7as_nTxVgcEW"





I2="https://8f15f039d438.ngrok.io"+f"/static/i3.jpg"

I3="https://8f15f039d438.ngrok.io"+f"/static/i2.png"

print(I2)
print(I3)
imgs=["i2.png","i4.jpg","i6.jpg","i5.jpg"]
import random,time
random.seed(int(time.time()))
def rand_img():
    uri=random.choice(imgs)
    return "https://8f15f039d438.ngrok.io/static/"+uri
