print("hajm menare")
h_soton = float(input("ertfa soton :"))
r_soton = float(input("shoa soton :"))
h_kolahak = float(input("ertfa kolahak :"))
r_kolahak = float(input("shoa kolahak :"))
r_otaghak = float(input("shoa otaghak :"))
hajm_otaghak = (4*3.14*r_otaghak)/3
hajm_kolahak = ((3.14*r_kolahak**2)*h_kolahak)/3
hajm_soton = (3.14*r_soton**2)*h_soton
hajm_kol = h_kolahak+h_soton+hajm_otaghak
print("hajm menare :",hajm_kol)
