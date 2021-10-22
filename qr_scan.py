from PIL import Image
from pyzbar.pyzbar import decode

f = open("QR Code\data.csv","w")
for i in range(170):
    data = str(decode(Image.open(f'QR Code\{i}.png'))[0].data)[2:-1]
    print(f"false,false,false,false,{data},false,false,,", file=f)