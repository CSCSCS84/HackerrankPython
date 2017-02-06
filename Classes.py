##Collection of Challenges in Domain Python->Classes of Hackerrank

#https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        c = self.real + no.real
        d = self.imaginary + no.imaginary
        return Complex(c, d)

    def __sub__(self, no):
        c = self.real - no.real
        d = self.imaginary - no.imaginary
        return Complex(c, d)

    def __mul__(self, no):
        c = self.real * no.real - self.imaginary * no.imaginary
        d = self.real * no.imaginary + no.real * self.imaginary
        return Complex(c, d)

    def __truediv__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary
        e = (a * c + b * d) / (c * c + d * d)
        f = (b * c - a * d) / (c * c + d * d)
        return Complex(e, f)

    def mod(self):
        c = self.real ** 2 + +self.imaginary ** 2
        c = math.sqrt(c)
        return Complex(c, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

#https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle