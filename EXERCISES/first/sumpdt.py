def sumpdt():
    n=raw_input("enter the limit")
    p = 1
    s = 1
    tup = ();
    print range(1, int(n))
    for i in range(1, int(n)+1):
        p = p*i
        print p, i
        s = s+i
    tup = (p,s);
    return tup
if __name__ == "__main__":
     a,b = sumpdt()
     print "sum=", b
     print "product=", a
 
