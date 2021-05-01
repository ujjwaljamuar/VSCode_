from PIL import Image

mac=Image.open('example.jpg')
print(mac.show())

print(mac.size)

# Cropping
newmac=mac.crop((0,0,100,100))
print(newmac.show())

mac1=Image.open('pencils.jpg')
print(mac1.show())
x=0
y=1100
w=1950/3
h=1300
newmac1=mac1.crop((x,y,w,h))

nemac1=mac1.paste(im=newmac1,box=(0,0))
print(nemac1.show())

mac1.resize((3000,500))

mac1.rotate(90)

'''
blie.save('purple.png')
purple=Image.open('purple.png')
'''