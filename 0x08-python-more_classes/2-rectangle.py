#!/usr/bin/python3
"""
created by tife
"""


class Rectangle():
    """
    A class that defines a rectange

    Attributes:
        empty
    """

    def __init__(self, width=0, height=0):
        """
        Init method for rectangle:
            width and height are optional
        Attributes:
            width: (int)
            height: (int)
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Property width to retrive it

        Returns:
            width (int): The height of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter height of the rectangle

        Attributes:
            width (int): The height of the rectangle

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Property height to retrive

        Returns:
            height (int): The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter height of rectangle
        Attributes:
            height (int): The height of the rectangle

        Raises:
            TypeError: if height is not an integer
            ValueError: If height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
            The Area of the rectangle
        """

        return self.__height * self.__width

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle

        Returns:
            The perimeter of the rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
