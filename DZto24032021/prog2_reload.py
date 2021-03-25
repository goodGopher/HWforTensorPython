from prog1_figures import Planimetry


class MyComplex():

    Real = 0
    Imagne = 0

    def __init__(self, Re=0, Im=0):

        self.Real = Re
        self.Imagne = Im


    def __eq__(self, o) :
        if self.Real == o.Real and self.Imagne == o.Imagne :
            return True
        else:
            return False

    def __add__ (self, o):
        R = self.Real + o.Real
        I = self.Imagne + o.Imagne

        return MyComplex(R,I)

    def __mul__(self,o):
        return MyComplex(self.Real*o.Real - self.Imagne*o.Imagne, 
                        self.Real*o.Imagne + self.Imagne*o.Real)


a = MyComplex()
a.Imagne = 5
a.Real = 5

b = MyComplex()
b.Imagne = 5
b.Real = 6

print((a*b).Real)