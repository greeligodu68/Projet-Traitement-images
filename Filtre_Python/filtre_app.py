from PIL import Image
import os 

def image_stock(image,n):
    image_stock = Image.new("RGB",(image.width+(n-1),image.height+(n-1)),(0,0,0)).convert("RGB")
    im_pix= image.load()
    imst_pix = image_stock.load()
    for i in range(image.width):
        for j in range(image.height):
            r,g,b = im_pix[i,j]
            imst_pix[i+(n//2),j+(n//2)] = (r,g,b)         
    return image_stock

def convert_gray(image_path):
 
    image = Image.open(image_path).convert("RGB")
    width, height = image.size 
    pix_rgb = image.load()  

    
    im_gray = Image.new("L", (width, height), 0)
    pix_gray = im_gray.load()

    
    for i in range(width):
        for j in range(height):
            pix_gray[i, j] = int(0.299 * pix_rgb[i, j][0] + 
                                 0.587 * pix_rgb[i, j][1] + 
                                 0.114 * pix_rgb[i, j][2])
    
    output_path = image_path  
    im_gray.save(output_path)                          

    return output_path    

def filtreMoyenneur(image_path, filterSize=3):
    image = Image.open(image_path) 
    height = image.height
    width = image.width

  
    if image.mode == 'RGBA' or image.mode == 'RGB':
        imageFiltre = Image.new(image.mode, (width, height), 0)
    elif image.mode == 'P':
        imageFiltre = Image.new("L", (width, height), 0)

    img_norm = image.load()
    img_filtre_Moy = imageFiltre.load()

    if image.mode in ['RGB', 'RGBA']:
        for x in range(width):
            for y in range(height):
                sommeR = sommeG = sommeB = sommeA = 0
                pixHorsRange = 0
                for i in range(x - filterSize // 2, x + filterSize // 2 + 1):
                    for j in range(y - filterSize // 2, y + filterSize // 2 + 1):
                        if 0 <= i < width and 0 <= j < height:
                            sommeR += img_norm[i, j][0]
                            sommeG += img_norm[i, j][1]
                            sommeB += img_norm[i, j][2]
                            if image.mode == 'RGBA':
                                sommeA += img_norm[i, j][3]
                        else:
                            pixHorsRange += 1
                taille = filterSize ** 2 - pixHorsRange

                if image.mode == 'RGBA':
                    img_filtre_Moy[x, y] = (sommeR // taille, sommeG // taille, sommeB // taille, sommeA // taille)
                else: 
                    img_filtre_Moy[x, y] = (sommeR // taille, sommeG // taille, sommeB // taille)

    elif image.mode == "P":
        for x in range(width):
            for y in range(height):
                somme = 0
                pixHorsRange = 0
                for i in range(x - filterSize // 2, x + filterSize // 2 + 1):
                    for j in range(y - filterSize // 2, y + filterSize // 2 + 1):
                        if 0 <= i < width and 0 <= j < height:
                            somme += img_norm[i, j]
                        else:
                            pixHorsRange += 1
                img_filtre_Moy[x, y] = somme // (filterSize ** 2 - pixHorsRange)

    
    output_path = image_path  
    imageFiltre.save(output_path)  
    return output_path  



def filtre_Erosion(image_path):
    image = Image.open(image_path).convert("RGB")
    n = 3
    imageFiltree = Image.new('RGB',(image.width,image.height),(0,0,0)).convert("RGB")
    im_stock = image_stock(image,n)
    
    imst_pix = im_stock.load()
    imf_pix = imageFiltree.load()
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
    output_path = image_path 
    imageFiltree.save(output_path)  
    return output_path  


def filtre_Dilatation(image_path):
    n = 3
    image = Image.open(image_path).convert("RGB")
    imageFiltree = Image.new('RGB',(image.width,image.height),(0,0,0)).convert("RGB")
    im_stock = image_stock(image,n)
    
    imst_pix = im_stock.load()
    imf_pix = imageFiltree.load()
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
    output_path = image_path
    imageFiltree.save(output_path)  
    return output_path  


def gradient_Morphologique(image_path):
    image = Image.open(image_path).convert("RGB")
    n = 3
    largeur, hauteur = image.width, image.height

    im_stock = image_stock(image, n)
    imst_pix = im_stock.load()

    gradient = Image.new('RGB', (largeur, hauteur), (0, 0, 0))
    imgr_pix = gradient.load()

    for i in range(largeur):
        for j in range(hauteur):
            min_r, min_g, min_b = 255, 255, 255
            max_r, max_g, max_b = 0, 0, 0

            for k in range(n):
                for l in range(n):
                    x = i + k
                    y = j + l
                    r, g, b = imst_pix[x, y]
                    
            
                    min_r = min(min_r, r)
                    min_g = min(min_g, g)
                    min_b = min(min_b, b)

                
                    max_r = max(max_r, r)
                    max_g = max(max_g, g)
                    max_b = max(max_b, b)

            imgr_pix[i, j] = (max_r - min_r, max_g - min_g, max_b - min_b)

    output_path = image_path
    gradient.save(output_path)
    return output_path


def filtre_Edgedetection(image_path):
    image = Image.open(image_path).convert("RGB")
    w = image.width
    h = image.height
    im_stock = image_stock(image,3)
    imst_pix = im_stock.load()
    imageFiltree = Image.new('RGB',(w,h),(0,0,0)).convert("RGB")
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
    output_path = image_path
    imageFiltree.save(output_path)  
    return output_path  

def quantifier_couleur(couleur, niveaux=5):
    step = 256 // niveaux
    return tuple((val // step) * step for val in couleur)


def filtre_Cartoon(image_path, seuil_contour=80, niveaux_couleur=5  ):

    image = Image.open(image_path)
    if image.mode != "RGB":
        image = image.convert("RGB")


    filtreMoyenneur(image_path, filterSize=5)
    image_lissée = Image.open(image_path).convert("RGB")
    width = image_lissée.width
    height = image_lissée.height
    lissée_pix = image_lissée.load()

 
    for i in range(width):
        for j in range(height):
            lissée_pix[i, j] = quantifier_couleur(lissée_pix[i, j], niveaux_couleur)

    temp_path = "temp_gray.png"
    image_lissée.save(temp_path)
    convert_gray(temp_path)            
    filtre_Edgedetection(temp_path)     
    contours = Image.open(temp_path).convert("L")
    contour_pix = contours.load()

    # Fusion contours + image quantifiée
    final_image = Image.new("RGB", (width, height))
    final_pix = final_image.load()
    for i in range(width):
        for j in range(height):
            if contour_pix[i, j] > seuil_contour:
                final_pix[i, j] = (0, 0, 0)
            else:
                final_pix[i, j] = lissée_pix[i, j]


    output_path = image_path
    final_image.save(output_path)
    return output_path




def contraste(image_path):
    s = 150
    v = 50
    image = Image.open(image_path).convert('RGB')
    n=3
    im_stock = image_stock(image, n)
    imst_pix = im_stock.load()
    w,h = image.size
    image_fil = Image.new('RGB',(w,h),(0,0,0))
    img_fil_pix = image_fil.load()
    for i in range(w):
        for j in range(h):
            r,g,b = imst_pix[i,j]
            if r>= s : rf = min(r+v,256)
            else: rf = max(r-v,0)
            if g>= s : gf = min(g+v,256)
            else: gf = max(g-v,0)
            if b>= s : bf = min(b+v,256)
            else: bf = max(b-v,0)
            img_fil_pix[i,j] = rf,gf,bf
    output_path = image_path
    image_fil.save(output_path)
    return output_path

def rgb_to_intensity(r, g, b):
    return int((r + g + b) / 3)



def oil_paint(image_path, radius=2, intensity_levels=16):
    image= Image.open(image_path).convert('RGB')
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

    output_path = image_path
    output_img.save(output_path)
    return output_path
