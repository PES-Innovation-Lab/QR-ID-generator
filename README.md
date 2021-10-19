# QR-ID-generator

A system used to generate QR Codes for ID Cards used by participants in Hashcode 2021.

## Usage
To generate N QR-Codes, run the following command:
```python 
python3 qr_gen.py N
```
If no value is provided, 120 codes will be generated.

QR Codes will be stored in a subdirectory of the present working directory called `QR Code`. QR Codes generated will be of the format `QR Code\[0-N].png`

## To Do
- [ ] Generate data to populate database before the hackathon.

