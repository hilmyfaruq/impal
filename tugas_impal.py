#no1
a = int(input('masukkan nilai a = '))
b = int(input('masukkan nilai b = '))
c = int(input('masukkan nilai c = '))
def segitiga(a,b,c):
    
    if (a==b==c):
        p = "segitiga sama sisi"

    elif (a==b):
        p = "segitiga sama kaki"

    elif (b==c):
        p = "segitiga sama kaki"

    elif (c==a):
        p = "segitiga sama kaki"
    
    elif (a<=0 or b<=0 or c<=0):
        p = "segitiga tidak bisa dibangun"

    elif (a*a==b*b + c*c or b*b == a*a + c*c or c*c == b*b + a*a):
        p = "segitiga siku-siku"
    else:
        p = "segitiga bebas"
    return p
print(segitiga(a,b,c))

#no2
a = float(input('masukkan nilai a = '))
b = float(input('masukkan nilai b = '))
c = float(input('masukkan nilai c = '))
def segitiga(a,b,c):
    
    if (a==b==c):
        p = "segitiga sama sisi"

    elif (a==b):
        p = "segitiga sama kaki"

    elif (b==c):
        p = "segitiga sama kaki"

    elif (c==a):
        p = "segitiga sama kaki"
    
    elif (a<=0 or b<=0 or c<=0):
        p = "segitiga tidak bisa dibangun"

    elif (a*a==b*b + c*c or b*b == a*a + c*c or c*c == b*b + a*a):
        p = "segitiga siku-siku"
    else:
        p = "segitiga bebas"
    return p
print(segitiga(a,b,c))

