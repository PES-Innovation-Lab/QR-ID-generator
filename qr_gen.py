import qrcode
import uuid
import os
import sys

# 120 ID cards by default
if len(sys.argv)<2: n = 120
else: n = int(sys.argv[1])

if not os.path.exists("QR Code"):
    os.makedirs("QR Code")

for i in range(n):
    
    qrcode.make(uuid.uuid4().hex).save(os.path.join("QR Code",f"{i}.png"))