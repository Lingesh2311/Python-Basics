'''
super() - Returns a temporary object of the super class.
This can be used to access the methods of the super class
without redefining the code again. Reusability is the main
concern with this concept
'''


class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def view_dim(self):
        print(f"Length: {self.length}, Width: {self.width}")
        return '\n'

    def view_area(self):
        print(f"Area: {self.length*self.width}")
        return ''

    def get_area(self):
        return self.length*self.width


class Square():
    def __init__(self, length):
        self.length = length
        self.width = length

    def view_dim(self):
        print(f"Length: {self.length}, Width: {self.width}")
        return '\n'

    def view_area(self):
        print(f"Area: {self.length*self.width}")
        return ''


class SuperSquare(Rectangle):
    '''
    Uses the super() functionality to reuse
    all the methods from the Rectangle Class
    '''
    def __init__(self, length):
        super().__init__(length, length)


class Cube(SuperSquare):
    '''
    Uses the super() functionality to reuse
    all the methods from the Rectangle class
    via the SuperSquare class
    '''
    def __init__(self, length):
        super().__init__(length)

    def view_surface_area(self):
        return f'\nSurface area: {super().get_area()*6}'

    def view_volume(self):
        return f'\nVolume: {super().get_area()*self.length}'


if __name__ == "__main__":
    print('Creating a rectangle of dimensions (10, 20)')
    rect = Rectangle(10, 20)
    print(f'Dimensions are', end=' ')
    print(f'{rect.view_dim()}', end='')
    print(f'{rect.view_area()}', end='')
    print('*'*80)
    print('Creating a square of dimensions (10, 10)')
    sqr = Square(10)
    print(f'Dimensions are', end=' ')
    print(f'{sqr.view_dim()}', end='')
    print(f'{sqr.view_area()}', end='')
    print('*'*80)
    print('Creating a Super Square of dimensions (10, 10)')
    supsqr = SuperSquare(10)
    print(f'Dimensions are', end=' ')
    print(f'{supsqr.view_dim()}', end='')
    print(f'{supsqr.view_area()}', end='')
    print('*'*80)
    print('Creating a cube of length (10)')
    cube = Cube(10)
    print(f'Parameters are', end=' ')
    print(f'{cube.view_surface_area()}', end='')
    print(f'{cube.view_volume()}')
    print('*'*80)
