from tinyec.ec import *
from numpy import array
from numpy.linalg import inv 

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

if __name__ == "__main__":

    G=(1,6) # Generating Point 
    na,nb= 13, 17  # private keys of user a and user b
    P = 137 # prime field
    o = 152
    K = Key(G,na,nb,P,o)
    print(K)