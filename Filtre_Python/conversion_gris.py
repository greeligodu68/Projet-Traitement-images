from PIL import Image
import os 

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