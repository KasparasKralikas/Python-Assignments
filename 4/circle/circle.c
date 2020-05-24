#include <Python.h>
#include "structmember.h"
#include <stdio.h>
#define M_PI 3.14159265358979323846

typedef struct
{
  PyObject_HEAD float radius;
} Circle;

static PyObject *circleError;

static void Circle_dealloc(Circle *self)
{
  Py_TYPE(self)->tp_free((PyObject *)self);
}

static PyObject *Circle_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
  Circle *self;

  self = (Circle *)type->tp_alloc(type, 0);
  if (self != NULL)
  {
    self->radius = 1;
  }

  return (PyObject *)self;
}

static int Circle_init(Circle *self, PyObject *args, PyObject *kwds)
{
  float radius;
  if (!PyArg_ParseTuple(args, "f", &radius))
    return -1;

  if (radius <= 0)
  {
    PyErr_SetString(circleError, "Circle cannot have a negative radius.");
    return -1;
  }
  self->radius = radius;

  return 0;
}

static PyObject *Circle_perimeter(Circle *self)
{
  char str[20];
  sprintf(str, "%.3f", self->radius * 2 * M_PI);
  return Py_BuildValue("s", str);
}

static PyObject *Circle_area(Circle *self)
{
  float semiPerimeter = (self->radius * self->radius * M_PI);
  char str[20];
  sprintf(str, "%.3f", self->radius * self->radius * M_PI);
  return Py_BuildValue("s", str);
}

static PyObject *Circle_str(Circle *self)
{
  char str[20];
  sprintf(str, "%.2f", self->radius);
  return PyUnicode_FromFormat("radius=%s", str);
}

static PyMemberDef Circle_members[] = {
    {"radius", T_FLOAT, offsetof(Circle, radius), 0, "Radius of the circle"},
    {NULL}};

static PyMethodDef Circle_methods[] = {
    {"perimeter", (PyCFunction)Circle_perimeter, METH_NOARGS, "Returns the perimeter of the circle."},
    {"area", (PyCFunction)Circle_area, METH_NOARGS, "Returns the area of the circle."},
    {NULL}};

static PyTypeObject CircleType = {
    PyVarObject_HEAD_INIT(NULL, 0) "circle.Circle", /* tp_name */
    sizeof(Circle),                                 /* tp_basicsize */
    0,                                              /* tp_itemsize */
    (destructor)Circle_dealloc,                     /* tp_dealloc */
    0,                                              /* tp_print */
    0,                                              /* tp_getattr */
    0,                                              /* tp_setattr */
    0,                                              /* tp_reserved */
    0,                                              /* tp_repr */
    0,                                              /* tp_as_number */
    0,                                              /* tp_as_sequence */
    0,                                              /* tp_as_mapping */
    0,                                              /* tp_hash  */
    0,                                              /* tp_call */
    (reprfunc)Circle_str,                           /* tp_str */
    0,                                              /* tp_getattro */
    0,                                              /* tp_setattro */
    0,                                              /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT |
        Py_TPFLAGS_BASETYPE, /* tp_flags */
    "This is a circle",      /* tp_doc */
    0,                       /* tp_traverse */
    0,                       /* tp_clear */
    0,                       /* tp_richcompare */
    0,                       /* tp_weaklistoffset */
    0,                       /* tp_iter */
    0,                       /* tp_iternext */
    Circle_methods,          /* tp_methods */
    Circle_members,          /* tp_members */
    0,                       /* tp_getset */
    0,                       /* tp_base */
    0,                       /* tp_dict */
    0,                       /* tp_descr_get */
    0,                       /* tp_descr_set */
    0,                       /* tp_dictoffset */
    (initproc)Circle_init,   /* tp_init */
    0,                       /* tp_alloc */
    Circle_new,              /* tp_new */
};

static struct PyModuleDef circleModule = {
    PyModuleDef_HEAD_INIT,
    "circleModule", // name of module
    "Circle type",  // module documentation, may be NULL
    -1,             // size of per- interpreter state of the module, or -1 if the module keeps state in global variables.
    NULL, NULL, NULL, NULL, NULL};

PyMODINIT_FUNC PyInit_circle(void)
{ //import circleModule
  PyObject *m;
  //CircleType.tp_new = PyType_GenericNew;
  if (PyType_Ready(&CircleType) < 0)
    return NULL;
  m = PyModule_Create(&circleModule);
  if (m == NULL)
    return NULL;
  Py_INCREF(&CircleType);
  PyModule_AddObject(m, "Circle", (PyObject *)&CircleType);

  circleError = PyErr_NewException("circle.error", NULL, NULL);
  Py_INCREF(circleError);
  PyModule_AddObject(m, "error", circleError);

  return m;
}