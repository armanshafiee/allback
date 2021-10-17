def primenumber (n) :
    if n == 1 :
        print("1 notprime and notemployee")
        return False
    for _ in range (2, n):
        if n % _ == 0 :
            print("{} {} _ {}".format(n, _, n // _))
            return False 
    else:
        print(n, "is a prime number")
        return True
#a = int(input())
a=100
for n in range(1,a):
    primenumber(n)

