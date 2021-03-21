"""Solving a quadratic equation."""

def main():
    """Solving a quadratic equation."""
    print("уравнение вида ax^2+bx+c=0\n")
    print("Enter a:")
    a = float(input())
    print("Enter b:")
    b = float(input())
    print("Enter c:")
    c = float(input())
    if a == 0:
        if b == 0:
            if c == 0:
                print("уравнение имеет бесконечное количество решений")
            else:
                print("нет решений")
        else:
            print("x = ", -c/b)
    else: 
        D = b*b - 4*a*c
        if D < 0:
            print("D < 0, уравнение не имеет действительных корней")
            print("x1 = ",-b/(2*a),"+i",abs(D)**(1/2)/(2*a))
            print("x2 = ",-b/(2*a),"-i",abs(D)**(1/2)/(2*a))
        elif D == 0:
            print("x = ",-b/(2*a))
        else:
            print("уравнение имеет два разных корня")
            print("x1 = ",((-b+D**(1/2))/(2*a)))
            print("x2 = ",((-b-D**(1/2))/(2*a)))
    input()

if __name__ == "__main__":
    main()