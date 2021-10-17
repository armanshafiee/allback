
class point:
    
    def __init__ (self , x , y ):
        self. x = x 
        self. y = y 
    def distance(p):
        c=sqrt( (p.x-self. x)**2 + (p.y-self.y)**2 ) 

        return c 

class line :
    def __init__ (self, s,e):
    
        self.s = s
        self.e = e
        self.width = 1
        self.color = "black"
    
    def increase(self,size):
    
        self.width=self.width + size
    
    def get_length(self):
    
        return self.s.get_distance(self.e)
    
    def slope(self):
    
        z=self.s.x-self.e.x
        t=self.s.y=self.e.y
        dd=z/t
            return dd    
    
    def arecross(self ,l):
    
        if slope(l) == slope(self):
    
            return False 
    
        else :
    
            return True

#class ploygon:

#    def __init__ ():



