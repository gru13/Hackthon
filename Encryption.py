from numpy import array,uint8,mod
from cv2 import imshow, imread,imwrite,INTER_LINEAR,resize,waitKey,destroyAllWindows,split,merge
from os import getcwd,chdir
from tinyec.ec import *

def Key(Gen_point:tuple, private_key_a:int, private_key_b:int, prime_field:int, order_field:int)->list[list]:
    G = Gen_point # Generating Point 

    na,nb= private_key_a, private_key_b  # private keys of user a and user b

    P = prime_field # prime field

    o = order_field # order of curve
    # creting the prime field
    
    feild = SubGroup(31,(1,6),41,1)
    #  creting curve
    
    curve = Curve(1,3,feild)
    # change the point G into curve
    
    G = Point(curve,G[0],G[1])
    # 
    #  creating public keys pa & pb
    pa = na*G
    pb = nb*G
    # 
    # finding the final key after key exchange
    ka = na*pb
    kb = nb*pa

    if (ka!=kb):    
        raise "Some error in key change or public domain"

    Ki = ka# intial Key
    # print(("na",na,"nb",nb),pa,pb,"final point after sharing",ka,'',sep="\n")

    k1 = Ki.x*G
    k2 = Ki.y*G

    a,b,c,d = k1.x,k1.y,k2.x,k2.y

    #  creating 4 x 4 self invertable

    Key = [[a,b,1-a,-b], [c,d,-c,1-d], [1+a,b,-a,-b], [c,1+d,-c,-d]]
    
    return Key

def cipher_de(img,K):
    img = array(img)
    K = mod(K,256)
    img_size = img.shape
    total_pixel = img.size
    img = img.flatten()
    Encry = []
    for i in range(0,total_pixel,4):
        Encry += list(K@img[i:i+4])
    Encry = array(Encry)
    Encry = Encry.reshape(512,512)
    Encry = array(Encry,dtype=uint8)
    return Encry
def cipher_de_rgb(img,K):
    b,g,r  = split(img)
    Encry  = merge([cipher_de(r,K),cipher_de(g,K),cipher_de(b,K)])
    Encry = array(Encry,dtype=uint8)
    return Encry

def show(h):
    j = array(h)
    img = array(j,dtype=uint8)
    imshow("ECC",img)
    waitKey(3000)

def save_image(save_name,image):
    chdir(getcwd())
    image = image.astype('uint8')
    image = image.clip(0, 255)
    image = resize(image,(512,512),interpolation = INTER_LINEAR)
    imwrite(save_name, image)


def Encryption(img_name,pa,pb):
    G=(1,6) # Generating Point 
    na,nb= pa,pb  # private keys of user a and user b
    P = 137 # prime field
    o = 152
    K = Key(G,na,nb,P,o)
    ima = imread(img_name)
    ima = resize(ima,(512,512))
    encr = cipher_de_rgb(ima,K)
    imagename = img_name.split(".")
    imagename = imagename[0]+"_Modified.png"
    save_image(imagename,encr)
    return imagename


if __name__ == "__main__":
    G=(1,6) # Generating Point 
    na,nb= 13, 17  # private keys of user a and user b
    P = 137 # prime field
    o = 152
    K = Key(G,na,nb,P,o)
    
    
    ima = imread("leo.png",0)
    # ima = imread("dd.png",0)

    ima = resize(ima,(512,512))
    show(ima)
    r = cipher_de(ima,K)
    show(r)
    r = array(r,dtype=uint8)
   
    save_image("leo.png",r)
    show(cipher_de(r,K))
    
    # show(cipher_de_rgb(cipher_de_rgb(ima,K),K))

    destroyAllWindows()

