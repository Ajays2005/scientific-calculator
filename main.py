class Shape:
    def __init__(self, l=None, w=None, r=None):
        self.width = w
        self.length = l
        self.radius=  r

    '''def getArea(self, option):
        if option == 1:
            self.radius = float(input())
            from math import pi
            return pi+(self.radius**2)
        elif option == 2:
            self.length = int(input())
            return self.length**2
        elif option == 3:
            self.length = int(input())
            self.width = int(input())
            return self.length*self.width
        else:
            return 'Invalid option'
    print(f'1.circle/n2.square/n3.Rectangle')
    option = int(input('Choose an item.....'))
    s=Shape()
    print(s.getArea(option))
    '''

