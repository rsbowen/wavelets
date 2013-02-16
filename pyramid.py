import Image

def pyramid_one(im,approximationFilter):
    imout = Image.new('L',(im.size[0]/2,im.size[1]/2)) #assumes im.size is even
    for i in range(im.size[0]/2):
        for j in range(im.size[1]/2):
            #this is not very pythonic!
            value = approximationFilter(im.getpixel((2*i,2*j)),\
                                        im.getpixel((2*i+1,2*j)),
                                        im.getpixel((2*i,2*j+1)),
                                        im.getpixel((2*i+1,2*j+1)))
            imout.putpixel((i,j),value)
    return imout


im = Image.open('Wolf-Puppy.jpg').convert('L')

x = 200
y = 100

im = im.crop((x,y,x+512,y+512))
im.show()

im2 = pyramid_one(im,lambda a,b,c,d: (a+b+c+d)/4)
im2.show()

im3 = pyramid_one(im2,lambda a,b,c,d: (a+b+c+d)/4)
im3.show()

im4 = pyramid_one(im3,lambda a,b,c,d: (a+b+c+d)/4)
im4.show()
