#!/usr/bin/python3
""" A rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instances initialized """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Height setter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height Setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x is not an integer")
        if value < 0:
            raise ValueError("x msut be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y is not an integer")
        if value < 0:
            raise ValueError("y must must be >=0")
        self.__y = value

    def area(self):
        """The area of the rectangle
            Returns: Area of the rectangle

            >>> Rectangle (2, 3)
            >>> 6
        """
        return self.width * self.height

    def display(self):
        """ Prints in stdout the rectangle
            instance with the character #
        """
        rectangle = self.y * "\n"

        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """ str special method """
        str_rectangle = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_rectangle + str_id + str_xy + str_wh

    def update(self, *args, **kwargs):
        """ Update method """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])

            else:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """ A method that returns a dictionary with properties """
        list_atr = ['id', 'width', 'height', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            dict_res[key] = getattr(self, key)

        return dict_res
