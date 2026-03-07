from PIL import Image

img = Image.open("1412.png")
pixels = list(img.getdata())

bits = []
for p in pixels:
    bits.append(str(p[1] & 1)) #green

bitstream = "".join(bits)

def decode(bs):
    out = bytearray()
    for i in range(0,len(bs),8):
        byte = bs[i:i+8]
        if len(byte)==8:
            out.append(int(byte,2))
    return out

print("Melakukan brute force shifting untuk mencari kata kunci...")
print(f"Total bits dalam bitstream: {len(bitstream)}")

for shift in range(8):
    print(f"Trying shift = {shift}...")
    
    shifted = bitstream[shift:]
    data = decode(shifted)

    text = data.decode("ascii",errors="ignore")

    preview = text[:50].replace('\n', '\\n').replace('\r', '\\r')
    print(f"  Preview: '{preview}'")
    
    if "MOON" in text or "1412" in text:
        print(f"FOUND keyword at shift {shift}!")
        print("\nSHIFT =",shift)
        print(text[:3020])
        break
    else:
        print(f"Keyword not found at shift {shift}")
    