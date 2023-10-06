#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('7-rectangle').Rectangle

class BaseGeometry:
    """This class represents a base geometry."""

    def area(self):
        """Method not implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value as an integer.
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This class represents a rectangle."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """This class represents a square."""

    def __init__(self, size):
        """Initialize a Square instance.
        Args:
            size (int): The size of the square.
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
