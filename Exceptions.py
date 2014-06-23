# -*- coding: utf-8 -*-

"""
project.exceptions
------------------

All exceptions used in the project code base are defined here.
"""


class ProjectException(Exception):
    """
    Base exception class. All Project-specific exceptions should subclass
    this class.
    """


class FieldLengthOverflow(ProjectException):
    """
    Raised when a field length overflow occurred
    """

