#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

int isalphanumeric(char* string)
{
    int result = 1;

    const char* p = string;

    while (*p != '\0') {
        int isalnum_symbol = isalnum(*p);
        if (!isalnum_symbol) {
            result = 0;
            break;
        }
        ++p;
    }
    
    return result;
}

static PyObject *isalphanumericError;

static PyObject *py_isalphanumeric(PyObject *self, PyObject *args)
{
    char *string;
    if (!PyArg_ParseTuple(args, "s", &string))
    {
        PyErr_SetString(isalphanumericError, "Input must be a string");
        return NULL;
    }

    int result = isalphanumeric(string);
    return Py_BuildValue("O", result ? Py_True : Py_False);
}

static PyMethodDef isalphanumericModuleMethods[] = {
    {"isalphanumeric", py_isalphanumeric, METH_VARARGS, "Checks if the given string consists of alphanumeric characters only"},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef isalphanumericModule = {
    PyModuleDef_HEAD_INIT,
    "isalphanumericModule",
    "Module that checks if the given string consists of alphanumeric characters only",
    -1,
    isalphanumericModuleMethods};

PyMODINIT_FUNC PyInit_isalphanumeric(void)
{
    PyObject *mod = PyModule_Create(&isalphanumericModule);
    isalphanumericError = PyErr_NewException("isalphanumericModule.error", NULL, NULL);
    Py_INCREF(isalphanumericError);
    PyModule_AddObject(mod, "error", isalphanumericError);
    return mod;
}