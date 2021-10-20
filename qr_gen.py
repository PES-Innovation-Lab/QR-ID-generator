import qrcode
import uuid
import os
import sys

# 120 ID cards by default
if len(sys.argv)<2: n = 170
else: n = int(sys.argv[1])

if not os.path.exists("QR Code"):
    os.makedirs("QR Code")
f=open(os.path.join("QR Code","data.csv"),"w")
for i in range(n):
    id = uuid.uuid4().hex
    qrcode.make(id).save(os.path.join("QR Code",f"{i}.png"))
    print(f"false,false,false,false,{uuid.uuid4().hex},false,false,,", file=f)