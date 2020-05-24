from distutils.core import setup, Extension

module = Extension("isalphanumeric", sources=["isalphanumeric.c"])

setup(name="isalphanumeric", ext_modules=[module])

# python setup.py install --user
# python
# import isalphanumeric
# isalphanumeric.isalphanumeric("test")