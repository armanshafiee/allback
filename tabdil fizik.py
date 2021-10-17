print("mabahes:+,-,*,/,tabdil,sorat,jabejayi,tondi,masafat,time,shetab")
print("num2=1=>edame,,,num2=0=>by by")
for z in range(999):
    print("1)+")
    print("2)-")
    print("3)*")
    print("4)/")
    print("5)tabdil")
    print("6)sorat")
    print("7)jabejayi")
    print("8)tondi")
    print("9)masafat")
    print("10)time")
    print("11)shetab")
    print("0)exit")
    a=str(input('num :'))
    if a=="1":
        avaly=float(input("avaly"))
        dovomy=float(input("dovomy"))
        hasel=avaly+dovomy
        print(hasel)
        num2=int(input("num2:"))
        if num2==1:
            y=0
        elif num2==0:
            break
    elif a=="2":
        avaly=float(input("avaly"))
        dovomy=float(input("dovomy"))
        hasel=avaly-dovomy
        print(hasel)
        num2=int(input("num2:"))
        if num2==1:
            y=0
        elif num2==0:
            break
    elif a=="3":
        avaly=float(input("avaly"))
        dovomy=float(input("dovomy"))
        hasel=avaly*dovomy
        print(hasel)
        num2=int(input("num2:"))
        if num2==1:
            y=0
        elif num2==0:
            break
    elif a=="4":
        avaly=float(input("avaly"))
        dovomy=float(input("dovomy"))
        hasel=avaly/dovomy
        print(hasel)
        num2=int(input("num2:"))
        if num2==1:
            y=0
        elif num2==0:
            break
    elif a=="5":
        adad = float(input("adad:"))
        vahed =str(input('km or ms :'))
        if vahed == "km":
            adade = adad/3.6
            print(adade,"ms")
        elif vahed == "ms":
            adade = adad*3.6
            print(adade,"km")
        else:
            print("vahedo hamonaro bede")
        num2=int(input("num2:"))
        if num2==1:
            y=0
        elif num2==0:
            break
    elif a=="6":
        jabejayi = float(input("jabejayi:"))
        t = float(input("taim:"))
        sorat = jabejayi/t
        print("sorat motevaset =",sorat)
        num2=int(input("num2:"))
        if num2==1:
            y=0
        elif num2==0:
            break
    elif a=="7":
        sorat = float(input("sorat:"))
        t = float(input("taim:"))
        jabejayi = sorat*t
        print("jabejayi =",jabejayi)
        num2=int(input("num2:"))
        if num2==1:
            y=0
        elif num2==0:
            break
    elif a=="8":
        masafat=float(input("masafat:"))
        t  = float(input("taim:"))
        tondi = masafat/t
        print("tondi=",tondi) 
        num2=int(input("num2:"))
        if num2==1:
            y=0
        elif num2==0:
            break
    elif a=="9":
        tondi=float(input("tondi:"))
        t  = float(input("taim:"))
        masafat=tondi*t
        print("masafat=",masafat)
        num2=int(input("num2:"))
        if num2==1:
            y=0
        elif num2==0:
            break
    elif a=="10":
        masafat=float(input("masafat or jabejayi:"))
        tondi=float(input("tondi:"))
        t = masafat/tondi
        print("time=",t)
        num2=int(input("num2:"))
        if num2==1:
            y=0
        elif num2==0:
            break
    elif a=="11":
        taqiratsorat=float(input("taqiratsorat:"))
        zamantaqirat=float(input("zamantaqirat:"))
        shetab=taqiratsorat/zamantaqirat
        print("shetab=",shetab)
        num2=int(input("num2:"))
        if num2==1:
            y=0
        elif num2==0:
            break
    
    elif a=="0" :
        break
print("by")
