from numpy import array,uint8,mod

def Encrypt_image(img,K):
    K = mod(K,256)
    img_size = img.shape
    total_pixel = img.size
    img = img.flatten()
    Encry = []
    for i in range(0,total_pixel,4):
        Encry += list(K@img[i:i+4])
    return K


