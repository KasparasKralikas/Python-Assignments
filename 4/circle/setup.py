from distutils.core import setup, Extension
from setuptools import setup, Extension

module = Extension("circle", sources=["circle.c"])

setup(name="circleModule",
      version="1.0",
      description="Circle module.",
      ext_modules=[module])


# python circleSetup.py install --user
# python
# import circle
# c=circle.circle(5)
# c.perimeter()
# c.area()
