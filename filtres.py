from PIL import Image
from math import sqrt
import numpy as np

image1 = Image.open("river.jpg").convert("RGB")

#image2 = Image.open('lenaColorBruit.png').convert("RGB")
#image3 = Image.open('ai.jpg')
#image0 = Image.open('w.png')



def image_stock(image,n):
    image_stock = Image.new("RGB",(image.width+(n-1),image.height+(n-1)),(0,0,0))
    im_pix= image.load()
    imst_pix = image_stock.load()
    for i in range(image.width):
        for j in range(image.height):
            r,g,b = im_pix[i,j]
            imst_pix[i+(n//2),j+(n//2)] = (r,g,b)         
    return image_stock

def filtre_Moyenneur(image):
    n = 3
    imageFiltree = Image.new('RGB',(image.width,image.height),(0,0,0))
    imf_pix = imageFiltree.load()
    im_stock = image_stock(image,n)
    imst_pix = im_stock.load()
    for i in range(image.width):
        for j in range(image.height):
            somme_r = 0
            somme_g = 0
            somme_b = 0
            for k in range(i,i+n):
                for l in range(j,j+n):
                    r,g,b = imst_pix[k,l]
                    somme_r += r
                    somme_g += g
                    somme_b += b
            imf_pix[i,j] = (somme_r//(n**2),somme_g//(n**2),somme_b//(n**2))
    return imageFiltree 



def filtre_Median(image):
    n = 3
    imageFiltree = Image.new('RGB',(image.width,image.height),(0,0,0))
    imf_pix = imageFiltree.load()
    im_stock = image_stock(image,n)
    imst_pix = im_stock.load()
    for i in range(image.width):
        for j in range(image.height):
            somme_r = []
            somme_g = []
            somme_b = []
            for k in range(i,i+n):
                for l in range(j,j+n):
                    r,g,b = imst_pix[k,l]
                    somme_r.append(r)
                    somme_g.append(g)
                    somme_b.append(b)
            imf_pix[i,j] = (int(np.median(somme_r)),int(np.median(somme_g)),int(np.median(somme_b)))
    return imageFiltree;





def filtre_Erosion(image):
    n = 3
    imageFiltree = Image.new('RGB',(image.width,image.height),(0,0,0))
    imf_pix = imageFiltree.load()
    im_stock = image_stock(image,n)
    imst_pix = im_stock.load()
    for i in range(image.width):
        for j in range(image.height):
            rm,gm,bm = imst_pix[i,j]
            for k in range(i,i+n):
                for l in range(j,j+n):
                    r,g,b = imst_pix[k,l]
                    if rm> r:
                        rm = r
                    if gm> g:
                        gm = g
                    if bm> b:
                        bm = b
            imf_pix[i,j] = (rm,gm,bm)
    return imageFiltree;




def filtre_Dilatation(image):
    n = 3
    imageFiltree = Image.new('RGB',(image.width,image.height),(0,0,0))
    imf_pix = imageFiltree.load()
    im_stock = image_stock(image,n)
    imst_pix = im_stock.load()
    for i in range(image.width):
        for j in range(image.height):
            rm,gm,bm = imst_pix[i,j]
            for k in range(i,i+n):
                for l in range(j,j+n):
                    r,g,b = imst_pix[k,l]
                    if rm< r:
                        rm = r
                    if gm< g:
                        gm = g
                    if bm< b:
                        bm = b
            imf_pix[i,j] = (rm,gm,bm)
    return imageFiltree;


def gradient_Morphologique(image):
    gradient = Image.new('RGB',(image.width,image.height),(0,0,0))
    imageErosee = filtre_Erosion(image,3)
    imageDilatee = filtre_Dilatation(image,3)
    imgr_pix = (gradient.load())
    imer_pix = (imageErosee.load())
    imdl_pix = (imageDilatee.load())
    for i in range(image.width):
        for j in range(image.height):
            rE,gE,bE = imer_pix[i,j]
            rD,gD,bD = imdl_pix[i,j]
            imgr_pix[i,j] = (rD-rE,gD-gE,bD-bE)
    
    return gradient




def filtre_SobelVertical(image):
    w = image.width
    h = image.height
    im_stock = image_stock(image,3)
    imst_pix = im_stock.load()
    imageFiltree = Image.new('RGB',(w,h),(0,0,0))
    imf_pix = (imageFiltree.load())
    filtre = [[1,2,1],[0,0,0],[-1,-2,-1]]
    for i in range(w):
        for j in range(h):
            somme_r = 0
            somme_g = 0
            somme_b = 0
            for k in range(i,i+3):
                for l in range(j,j+3):
                    p = k-i
                    q = l-j
                    #en cette partie j'ai pas réussi à faire qlq chose de simple
                    #j'ai fait 2 changement d'indices (décalage) p et q
                    #de cette façon p et q vont de 0 à 2 pour manipuler les valeurs du filtre
                    r,g,b = imst_pix[k,l]
                    valeur_r = r*filtre[p][q]
                    valeur_g = g*filtre[p][q]
                    valeur_b = b*filtre[p][q]
                    #je met ces valeurs dans les sommes
                    somme_r += valeur_r
                    somme_g += valeur_g
                    somme_b += valeur_b
            #imf_pix[i,j] =  (abs(somme_r),abs(somme_g),abs(somme_b))
            imf_pix[i,j] =  (min(abs(somme_r),255),min(abs(somme_g),255),min(abs(somme_b),255))
    return imageFiltree



def filtre_SobelHorizontal(image):
    w = image.width
    h = image.height
    im_stock = image_stock(image,3)
    imst_pix = im_stock.load()
    imageFiltree = Image.new('RGB',(w,h),(0,0,0))
    imf_pix = (imageFiltree.load())
    filtre = [[1,0,-1],[2,0,-2],[1,0,-1]]
    for i in range(w):
        for j in range(h):
            somme_r = 0
            somme_g = 0
            somme_b = 0
            for k in range(i,i+3):
                for l in range(j,j+3):
                    p = k-i
                    q = l-j
                    #en cette partie j'ai pas réussi à faire qlq chose de simple
                    #j'ai fait 2 changement d'indices (décalage) p et q
                    #de cette façon p et q vont de 0 à 2 pour manipuler les valeurs du filtre
                    r,g,b = imst_pix[k,l]
                    valeur_r = r*filtre[p][q]
                    valeur_g = g*filtre[p][q]
                    valeur_b = b*filtre[p][q]
                    #je met ces valeurs dans les sommes
                    somme_r += valeur_r
                    somme_g += valeur_g
                    somme_b += valeur_b
            imf_pix[i,j] =  (min(abs(somme_r),255),min(abs(somme_g),255),min(abs(somme_b),255))
    return imageFiltree


def filtre_SobelNormeGradient(image):
    w = image.width
    h = image.height
    Gx_pix = filtre_SobelVertical(image).load()
    Gy_pix = filtre_SobelHorizontal(image).load()
    imageFiltree = Image.new('RGB',(w,h),(0,0,0))
    imf_pix = (imageFiltree.load())
    for i in range(w):
        for j in range(h):
            rX,gX,bX = Gx_pix[i,j]
            rY,gY,bY = Gy_pix[i,j]
            r = int(sqrt(rX**2 + rY**2))
            g = int(sqrt(gX**2 + gY**2))
            b = int(sqrt(bX**2 + bY**2))
            imf_pix[i,j]= r,g,b
    return imageFiltree

def filtre_Edgedetection(image):
    w = image.width
    h = image.height
    im_stock = image_stock(image,3)
    imst_pix = im_stock.load()
    imageFiltree = Image.new('RGB',(w,h),(0,0,0))
    imf_pix = (imageFiltree.load())
    filtre = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
    for i in range(w):
        for j in range(h):
            somme_r = 0
            somme_g = 0
            somme_b = 0
            for k in range(i,i+3):
                for l in range(j,j+3):
                    p = k-i
                    q = l-j
                    r,g,b = imst_pix[k,l]
                    valeur_r = r*filtre[p][q]
                    valeur_g = g*filtre[p][q]
                    valeur_b = b*filtre[p][q]
                    somme_r += valeur_r
                    somme_g += valeur_g
                    somme_b += valeur_b
            imf_pix[i,j] =  (min(abs(somme_r),255),min(abs(somme_g),255),min(abs(somme_b),255))
    return imageFiltree

def filtre_Sharpen(image):
    w = image.width
    h = image.height
    im_stock = image_stock(image,3)
    imst_pix = im_stock.load()
    imageFiltree = Image.new('RGB',(w,h),(0,0,0))
    imf_pix = (imageFiltree.load())
    filtre = [[1,0,-1],[2,0,-2],[1,0,-1]]
    for i in range(w):
        for j in range(h):
            somme_r = 0
            somme_g = 0
            somme_b = 0
            for k in range(i,i+3):
                for l in range(j,j+3):
                    p = k-i
                    q = l-j
                    r,g,b = imst_pix[k,l]
                    valeur_r = r*filtre[p][q]
                    valeur_g = g*filtre[p][q]
                    valeur_b = b*filtre[p][q]
                    somme_r += valeur_r
                    somme_g += valeur_g
                    somme_b += valeur_b
            imf_pix[i,j] =  (min(abs(somme_r),255),min(abs(somme_g),255),min(abs(somme_b),255))
    return imageFiltree

def filtre_Gaussianblur(image):
    w = image.width
    h = image.height
    im_stock = image_stock(image,3)
    imst_pix = im_stock.load()
    imageFiltree = Image.new('RGB',(w,h),(0,0,0))
    imf_pix = (imageFiltree.load())
    filtre = [[1,2,1],[2,4,2],[1,2,1]]
    for i in range(w):
        for j in range(h):
            somme_r = 0
            somme_g = 0
            somme_b = 0
            for k in range(i,i+3):
                for l in range(j,j+3):
                    p = k-i
                    q = l-j
                    r,g,b = imst_pix[k,l]
                    valeur_r = r*filtre[p][q]
                    valeur_g = g*filtre[p][q]
                    valeur_b = b*filtre[p][q]
                    somme_r += valeur_r
                    somme_g += valeur_g
                    somme_b += valeur_b
            imf_pix[i,j] =  (min(abs(int(1/16*somme_r)),255),
                             min(abs(int(1/16*somme_g)),255),
                             min(abs(int(1/16*somme_b)),255))
    return imageFiltree

def filtre_Sharpen(image):
    w = image.width
    h = image.height
    im_stock = image_stock(image,3)
    imst_pix = im_stock.load()
    imageFiltree = Image.new('RGB',(w,h),(0,0,0))
    imf_pix = (imageFiltree.load())
    filtre = [[0,-1,0],[-1,5,-1],[0,-1,0]]
    for i in range(w):
        for j in range(h):
            somme_r = 0
            somme_g = 0
            somme_b = 0
            for k in range(i,i+3):
                for l in range(j,j+3):
                    p = k-i
                    q = l-j
                    r,g,b = imst_pix[k,l]
                    valeur_r = r*filtre[p][q]
                    valeur_g = g*filtre[p][q]
                    valeur_b = b*filtre[p][q]
                    somme_r += valeur_r
                    somme_g += valeur_g
                    somme_b += valeur_b
            imf_pix[i,j] =  (min(abs(int(somme_r)),255),
                             min(abs(int(somme_g)),255),
                             min(abs(int(somme_b)),255))
    return imageFiltree

def filtre_Emboss(image):
    w = image.width
    h = image.height
    im_stock = image_stock(image,3)
    imst_pix = im_stock.load()
    imageFiltree = Image.new('RGB',(w,h),(0,0,0))
    imf_pix = (imageFiltree.load())
    filtre = [[-2,-1,0],[-1,1,1],[0,1,2]]
    for i in range(w):
        for j in range(h):
            somme_r = 0
            somme_g = 0
            somme_b = 0
            for k in range(i,i+3):
                for l in range(j,j+3):
                    p = k-i
                    q = l-j
                    r,g,b = imst_pix[k,l]
                    valeur_r = r*filtre[p][q]
                    valeur_g = g*filtre[p][q]
                    valeur_b = b*filtre[p][q]
                    somme_r += valeur_r
                    somme_g += valeur_g
                    somme_b += valeur_b
            imf_pix[i,j] =  (min(abs(int(somme_r)),255),
                             min(abs(int(somme_g)),255),
                             min(abs(int(somme_b)),255))
    return imageFiltree

def effect_Saturation(image):
    n = 3
    imageFiltree = Image.new('RGB',(image.width,image.height),(0,0,0))
    imf_pix = imageFiltree.load()
    image_pix = image.load()
    for i in range(image.width):
        for j in range(image.height):
            r,g,b = image_pix[i,j]
            imf_pix[i,j] =  (min(abs(int(r+100)),255),
                             min(abs(int(g)),255),
                             min(abs(int(b+100)),255))
    return imageFiltree 

def effet_Joli(image):
    n = 3
    imageFiltree = Image.new('RGB',(image.width,image.height),(0,0,0))
    imf_pix = imageFiltree.load()
    image_pix = image.load()
    for i in range(image.width):
        for j in range(image.height):
            r,g,b = image_pix[i,j]
            imf_pix[i,j] =  (min(abs(int(r+100)),255),
                             min(abs(int(g+100)),255),
                             min(abs(int(b+100)),255))
    return imageFiltree 




def contraste(image):
    s = 150
    v = 50
    img_pix = image.load()
    w,h = image.size
    image_fil = Image.new('RGB',(w,h),(0,0,0))
    img_fil_pix = image_fil.load()
    for i in range(w):
        for j in range(h):
            r,g,b = img_pix[i,j]
            if r>= s : rf = min(r+v,256)
            else: rf = max(r-v,0)
            if g>= s : gf = min(g+v,256)
            else: gf = max(g-v,0)
            if b>= s : bf = min(b+v,256)
            else: bf = max(b-v,0)
            img_fil_pix[i,j] = rf,gf,bf
    return image_fil

def rgb_to_intensity(r, g, b):
    return int((r + g + b) / 3)

#IMPORTANT: en augmentant la valeur de radius l'image deveint plus stylée
#Mais ça prend beaucoup bcp de temps
#Essayez vous meme pour voir c'est stylé

def oil_paint(image, radius=2, intensity_levels=16):
    width, height = image.size
    pixels = image.load()
    im_stck = image_stock(image,(radius*2)+1)
    imst_pix = im_stck.load()
    # Create new output image
    output_img = Image.new("RGB", (width, height))
    output_pixels = output_img.load()

    for y in range(height):
        for x in range(width):
            histogram = [0] * intensity_levels
            average_r = [0] * intensity_levels
            average_g = [0] * intensity_levels
            average_b = [0] * intensity_levels

            # Neighborhood loop
            for dy in range(-radius, radius + 1):
                for dx in range(-radius, radius + 1):
                    nx = x + dx
                    ny = y + dy
                    r, g, b = imst_pix[nx,ny]
                    intensity = rgb_to_intensity(r, g, b) * intensity_levels // 256
                    intensity = min(intensity, intensity_levels - 1)

                    histogram[intensity] += 1
                    average_r[intensity] += r
                    average_g[intensity] += g
                    average_b[intensity] += b

            # Find dominant intensity level
            dominant = histogram.index(max(histogram))
            count = histogram[dominant]

            if count == 0:
                output_pixels[x, y] = pixels[x, y]
            else:
                r = average_r[dominant] // count
                g = average_g[dominant] // count
                b = average_b[dominant] // count
                output_pixels[x, y] = (r, g, b)

    return output_img


im = contraste(image1)
im.show()