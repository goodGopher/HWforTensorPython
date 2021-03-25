class Figure:
    """"""
    name = "Фигура"
    side = []

    def show_name(self):
        print(self.name)

    def _figure_check(self):
        for i in self.side:
            if i <= 0:
                print(f"Wrong value: {i}")
                raise ValueError

class Planimetry(Figure):
    perimeter = 0
    area = 0

    def calc_perimeter(self):

        if self.perimeter == 0:
            for i in self.side:
                self.perimeter += i
        return self.perimeter
    

class Triangle(Planimetry):

    side = [5,4,3]

    def __init__(self,side1=5,side2=4,side3=3):

        self.name = "Triangle"
        self.side[0] = side1
        self.side[1] = side2
        self.side[2] = side3

        self._triangle_check()
    


    def calc_area(self):
        p = self.calc_perimeter() / 2 
        
        if self.area == 0:
            self.area = (p*(p - self.side[0])*(p - self.side[1])*(p - self.side[2]))**(0.5)
        return self.area
        
    def _triangle_check(self):
        self._figure_check()
        s = 0;
        for i in self.side:
            s += i
        for i in self.side:
            if s / 2 - i <= 0:
                print(f"Definition error: {self.side[0]},{self.side[1]},{self.side[2]} : impossible triangle")
                raise ValueError


class Rectangle(Planimetry):
    
    side = [1,1]


    def __init__(self,side1=1,side2=1):

        self.name = "Rectangle"
        self.side[0] = side1
        self.side[1] = side2
        

        self._figure_check()
    
    def calc_perimeter(self):
        return 2 * super().calc_perimeter()

    def calc_area(self):
        return self.side[0] * self.side[1]
        
   
    


class Stereometry(Figure):
    volume = 0

class Parallelepiped(Stereometry):

    side = [1,1,1]

    def __init__(self,side1=1,side2=1,side3=1):

        self.name = "Parallelepiped"
        self.side[0] = side1
        self.side[1] = side2
        self.side[2] = side3

        self._figure_check()

    def calc_volume(self):
        if self.volume == 0:
            self.volume = self.side[0] * self.side[1]* self.side[2]
        return self.volume

class Сylinder(Stereometry):
    
    side = [1,1]

    def __init__(self,radius=1,height=1):

        self.name = "Сylinder"
        self.side[0] = radius
        self.side[1] = height
        

        self._figure_check()

    def calc_volume(self):
        if self.volume == 0:
            self.volume = (self.side[0]**2) * 3.1415 * self.side[1]
        return self.volume



t = Triangle(2,4,5)
print(t.calc_perimeter())
print(t.calc_area())

r = Rectangle(2,2)
print(r.calc_perimeter())
print(r.calc_area())