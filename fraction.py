class Fraction:
    
    def __init__(self,n,d):
        self.numerator = n
        self.denominator = d

    def __str__(self):
        return "{}/{}".format(self.numerator,self.denominator)

    def __add__(self,outher):
        temp_numerator = self.numerator*outher.denominator + outher.numerator*self.denominator
        temp_denominator = self.denominator*outher.denominator   
        return "{}/{}".format(temp_numerator,temp_denominator) 

    def __sub__(self,outher):
        temp_numerator = self.numerator*outher.denominator - outher.numerator*self.denominator
        temp_denominator = self.denominator*outher.denominator    
        return "{}/{}".format(temp_numerator,temp_denominator)    

    def __mul__(self,outher):
        temp_numerator = self.numerator*outher.numerator
        temp_denominator = self.denominator*outher.denominator 
        return "{}/{}".format(temp_numerator,temp_denominator)  

    def __truediv__(self,outher):
        temp_numerator = self.numerator*outher.denominator
        temp_denominator = self.denominator*outher.numerator
        return "{}/{}".format(temp_numerator,temp_denominator)
