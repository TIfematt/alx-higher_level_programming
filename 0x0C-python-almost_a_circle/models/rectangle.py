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
